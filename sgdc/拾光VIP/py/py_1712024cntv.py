#coding=utf-8
#!/usr/bin/python
import re
import sys
import time
import json
from urllib.parse import quote
sys.path.append('..')
from base.spider import Spider

class Spider(Spider):  # 元类 默认的元类 type
	def getName(self):
		return "中央电视台"

	def init(self, extend):
		pass

	def destroy(self):
		pass

	def isVideoFormat(self, url):
		pass

	def manualVideoCheck(self):
		pass

	def homeContent(self, filter):
		result = {}
		cateManual = {
			"栏目大全": "栏目大全",
			"特别节目": "特别节目"
		}
		classes = []
		for k in cateManual:
			classes.append({
				'type_name': k,
				'type_id': cateManual[k]
			})
		result['class'] = classes
		if filter:
			import datetime
			result['filters'] = self.config['filter']
			currentYear = datetime.datetime.now().year
			yearList = [{"n": "全部", "v": ""}]
			for year in range(currentYear, currentYear - 10, -1):
				yearList.append({"n": year, "v": year})
			for classe in classes:
				if classe['type_id'] == '栏目大全':
					key = 'year'
				elif classe['type_id'] == '特别节目':
					key = 'datanf-year'
				else:
					key = 'year'
				yearDict = {"key": key, "name": "年份", "value": yearList}
				if yearDict not in result['filters'][classe['type_id']]:
					result['filters'][classe['type_id']].append(yearDict)
		return result

	def homeVideoContent(self):
		result = {
			'list': []
		}
		return result

	def categoryContent(self, cid, page, filter, ext):
		result = {}
		params = {
			'n': '20',
			'p': page,
			't': 'json',
			'serviceId': 'tvcctv'
		}
		year = ''
		month = ''
		for key in ext.keys():
			if key == 'year':
				year = ext['year']
			elif key == 'month':
				month = ext['month']
			else:
				params[key] = ext[key]
		if year == '':
			date = ''
		else:
			date = year + month
		if cid == '栏目大全':
			url = 'https://api.cntv.cn/lanmu/columnSearch?'
			for key in params:
				url += f'{key}={params[key]}&'
			url = url.strip('&')
			data = self.fetch(url, headers=self.header, timeout=10).json()
			vodList = data['response']['docs']
			videos = []
			for vod in vodList:
				lastVideo = vod['lastVIDE']['videoSharedCode']
				if len(lastVideo) == 0:
					lastVideo = '_'
				guid = json.dumps({'cid': '栏目大全', 'date': date, 'title': vod['column_name'], 'lastVideo': lastVideo, 'logo': vod['column_logo']}, ensure_ascii=False)
				title = vod['column_name']
				img = vod['column_logo']
				videos.append({
					"vod_id": guid,
					"vod_name": title,
					"vod_pic": img,
					"vod_remarks": ''
				})
			lenvodList = len(vodList)
			page = int(page)
			if lenvodList * page < data['response']['numFound']:
				pagecount = page + 1
			else:
				pagecount = page
		elif cid == '特别节目':
			url = f'https://api.cntv.cn/list/getVideoAlbumList?channelid=CHAL1460955953877151&fc={quote(cid)}&'
			for key in params:
				if key.startswith('data'):
					keyName = key.split('-')[1]
				else:
					keyName = key
				url += f'{keyName}={quote(params[key])}&'
			url = url.strip('&')
			data = self.fetch(url, headers=self.header, timeout=10).json()
			vodList = data['data']['list']
			videos = []
			for vod in vodList:
				guid = json.dumps({'cid': '特别节目', 'date': date, 'title': vod['title'], 'vid': vod['id'], 'logo': vod['image'], 'content': vod['brief']}, ensure_ascii=False)
				title = vod['title']
				img = vod['image']
				videos.append({
					"vod_id": guid,
					"vod_name": title,
					"vod_pic": img,
					"vod_remarks": ''
				})
			lenvodList = len(vodList)
			page = int(page)
			if lenvodList * page < data['data']['total']:
				pagecount = page + 1
			else:
				pagecount = page
		else:
			videos = []
			lenvodList = 0
			pagecount = page

		result['list'] = videos
		result['page'] = page
		result['pagecount'] = pagecount
		result['limit'] = lenvodList
		result['total'] = lenvodList
		return result

	def detailContent(self, did):
		videoList = []
		params = json.loads(did[0])
		cid = params['cid']
		date = params['date']
		if date == '':
			content = '仅展示近100期节目，其余节目通过筛选访问\n'
		else:
			content = ''
		if cid == '栏目大全':
			title = params['title']
			logo = params['logo']
			lastVideo = params['lastVideo']
			if lastVideo == '_':
				return {}
			url = f"https://api.cntv.cn/video/videoinfoByGuid?serviceId=tvcctv&guid={lastVideo}"
			data = self.fetch(url, headers=self.header, timeout=10).json()
			topicId = data['ctid']
			content = content + data['vset_brief']
			url = f"https://api.cntv.cn/NewVideo/getVideoListByColumn?n=100&t=json&mode=0&sort=desc&serviceId=tvcctv&d={date}&id={topicId}"
			data = self.fetch(url, headers=self.header, timeout=10).json()
			vodList = data['data']['list']
			for video in vodList:
				videoList.append(video['title'] + "$" + video['guid'])
			for video in vodList:
				videoList.append(video['title'] + "$" + video['guid'])
		elif cid == '特别节目':
			title = params['title']
			logo = params['logo']
			content += params['content']
			url = f'https://api.cntv.cn/NewVideo/getVideoListByAlbumIdNew?id={params["vid"]}&serviceId=tvcctv&p=1&n=100&mode=0&pub=1'
			r = self.fetch(url, headers=self.header, timeout=10)
			data = r.json()
			vodList = data['data']['list']
			if len(vodList) == 0:
				vodList = re.finditer(r'href="(?P<guid>.+?)" target="_blank" alt="(?P<title>.+?)" title=".+?">', r.text, re.M | re.S)
			for video in vodList:
				try:
					name = video['title']
					guid = video['guid']
				except:
					name = video.group('title')
					guid = video.group('guid')
				if len(guid) == 0:
					continue
				videoList.append(name + "$" + guid)
			if len(videoList) == 0:
				return {}
			if len(date) == 0:
				date = time.strftime("%Y", time.localtime(time.time()))
		else:
			title = ''
			logo = ''
		vod = {"vod_id": did[0], "vod_name": date + " " + title, "vod_pic": logo, "vod_year": date, "vod_remarks": date, "vod_content": content}
		vod['vod_play_from'] = 'CCTV'
		vod['vod_play_url'] = "#".join(videoList)
		result = {'list': [vod]}
		return result

	def searchContent(self, key, quick):
		return self.searchContentPage(key, quick, '1')

	def searchContentPage(self, key, quick, page):
		result = {}
		return result

	def playerContent(self, flag, pid, vipFlags):
		result = {}
		url = f"https://vdn.apps.cntv.cn/api/getHttpVideoInfo.do?pid={pid}"
		data = self.fetch(url, headers=self.header, timeout=10).json()
		url = data['hls_url'].strip()
		result["parse"] = 0
		result["playUrl"] = ''
		result["url"] = url
		result["header"] = ''
		return result

	config = {"filter": {"栏目大全": [{"key": "cid", "name": "频道", "value": [{"n": "全部", "v": ""}, {"n": "CCTV-1综合", "v": "EPGC1386744804340101"}, {"n": "CCTV-2财经", "v": "EPGC1386744804340102"}, {"n": "CCTV-3综艺", "v": "EPGC1386744804340103"}, {"n": "CCTV-4中文国际", "v": "EPGC1386744804340104"}, {"n": "CCTV-5体育", "v": "EPGC1386744804340107"}, {"n": "CCTV-6电影", "v": "EPGC1386744804340108"}, {"n": "CCTV-7国防军事", "v": "EPGC1386744804340109"}, {"n": "CCTV-8电视剧", "v": "EPGC1386744804340110"}, {"n": "CCTV-9纪录", "v": "EPGC1386744804340112"}, {"n": "CCTV-10科教", "v": "EPGC1386744804340113"}, {"n": "CCTV-11戏曲", "v": "EPGC1386744804340114"}, {"n": "CCTV-12社会与法", "v": "EPGC1386744804340115"}, {"n": "CCTV-13新闻", "v": "EPGC1386744804340116"}, {"n": "CCTV-14少儿", "v": "EPGC1386744804340117"}, {"n": "CCTV-15音乐", "v": "EPGC1386744804340118"}, {"n": "CCTV-16奥林匹克", "v": "EPGC1634630207058998"}, {"n": "CCTV-17农业农村", "v": "EPGC1563932742616872"}, {"n": "CCTV-5+体育赛事", "v": "EPGC1468294755566101"}]}, {"key": "fc", "name": "分类", "value": [{"n": "全部", "v": ""}, {"n": "新闻", "v": "新闻"}, {"n": "体育", "v": "体育"}, {"n": "综艺", "v": "综艺"}, {"n": "健康", "v": "健康"}, {"n": "生活", "v": "生活"}, {"n": "科教", "v": "科教"}, {"n": "经济", "v": "经济"}, {"n": "农业", "v": "农业"}, {"n": "法治", "v": "法治"}, {"n": "军事", "v": "军事"}, {"n": "少儿", "v": "少儿"}, {"n": "动画", "v": "动画"}, {"n": "纪实", "v": "纪实"}, {"n": "戏曲", "v": "戏曲"}, {"n": "音乐", "v": "音乐"}, {"n": "影视", "v": "影视"}]}, {"key": "fl", "name": "字母", "value": [{"n": "全部", "v": ""}, {"n": "A", "v": "A"}, {"n": "B", "v": "B"}, {"n": "C", "v": "C"}, {"n": "D", "v": "D"}, {"n": "E", "v": "E"}, {"n": "F", "v": "F"}, {"n": "G", "v": "G"}, {"n": "H", "v": "H"}, {"n": "I", "v": "I"}, {"n": "J", "v": "J"}, {"n": "K", "v": "K"}, {"n": "L", "v": "L"}, {"n": "M", "v": "M"}, {"n": "N", "v": "N"}, {"n": "O", "v": "O"}, {"n": "P", "v": "P"}, {"n": "Q", "v": "Q"}, {"n": "R", "v": "R"}, {"n": "S", "v": "S"}, {"n": "T", "v": "T"}, {"n": "U", "v": "U"}, {"n": "V", "v": "V"}, {"n": "W", "v": "W"}, {"n": "X", "v": "X"}, {"n": "Y", "v": "Y"}, {"n": "Z", "v": "Z"}]}, {"key": "month", "name": "月份", "value": [{"n": "全部", "v": ""}, {"n": "12", "v": "12"}, {"n": "11", "v": "11"}, {"n": "10", "v": "10"}, {"n": "09", "v": "09"}, {"n": "08", "v": "08"}, {"n": "07", "v": "07"}, {"n": "06", "v": "06"}, {"n": "05", "v": "05"}, {"n": "04", "v": "04"}, {"n": "03", "v": "03"}, {"n": "02", "v": "02"}, {"n": "01", "v": "01"}]}], "特别节目": [{"key": "datapd-channel", "name": "频道", "value": [{"n": "全部", "v": ""}, {"n": "CCTV-1 综合", "v": "CCTV-1综合,CCTV-1高清,CCTV-1综合高清"}, {"n": "CCTV-2 财经", "v": "CCTV-2财经,CCTV-2高清,CCTV-2财经高清"}, {"n": "CCTV-3 综艺", "v": "CCTV-3综艺,CCTV-3高清,CCTV-3综艺高清"}, {"n": "CCTV-4 中文国际", "v": "CCTV-4中文国际,CCTV-4高清,CCTV-4中文国际(亚)高清"}, {"n": "CCTV-5 体育", "v": "CCTV-5体育,CCTV-5高清,CCTV-5体育高清"}, {"n": "CCTV-6 电影", "v": "CCTV-6电影,CCTV-6高清,CCTV-6电影高清"}, {"n": "CCTV-7 国防军事", "v": "CCTV-7军事农业,CCTV-7高清,CCTV-7军事农业高清,CCTV-7国防军事高清"}, {"n": "CCTV-8 电视剧", "v": "CCTV-8电视剧,CCTV-8高清,CCTV-8电视剧高清"}, {"n": "CCTV-9 纪录", "v": "CCTV-9纪录,CCTV-9高清,CCTV-9纪录高清"}, {"n": "CCTV-10 科教", "v": "CCTV-10科教,CCTV-10高清,CCTV-10科教高清"}, {"n": "CCTV-11 戏曲", "v": "CCTV-11戏曲,CCTV-11高清,CCTV-11戏曲高清"}, {"n": "CCTV-12 社会与法", "v": "CCTV-12社会与法,CCTV-12高清,CCTV-12社会与法高清"}, {"n": "CCTV-13 新闻", "v": "CCTV-13新闻,CCTV-13高清,CCTV-13新闻高清"}, {"n": "CCTV-14 少儿", "v": "CCTV-14少儿,CCTV-14高清,CCTV-14少儿高清"}, {"n": "CCTV-15 音乐", "v": "CCTV-15音乐,CCTV-15高清,CCTV-15音乐高清"}, {"n": "CCTV-17 农业农村", "v": "CCTV-17农业农村高清"}]}, {"key": "datafl-sc", "name": "类型", "value": [{"n": "全部", "v": ""}, {"n": "新闻", "v": "新闻"}, {"n": "经济", "v": "经济"}, {"n": "综艺", "v": "综艺"}, {"n": "体育", "v": "体育"}, {"n": "军事", "v": "军事"}, {"n": "影视", "v": "影视"}, {"n": "科教", "v": "科教"}, {"n": "戏曲", "v": "戏曲"}, {"n": "青少", "v": "青少"}, {"n": "音乐", "v": "音乐"}, {"n": "社会", "v": "社会"}, {"n": "文化", "v": "文化"}, {"n": "公益", "v": "公益"}, {"n": "其他", "v": "其他"}]}, {"key": "dataszm-letter", "name": "首字母", "value": [{"n": "全部", "v": ""}, {"n": "A", "v": "A"}, {"n": "B", "v": "B"}, {"n": "C", "v": "C"}, {"n": "D", "v": "D"}, {"n": "E", "v": "E"}, {"n": "F", "v": "F"}, {"n": "G", "v": "G"}, {"n": "H", "v": "H"}, {"n": "I", "v": "I"}, {"n": "J", "v": "J"}, {"n": "K", "v": "K"}, {"n": "L", "v": "L"}, {"n": "M", "v": "M"}, {"n": "N", "v": "N"}, {"n": "O", "v": "O"}, {"n": "P", "v": "P"}, {"n": "Q", "v": "Q"}, {"n": "R", "v": "R"}, {"n": "S", "v": "S"}, {"n": "T", "v": "T"}, {"n": "U", "v": "U"}, {"n": "V", "v": "V"}, {"n": "W", "v": "W"}, {"n": "X", "v": "X"}, {"n": "Y", "v": "Y"}, {"n": "Z", "v": "Z"}]}]}}
	header = {
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36",
		"Origin": "https://tv.cctv.com",
		"Referer": "https://tv.cctv.com/"
	}

	def localProxy(self, param):
		return [200, "video/MP2T", ""]