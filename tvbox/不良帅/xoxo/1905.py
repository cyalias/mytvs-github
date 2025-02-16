#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider
import json
import re
import time
import uuid
import hashlib
from urllib import request, parse
import urllib
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context#全局取消证书验证
class Spider(Spider):  # 元类 默认的元类 type
	def getName(self):
		return "1905电影"
	def init(self,extend=""):
		print("============{0}============".format(extend))
		pass
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def homeContent(self,filter):
		result = {}
		cateManual = {
			"电影": "n_1",
			"微电影":"n_1_c_922",
			"系列电影":"n_2",
			"纪录片":"c_927",
			"晚会":"n_1_c_586",
			"独家":"n_1_c_178",
			"综艺":"n_1_c_1024"
			# ,"体育":"n_1_c_1053"
			}
		classes = []
		for k in cateManual:
			classes.append({
				'type_name':k,
				'type_id':cateManual[k]
			})
		result['class'] = classes
		if(filter):
			result['filters'] = self.config['filter']
		return result
	def homeVideoContent(self):
		url = 'https://www.1905.com/vod/cctv6/lst/'
		rsp = self.fetch(url, headers=self.header)
		html = self.html(rsp.text)
		aList = html.xpath("//div[@class='grid-2x']/a")
		videos = self.custom_list(aList=aList)
		result = {
			'list':videos
		}
		return result
	def categoryContent(self,tid,pg,filter,extend):
		result = {}
		videos=[]
		by='/o3p'
		if 'by' in extend.keys():
			by='/{0}p'.format(extend['by'])
		url = 'https://www.1905.com/vod/list/{0}{2}{1}.html'.format(tid, pg,by)
		HtmlTxt =self.custom_webReadFile(url,header=self.header)
		html = self.html(HtmlTxt)
		aList = html.xpath("//section[contains(@class,'search-list')]/div/a" if tid != u'n_2' else "//div[@class='mod']/div[1]/a")
		videos = self.custom_list(aList=aList)
		limit = len(aList)
		result['list'] = videos
		result['page'] = pg
		result['pagecount'] = 100
		result['limit'] = limit
		result['total'] = 100 * limit
		return result
	def detailContent(self,array):
		result = {}
		temporary = array[0].split('###')
		title=temporary[1]
		aid=temporary[0]
		pic=temporary[2]
		remark=''
		actor=''
		direct=''
		content=''
		vodItems=[]
		playList=[]
		vod_play_from=['播放线路',]
		if aid.isdigit()==False:			
			HtmlTxt=self.custom_webReadFile(aid,self.header)
			url=self.custom_RegexGetText(HtmlTxt,r'<a class="iconBanner-playBtn icon-banner btn-play"\s*href="(.+?)"',1)
			if url=='':
				url=self.custom_RegexGetText(HtmlTxt,r'property="og:url"\scontent="(.+?)"', 1)
			if self.custom_RegexGetText(url,r'/(film)/',1)!='':
				HtmlTxt=self.custom_webReadFile(aid+'video',self.header)
				url=self.custom_RegexGetText(HtmlTxt,r'<li class="video-position-icon\s{0,1}">\r*\n*\s*<a href="(.+?)"\s{1,4}class="online-list-positive other-vedio-url"', 1)
			if len(self.custom_RegexGetText(url,r'(vip.1905)',1))>3:
				vod_play_from=['播放线路(需要vip解析)',]
				aid=url
				title=self.custom_RegexGetText(HtmlTxt,r'<div class="container-right">\s*\r*\n*\t*<h1>(.+?)<',1).replace(' ','')
				pic=self.custom_RegexGetText(HtmlTxt,r'<img class="poster" src="(.+?)"',1)
				content=self.custom_RegexGetText(HtmlTxt,r'<p>(.+?)</p>',1)
				vodItems.append(title + "$" + aid)
				joinStr = '#'.join(vodItems)
				playList.append(joinStr)
			else:
				aid=self.custom_RegexGetText(url,r'play/(.*?)\.sh',1)
		if aid=='':
			return  {'list': []}
		elif  aid.isdigit() and vod_play_from[0].find('需要vip解析')<0:
			url = "https://www.1905.com/api/content/?callback=&m=Vod&a=getVodSidebar&id={0}&fomat=json".format(aid)
			try:
				HtmlTxt=self.custom_webReadFile(url,self.header)
				root = json.loads(HtmlTxt)
				title = root['title']
				pic = root['thumb']
				remark = root['commendreason']
				content = root['description']
				actor = root['starring']
				direct = root['direct']
				vodItems.append(title + "$" + aid)
				series = root['info']['series_data']
				series = root['info']['series_data']
				for ser in series:
					vodItems.append(ser['title'] + "$" + ser['contentid'])
				joinStr = '#'.join(vodItems)
				playList.append(joinStr)
			except:
				joinStr = '#'.join([title + "$" + aid])
				playList.append(joinStr)
		else:
			pass
			
		vod = {
			"vod_id":array[0],
			"vod_name":title,
			"vod_pic":pic,
			"type_name":'',
			"vod_year":"",
			"vod_area":"",
			"vod_remarks":remark,
			"vod_actor":actor,
			"vod_director":direct,
			"vod_content":content
		}
		vod['vod_play_from'] =  "$$$".join(vod_play_from)
		vod['vod_play_url'] = "$$$".join(playList)
		result = {
			'list':[
				vod
			]
		}
		return result

	def searchContent(self,key,quick):
		url = 'https://www.1905.com/search/index-p-type-film-q-{}.html?envod=1&year=0&score=0&order=0'.format(urllib.parse.quote(key))#只搜索能看电影,想搜其它的可以把html之后的字符删掉
		#https://www.1905.com/search/index-p-type-all-q-{}.html
		html = self.html(self.custom_webReadFile(url,self.header))
		aList = html.xpath('//div[@class="main clearfix"]')
		videos = self.custom_list_search(aList=aList)
		result = {
			'list':videos
		}
		return result
	def playerContent(self,flag,id,vipFlags):
		result = {}
		if flag.find('vip解析')>0:
			result["parse"] = 1#0=直接播放、1=嗅探
			result["playUrl"] =''
			result["url"] = id
			result['jx'] = 1#1=VIP解析,0=不解析
			result["header"] = ''
		else:
			nonce = int(round(time.time() * 1000))
			expiretime = nonce + 600
			uid = str(uuid.uuid4())
			playerid = uid.replace("-", "")[5:20]
			signature = 'cid={0}&expiretime={1}&nonce={2}&page=https%3A%2F%2Fwww.1905.com%2Fvod%2Fplay%2F{3}.shtml&playerid={4}&type=hls&uuid={5}.dde3d61a0411511d'.format(id,expiretime,nonce,id,playerid,uid)
			signature = hashlib.sha1(signature.encode()).hexdigest()
			url = 'https://profile.m1905.com/mvod/getVideoinfo.php?nonce={0}&expiretime={1}&cid={2}&uuid={3}&playerid={4}&page=https%3A%2F%2Fwww.1905.com%2Fvod%2Fplay%2F{5}.shtml&type=hls&signature={6}&callback='.format(nonce,expiretime,id,uid,playerid,id,signature)
			HtmlTxt=self.custom_webReadFile(url,self.header)
			jo = json.loads(HtmlTxt.replace("(", "").replace(")", ""))
			data = jo['data']['sign']
			sign = ''
			qualityStr = ''
			if 'uhd' in data.keys():
				sign = data['uhd']['sign']
				qualityStr = 'uhd'
			elif 'hd' in data.keys():
				sign = data['hd']['sign']
				qualityStr = 'hd'
			elif 'sd' in data.keys():
				sign = data['sd']['sign']
				qualityStr = 'sd'
			host = jo['data']['quality'][qualityStr]['host']
			path = jo['data']['path'][qualityStr]['path']
			playUrl = host + sign + path
			result["parse"] = 0#0=直接播放、1=嗅探
			result["playUrl"] =''
			result["url"] = playUrl
			result["header"] = self.header
		return result


	config = {
		"player": {},
		"filter": {
		"n_1":[
		{"key":"by","name":"排序:","value":[{"n":"默认(最热)","v":"o3"},{"n":"最新","v":"o1"},{"n":"好评","v":"o4"}]}
		],
		"n_1_c_922":[
		{"key":"by","name":"排序:","value":[{"n":"默认(最热)","v":"o3"},{"n":"最新","v":"o1"},{"n":"好评","v":"o4"}]}
		],
		"n_2":[
		{"key":"by","name":"排序:","value":[{"n":"默认(最热)","v":"o3"},{"n":"最新","v":"o1"},{"n":"好评","v":"o4"}]}
		],
		"c_927":[
		{"key":"by","name":"排序:","value":[{"n":"默认(最热)","v":"o3"},{"n":"最新","v":"o1"},{"n":"好评","v":"o4"}]}
		],
		"n_1_c_586":[
		{"key":"by","name":"排序:","value":[{"n":"默认(最热)","v":"o3"},{"n":"最新","v":"o1"},{"n":"好评","v":"o4"}]}
		],
		"n_1_c_178":[
		{"key":"by","name":"排序:","value":[{"n":"默认(最热)","v":"o3"},{"n":"最新","v":"o1"},{"n":"好评","v":"o4"}]}
		],
		"n_1_c_1024":[
		{"key":"by","name":"排序:","value":[{"n":"默认(最热)","v":"o3"},{"n":"最新","v":"o1"},{"n":"好评","v":"o4"}]}
		]					
		}
		}
	header = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.43',
        'Referer': 'https://www.1905.com/vod/list/n_1/o3p1.html',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
	}
	def localProxy(self,param):
		return [200, "video/MP2T", action, ""]
	#-----------------------------------------------自定义函数-----------------------------------------------
	#分类取结果
	def custom_list(self,aList):
		videos = []
		for a in aList:
			img=a.xpath('./img/@src')[0]
			title=a.xpath('./img/@alt')[0]
			url=a.xpath("./@href")[0]
			if url.find('vip.1905')>1:#可以除掉
				continue
			if self.custom_RegexGetText(url,'(play)',1)=='':
				vod_id="{0}###{1}###{2}".format(url,title,img)
			else:
				id=self.custom_RegexGetText(url,r'play/(.*?)\.sh',1)
				vod_id="{0}###{1}###{2}".format(id,title,img)
			videos.append({
					"vod_id":vod_id,
					"vod_name":title,
					"vod_pic":img,
					"vod_remarks":''
				})
		return videos
	def custom_list_search(self,aList):
		videos = []
		for a in aList:
			try:
				img=a.xpath('./div[@class="movie-pic"]/a[@class="img-a"]/img/@src')[0]
				title=a.xpath('./div[@class="movie-pic"]/a[@class="img-a"]/img/@alt')[0]
				url=a.xpath('./ul[@class="cont"]/li[@class="spec paly-tab-icon position-icon"]/a/@href')
				if len(url)<1:
					url=a.xpath('./div[@class="movie-pic"]/a[@class="img-a"]/@href')[0]
				else:
					url=url[0]
					if url.find('vip.1905')>1:
						url=a.xpath('./div[@class="movie-pic"]/a[@class="img-a"]/@href')[0]
				if self.custom_RegexGetText(url,'(play)',1)=='':
					vod_id="{0}###{1}###{2}".format(url,title,img)
				else:
					id=self.custom_RegexGetText(url,r'play/(.*?)\.sh',1)
					vod_id="{0}###{1}###{2}".format(id,title,img)
				videos.append({
						"vod_id":vod_id,
						"vod_name":title,
						"vod_pic":img,
						"vod_remarks":''
					})
			except:
				pass
		return videos
	#访问网页
	def custom_webReadFile(self,urlStr,header=None,codeName='utf-8'):
		html=''
		if header==None:
			header={
				"Referer":urlStr,
				'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
				"Host":self.custom_RegexGetText(Text=urlStr,RegexText='https*://(.*?)(/|$)',Index=1)
			}
		req=urllib.request.Request(url=urlStr,headers=header)#,headers=header
		with  urllib.request.urlopen(req)  as response:
			html = response.read().decode(codeName,'ignore')
		return html

	#正则取文本
	def custom_RegexGetText(self,Text,RegexText,Index):
		returnTxt=""
		Regex=re.search(RegexText, Text, re.M|re.S)
		if Regex is None:
			returnTxt=""
		else:
			returnTxt=Regex.group(Index)
		return returnTxt