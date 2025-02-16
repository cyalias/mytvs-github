"""

作者 凯悦宾馆 🚓 内容均从互联网收集而来 仅供交流学习使用 版权归原创者所有 如侵犯了您的权益 请通知作者 将及时删除侵权内容
                    ====================kaiyuebinguan====================

"""

from Crypto.Util.Padding import unpad
from urllib.parse import unquote
from Crypto.Cipher import ARC4
from base.spider import Spider
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import binascii
import requests
import base64
import json
import time
import sys
import re
import os

sys.path.append('..')

xurl = "http://img.shifen.me"

headerx = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'
          }

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
        result = {"class": [{"type_id": "5", "type_name": "电影🌠"},
                            {"type_id": "14", "type_name": "剧集🌠"},
                            {"type_id": "19", "type_name": "动漫🌠"},
                            {"type_id": "23", "type_name": "综艺🌠"}]
                 }
        return result

    def homeVideoContent(self):
        videos = []

        try:
            xurl1 = "http://42.194.235.17:20000/api/bt/list?genere_id&order&lang&keywords&code=unknownec1280db12795506&category_id=1&limit=24&channel=wandoujia&page=1&sort=update"
            detail = requests.get(url=xurl1, headers=headerx)
            detail.encoding = "utf-8"
            if detail.status_code == 200:
                data = detail.json()

                for vod in data['data']:

                    name = vod['title']

                    id = vod['id']
                    id = f"http://42.194.235.17:20000/api/node/detail?channel=wandoujia&id={vod['id']}"

                    pic = vod['images']['poster']

                    remark = vod['torrents']['zh'][0]['title']

                    video = {
                        "vod_id": id,
                        "vod_name":  name,
                        "vod_pic": pic,
                        "vod_remarks": remark
                            }
                    videos.append(video)

            result = {'list': videos}
            return result
        except:
            pass

    def categoryContent(self, cid, pg, filter, ext):
        result = {}
        videos = []

        if pg:
            page = int(pg)
        else:
            page = 1

        if page == '1':
            url = f'http://42.194.235.17:20000/api/bt/list?genere_id&order&lang&keywords&code=unknownec1280db12795506&category_id={cid}&limit=24&channel=wandoujia&page={str(page)}&sort=update'

        else:
            url = f'http://42.194.235.17:20000/api/bt/list?genere_id&order&lang&keywords&code=unknownec1280db12795506&category_id={cid}&limit=24&channel=wandoujia&page={str(page)}&sort=update'

        try:
            detail = requests.get(url=url, headers=headerx)
            detail.encoding = "utf-8"
            if detail.status_code == 200:
                data = detail.json()

                for vod in data['data']:

                    name = vod['title']

                    id = vod['id']

                    id = f"http://42.194.235.17:20000/api/node/detail?channel=wandoujia&id={id}"

                    pic = vod['images']['poster']

                    remark = vod['torrents']['zh'][0]['title']

                    video = {
                        "vod_id": id,
                        "vod_name":  name,
                        "vod_pic": pic,
                        "vod_remarks": remark
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
        purl = ''

        detail = requests.get(url=did, headers=headerx)
        detail.encoding = "utf-8"
        if detail.status_code == 200:
            data = detail.json()

            content = data['data']['description']
            content = content.replace('\u3000', '').replace(' ', '').replace('\r', '').replace('\n', '')

            for vod in data['data']['btbo_downlist']:

                name = vod['title']

                url1 = vod['url']

                purl = purl + name + '$' + url1 + '#'

            purl = purl[:-1]

        videos.append({
            "vod_id": did,
            "vod_actor": '😸皮皮 😸灰灰',
            "vod_director": '😸丢丢',
            "vod_content": content,
            "vod_play_from": '丢丢专线',
            "vod_play_url": purl
                     })

        result['list'] = videos
        return result

    def playerContent(self, flag, id, vipFlags):

        result = {}
        result["parse"] = 0
        result["playUrl"] = ''
        result["url"] = id
        result["header"] = headerx
        return result

    def searchContentPage(self, key, quick, page):
        result = {}
        videos = []

        if not page:
            page = '1'
        if page == '1':
            url = f'http://42.194.235.17:20000/api/video/search?page={str(page)}&key={key}'

        else:
            url = f'http://42.194.235.17:20000/api/video/search?page={str(page)}&key={key}'

        detail = requests.get(url=url, headers=headerx)
        detail.encoding = "utf-8"
        if detail.status_code == 200:
            data = detail.json()

            for vod in data['data']:

                name = vod['title']

                id = vod['id']
                id = f"http://42.194.235.17:20000/api/node/detail?channel=wandoujia&id={vod['id']}"

                pic = vod['thumbnail']

                remark = vod['mask']

                video = {
                    "vod_id": id,
                    "vod_name": name,
                    "vod_pic": pic,
                    "vod_remarks": remark
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


"""

   =======================================

   换行 \n   零个或者多个空格 \s+   数字型 int   文本型 str   分页{} '年代':'2021'       

   性能要求高"lxml"   处理不规范的HTML"html5lib"   简单应用"html.parser"   解析XML"xml"

   =======================================

   /rss/index.xml?wd=爱情&page=1                                搜索有验证

   /index.php/ajax/suggest?mid=1&wd=爱情&page=1&limit=30        搜索有验证

   /index.php/ajax/data?mid=1&tid={cateId}&class={class}&area={area}&page={catePg}&limit=30   分类有验证

   /index.php/vod/type/class/{cid}/id/41/page/{str(page)}/year/{NdType}.html        隐藏分类

   /{cateId}-{area}-{by}-{class}-{lang}-{letter}---{catePg}---{year}.html

   短剧 穿越 古装 仙侠 女频 恋爱 反转 现代 都市 剧情 玄幻 脑洞 悬疑  

   =======================================

   aaa = self.extract_middle_text(res, 'bbb', 'ccc', 0)
   aaa = aaa.replace('aaa', '').replace('bbb', '') 替换多余
   取头 取尾  （不循环)   截取项  （不循环)   长用于直链  二次截取                0号子程序

   aaa =self.extract_middle_text(res, 'bbb', 'ccc',1,'html">(.*?)<')
   aaa = aaa.replace('aaa', '').replace('bbb', '') 替换多余
   取头 取尾  （不循环)   截取项  （循环)     长用于详情  和2号区别没有$$$        1号子程序

   aaa = self.extract_middle_text(res, 'bbb','ccc', 2,'<span class=".*?" id=".*?">(.*?)</span>')
   aaa = aaa.replace('aaa', '').replace('bbb', '') 替换多余
   取头 取尾  （不循环)   截取项  （循环)     只能用于线路数组  里面包含$$$       2号子程序

   aaa = self.extract_middle_text(res, 'bbb', 'ccc', 3,'href="(.*?)" class=".*?">(.*?)</a>')
   aaa = aaa.replace('aaa', '').replace('bbb', '') 替换多余
   取头 取尾  （循环)     截取项  （循环)    长用于播放数组                     3号子程序

   =======================================

"""

if __name__ == '__main__':
    spider_instance = Spider()

    # res=spider_instance.homeContent('filter')  #  分类🚨

    # res = spider_instance.homeVideoContent()  # 首页🚨

    # res=spider_instance.categoryContent('5', 1, 'filter', {})  #  分页🚨

    res = spider_instance.detailContent(['http://42.194.235.17:20000/api/node/detail?channel=wandoujia&id=559366'])  #  详情页🚨

    # res = spider_instance.playerContent('1', 'http://42.194.235.17:20000/api/nUser/commentList?url_id=176366&page=1&token=', 'vipFlags')  #  播放页🚨

    # res = spider_instance.searchContentPage('爱情', 'quick', '1')  # 搜索页🚨

    print(res)



