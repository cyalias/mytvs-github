# coding=utf-8
# !/usr/bin/python
# 嗷呜
import re
import sys
import random
from urllib.parse import quote
import requests
from Crypto.Hash import MD5
sys.path.append("..")
from base.spider import Spider
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode
import json


class Spider(Spider):
        
    def getName(self):
        return "mq"

    def init(self, extend=""):
        self.demo = self.key()
        self.host = self.demo['host']
        self.playlist = None
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def action(self, action):
        pass

    def destroy(self):
        pass

    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 '
                      'MUOUAPP/10.8.4506.400',
        'brand-model': 'M2012K10C',
        'sys-version': '11',
        'device': '6132ea9af18fc022',
        'os': 'Android',
        'app-version': '4.1.6',
    }

    def homeContent(self, filter):
        data = self.fetch(
            "{0}/api.php/v1.vod/types".format(self.host),
            headers=self.header,
        ).text
        data1 = self.aes(data)
        dy = {
            "class": "类型",
            "area": "地区",
            "lang": "语言",
            "year": "年份",
            "letter": "字母",
            "by": "排序",
            "sort": "排序",
        }
        filters = {}
        classes = []
        json_data = data1['data']['typelist']
        for item in json_data:
            if item["type_name"] == "全部":
                continue
            has_non_empty_field = False
            jsontype_extend = item["type_extend"]
            jsontype_extend['by'] = '按更新,按播放,按评分'
            classes.append({"type_name": item["type_name"], "type_id": item["type_id"]})
            for key in dy:
                if key in jsontype_extend and jsontype_extend[key].strip() != "":
                    has_non_empty_field = True
                    break
            if has_non_empty_field:
                filters[str(item["type_id"])] = []
                for dkey in jsontype_extend:
                    if dkey in dy and jsontype_extend[dkey].strip() != "":
                        values = jsontype_extend[dkey].split(",")
                        sl = {'按更新': 'time', '按播放': 'hits', '按评分': 'score'}
                        value_array = [
                            {"n": value.strip(), "v": sl[value.strip()] if dkey == "by" else value.strip()}
                            for value in values
                            if value.strip() != ""
                        ]
                        filters[str(item["type_id"])].append(
                            {"key": dkey, "name": dy[dkey], "value": value_array}
                        )
        result = {"class": classes, "filters": filters}
        return result

    def homeVideoContent(self):
        data = self.fetch(
            "{0}/api.php/v1.vod/HomeIndex?page=&limit=6".format(self.host),
            headers=self.header,
        ).text
        vods = []
        data1 = self.aes(data)["data"]
        for items in data1:
            if len(items["vod_list"]) > 0:
                vods.extend(items["vod_list"])
        result = {"list": vods}
        return result

    def categoryContent(self, tid, pg, filter, extend):
        def encode_chinese_chars(s):
            chinese_chars_pattern = r'[\u4e00-\u9fff]+'

            def encode_match(match):
                return quote(match.group(0))

            return re.sub(chinese_chars_pattern, encode_match, s)

        result = {}
        url = f"{self.host}/api.php/v1.vod?type={tid}&class={extend.get('class', '')}&area={extend.get('area', '')}&year={extend.get('year', '')}&by={extend.get('by', '')}&page={pg}&limit=18"
        data = self.fetch(encode_chinese_chars(url), headers=self.header).text
        data1 = self.aes(data)["data"]["list"]
        vods = []
        for item in data1:
            vods.append({
                'vod_id': item['vod_id'],
                'vod_name': item['vod_name'],
                'vod_pic': item['vod_pic'],
                'vod_year': item['vod_year'],
                'vod_remarks': item['vod_remarks'],
            })
        result["list"] = vods
        result["page"] = pg
        result["pagecount"] = 9999
        result["limit"] = 90
        result["total"] = 999999
        return result

    def detailContent(self, ids):
        url = "{0}/api.php/v1.vod/detail?vod_id={1}".format(self.host, ids[0])
        data = self.fetch(url, headers=self.header).text
        vods = self.aes(data)
        vod = vods['data']
        self.playlist = vod['vod_play_url']
        if vod['type']:
            del vod['type']
        if vod['vod_play_list']:
            del vod['vod_play_list']
        if vod['vod_down_list']:
            del vod['vod_down_list']
        result = {"list": [vod]}
        return result

    def searchContent(self, key, quick, pg=1):
        url = "{0}/api.php/v1.vod?wd={1}&limit=18&page={2}".format(self.host, quote(key), pg)
        data = self.fetch(url, headers=self.header).text
        data1 = self.aes(data)["data"]['list']
        vods = []
        for item in data1:
            vods.append({
                'vod_id': item['vod_id'],
                'vod_name': item['vod_name'],
                'vod_pic': item['vod_pic'],
                'vod_year': item['vod_year'],
                'vod_remarks': item['vod_remarks'],
            })
        result = {"list": vods, "page": pg}
        return result

    def playerContent(self, flag, id, vipFlags):
        url = id
        dmurl = self.dmurl(id)
        if dmurl:
            dmurl = self.getProxyUrl() + '&dmurl={0}'.format(dmurl)
        p = 0
        if "m3u8" not in url and "mp4" not in url:
            try:
                data = requests.get(self.demo['jx'] + url, headers=self.header, timeout=10).json()
                url = data["url"]
            except Exception as e:
                p = 1
        result = {"parse": p, "url": url, 'danmaku': dmurl, "header": self.header}
        return result

    def localProxy(self, param):
        url = param.get('dmurl')
        data = self.fetch(self.demo['dm'] + url, headers=self.header, timeout=10).text
        if data:
            return self.xml(json.loads(data))
        return ''
        
    def key(self):
        hostt = self.fetch('https://muouapp.oss-cn-hangzhou.aliyuncs.com/MUOUAPP/35174627.txt',
                           headers=self.header).text.strip()
        data = self.fetch('{0}/peizhi.php'.format(hostt), headers=self.header).text.strip()[8:-1]
        bsdata = json.loads(b64decode(data).decode('utf-8'))
        host = bsdata['HBqq']
        jx = bsdata['HBrjjg']
        dm = bsdata['dmkuurl']
        key = MD5.new(bsdata['key'].encode('utf-8')).hexdigest()[:16]
        return {'key': key, 'host': host, 'jx': jx, 'dm': dm}
        
    def xml(self, htt):
        html2 = htt['danmuku']
        lists = [item for item in html2]
        suoj = '\t'
        danmustr = f'<?xml version="1.0" encoding="UTF-8"?>\n<i>\n{suoj}<chatserver>chat.xtdm.com</chatserver>\n{suoj}<chatid>88888888</chatid>\n{suoj}<mission>0</mission>\n{suoj}<maxlimit>99999</maxlimit>\n{suoj}<state>0</state>\n{suoj}<real_name>0</real_name>\n{suoj}<source>k-v</source>\n'
        for i in range(len(lists)):
            dm0 = lists[i][0]
            dm2 = self.gcolor()
            dm4 = lists[i][4]
            if '<' in dm4 or '>' in dm4 or '&' in dm4 or '\u0000' in dm4 or '\b' in dm4:
                continue
            tempdata = f'{suoj}<d p="{dm0},1,25,{dm2},0">{dm4}</d>\n'
            danmustr += tempdata
        danmustr += '</i>'
        return [200, "text/xml", danmustr]

    def dmurl(self, s):
        if '.html' in s:
            return s
        parts = self.playlist.split('$$$')
        html_part = next((p for p in parts if '.html' in p), None)
        if html_part:
            position = html_part.split('#')
            for item in parts:
                if s in item:
                    target_index = next((i for i, sub in enumerate(item.split('#')) if s in sub), None)
                    if target_index:
                        return position[target_index].split('$')[1]
        return ''
        
    def gcolor(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color_decimal = (r << 16) + (g << 8) + b
        return color_decimal
        
    def aes(self, text):
        key = self.demo['key'].encode('utf-8')
        cipher = AES.new(key, AES.MODE_CBC, key)
        ciphertext = b64decode(text)
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')
        replacement = '{"code":"'
        index = decrypted.rfind('success')
        if index != -1:
            decrypted = replacement + decrypted[index:]
        return json.loads(decrypted)
