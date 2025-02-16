"""

作者 凯悦宾馆 🚓 内容均从互联网收集而来 仅供交流学习使用 版权归原创者所有 如侵犯了您的权益 请通知作者 将及时删除侵权内容
                    ====================kaiyuebinguan====================

"""

import requests
from bs4 import BeautifulSoup
import re
from base.spider import Spider
import sys
import json
import base64
import urllib.parse

sys.path.append('..')

xurl = "https://www.netfly.tv"

headerx = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

pm = ''


class Spider(Spider):
    global xurl
    global headerx

    def getName(self):
        return "首页"

    def init(self, extend):
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def extract_middle_text(self, text, start_str, end_str, pl, start_index1: str = '', end_index2: str = ''):
        if pl == 3:
            plx = []
            while True:
                start_index = text.find(start_str)
                if start_index == -1:
                    break
                end_index = text.find(end_str, start_index + len(start_str))
                if end_index == -1:
                    break
                middle_text = text[start_index + len(start_str):end_index]
                plx.append(middle_text)
                text = text.replace(start_str + middle_text + end_str, '')
            if len(plx) > 0:
                purl = ''
                for i in range(len(plx)):
                    matches = re.findall(start_index1, plx[i])
                    output = ""
                    for match in matches:
                        match3 = re.search(r'(?:^|[^0-9])(\d+)(?:[^0-9]|$)', match[1])
                        if match3:
                            number = match3.group(1)
                        else:
                            number = 0
                        if 'http' not in match[0]:
                            output += f"#{'📽️丢丢👉' + match[1]}${number}{xurl}{match[0]}"
                        else:
                            output += f"#{'📽️丢丢👉' + match[1]}${number}{match[0]}"
                    output = output[1:]
                    purl = purl + output + "$$$"
                purl = purl[:-3]
                return purl
            else:
                return ""
        else:
            start_index = text.find(start_str)
            if start_index == -1:
                return ""
            end_index = text.find(end_str, start_index + len(start_str))
            if end_index == -1:
                return ""

        if pl == 0:
            middle_text = text[start_index + len(start_str):end_index]
            return middle_text.replace("\\", "")

        if pl == 1:
            middle_text = text[start_index + len(start_str):end_index]
            matches = re.findall(start_index1, middle_text)
            if matches:
                jg = ' '.join(matches)
                return jg

        if pl == 2:
            middle_text = text[start_index + len(start_str):end_index]
            matches = re.findall(start_index1, middle_text)
            if matches:
                new_list = [f'✨丢丢👉{item}' for item in matches]
                jg = '$$$'.join(new_list)
                return jg

    def homeContent(self, filter):
        result = {}
        result = {"class": [{"type_id": "/vod/show/1", "type_name": "丢丢电影🌠"},
                            {"type_id": "/vod/show/2", "type_name": "丢丢剧集🌠"},
                            {"type_id": "/vod/show/3", "type_name": "丢丢综艺🌠"},
                            {"type_id": "/vod/show/4", "type_name": "丢丢动漫🌠"},
                            {"type_id": "/vod/show/5", "type_name": "丢丢其他🌠"}],

                  "list": [],
                  "filters": {"/vod/show/1": [{"key": "年代",
                                              "name": "年代",
                                              "value": [{"n": "全部", "v": ""},
                                                        {"n": "2024", "v": "2024"},
                                                        {"n": "2023", "v": "2023"},
                                                        {"n": "2022", "v": "2022"},
                                                        {"n": "2021", "v": "2021"},
                                                        {"n": "2020", "v": "2020"},
                                                        {"n": "2019", "v": "2019"},
                                                        {"n": "2018", "v": "2018"}]}],
                              "/vod/show/2": [{"key": "年代",
                                              "name": "年代",
                                              "value": [{"n": "全部", "v": ""},
                                                        {"n": "2024", "v": "2024"},
                                                        {"n": "2023", "v": "2023"},
                                                        {"n": "2022", "v": "2022"},
                                                        {"n": "2021", "v": "2021"},
                                                        {"n": "2020", "v": "2020"},
                                                        {"n": "2019", "v": "2019"},
                                                        {"n": "2018", "v": "2018"}]}],
                              "/vod/show/3": [{"key": "年代",
                                              "name": "年代",
                                              "value": [{"n": "全部", "v": ""},
                                                        {"n": "2024", "v": "2024"},
                                                        {"n": "2023", "v": "2023"},
                                                        {"n": "2022", "v": "2022"},
                                                        {"n": "2021", "v": "2021"},
                                                        {"n": "2020", "v": "2020"},
                                                        {"n": "2019", "v": "2019"},
                                                        {"n": "2018", "v": "2018"}]}],
                              "/vod/show/4": [{"key": "年代",
                                              "name": "年代",
                                              "value": [{"n": "全部", "v": ""},
                                                        {"n": "2024", "v": "2024"},
                                                        {"n": "2023", "v": "2023"},
                                                        {"n": "2022", "v": "2022"},
                                                        {"n": "2021", "v": "2021"},
                                                        {"n": "2020", "v": "2020"},
                                                        {"n": "2019", "v": "2019"},
                                                        {"n": "2018", "v": "2018"}]}],
                              "/vod/show/5": [{"key": "年代",
                                              "name": "年代",
                                              "value": [{"n": "全部", "v": ""},
                                                        {"n": "2024", "v": "2024"},
                                                        {"n": "2023", "v": "2023"},
                                                        {"n": "2022", "v": "2022"},
                                                        {"n": "2021", "v": "2021"},
                                                        {"n": "2020", "v": "2020"},
                                                        {"n": "2019", "v": "2019"},
                                                        {"n": "2018", "v": "2018"}]}]}}

        return result

    def homeVideoContent(self):
        videos = []
        try:
            detail = requests.get(url=xurl, headers=headerx)
            detail.encoding = "utf-8"
            res = detail.text
            res = self.extract_middle_text(res, '<div class="module">', '专题片单', 0)
            doc = BeautifulSoup(res, "lxml")

            soups = doc.find_all('div', class_="module-items")

            for soup in soups:
                vods = soup.find_all('a')

                for vod in vods:

                    name = vod['title']

                    id = vod['href']

                    pics = vod.find('div', class_="module-item-pic")
                    pic = pics.find('img')['data-original']

                    if 'http' not in pic:
                        pic = xurl + pic

                    remark = self.extract_middle_text(str(vod), 'module-item-note">', '</div>', 0)

                    video = {
                        "vod_id": id,
                        "vod_name": '丢丢📽️' + name,
                        "vod_pic": pic,
                        "vod_remarks": '丢丢▶️' + remark
                             }
                    videos.append(video)

            result = {'list': videos}
            return result
        except:
            pass

    def categoryContent(self, cid, pg, filter, ext):
        result = {}
        if pg:
            page = int(pg)
        else:
            page = 1
        page = int(pg)
        videos = []

        if '年代' in ext.keys():
            NdType = ext['年代']
        else:
            NdType = ''

        if page == '1':
            url = f'{xurl}{cid}-----------.html'

        else:
            url = f'{xurl}{cid}--------{str(page)}---{NdType}.html'

        try:
            detail = requests.get(url=url, headers=headerx)
            detail.encoding = "utf-8"
            res = detail.text
            res = self.extract_middle_text(res, '按评分排序', '<div id="page">', 0)
            doc = BeautifulSoup(res, "lxml")

            for soup in doc:
                vods = soup.find_all('a')

                for vod in vods:

                    name = vod['title']

                    id = vod['href']

                    pics = vod.find('div', class_="module-item-pic")
                    pic = pics.find('img')['data-original']

                    if 'http' not in pic:
                        pic = xurl + pic

                    remark = self.extract_middle_text(str(vod), 'module-item-note">', '</div>', 0)

                    video = {
                        "vod_id": id,
                        "vod_name": '丢丢📽️' + name,
                        "vod_pic": pic,
                        "vod_remarks": '丢丢▶️' + remark
                            }
                    videos.append(video)

        except:
            pass
        result = {'list': videos}
        result['page'] = pg
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def detailContent(self, ids):
        global pm
        did = ids[0]
        result = {}
        videos = []
        playurl = ''
        if 'http' not in did:
            did = xurl + did
        res1 = requests.get(url=did, headers=headerx)
        res1.encoding = "utf-8"
        res = res1.text

        content = '😸丢丢🎉为您介绍剧情📢本资源来源于网络🚓侵权请联系删除👉' + self.extract_middle_text(res,'20px;">','</p>', 0)
        content = content.replace('\u3000', '').replace(' ', '').replace('<p>', '').replace('\n', '')

        xianlu = self.extract_middle_text(res, '<div class="module-tab-items-box hisSwiper"','<div class="shortcuts-mobile-overlay">',2, 'data-dropdown-value=".*?"><span>(.*?)</span>')

        bofang = self.extract_middle_text(res, '<div class="module-play-list-content', '</div>', 3,'href="(.*?)" title=".*?"><span>(.*?)</span>')

        videos.append({
            "vod_id": did,
            "vod_actor": '😸皮皮 😸灰灰',
            "vod_director": '😸丢丢',
            "vod_content": content,
            "vod_play_from": xianlu,
            "vod_play_url": bofang
                     })

        result['list'] = videos
        return result

    def playerContent(self, flag, id, vipFlags):
        parts = id.split("http")
        xiutan = 0
        if xiutan == 0:
            if len(parts) > 1:
                before_https, after_https = parts[0], 'http' + parts[1]
            res = requests.get(url=after_https, headers=headerx)

            url = self.extract_middle_text(res.text, '},"url":"', '"', 0).replace('\\', '')

            result = {}
            result["parse"] = xiutan
            result["playUrl"] = ''
            result["url"] = url
            result["header"] = headerx
            return result


    def searchContentPage(self, key, quick, page):
        result = {}
        videos = []
        if not page:
            page = '1'
        if page == '1':
            url = f'{xurl}/vod/search/-------------.html?wd={key}'

        else:
            url = f'{xurl}/vod/search/{key}----------{str(page)}---.html'

        detail = requests.get(url=url, headers=headerx)
        detail.encoding = "utf-8"
        res = detail.text
        doc = BeautifulSoup(res, "lxml")

        soups = doc.find_all('div', class_="module-card-item")

        for vod in soups:
            names = vod.find('div', class_="module-item-pic")
            name = names.find('img')['alt']

            ids = vod.find('div', class_="module-card-item-title")
            id = ids.find('a')['href']

            pics = vod.find('div', class_="module-item-pic")
            pic = pics.find('img')['data-original']

            if 'http' not in pic:
                pic = xurl + pic

            remark = self.extract_middle_text(str(vod), 'module-item-note">', '</div>', 0)

            video = {
                "vod_id": id,
                "vod_name": '丢丢📽️' + name,
                "vod_pic": pic,
                "vod_remarks": '丢丢▶️' + remark
                    }
            videos.append(video)

        result['list'] = videos
        result['page'] = page
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def searchContent(self, key, quick):
        return self.searchContentPage(key, quick, '1')

    def localProxy(self, params):
        if params['type'] == "m3u8":
            return self.proxyM3u8(params)
        elif params['type'] == "media":
            return self.proxyMedia(params)
        elif params['type'] == "ts":
            return self.proxyTs(params)
        return None


