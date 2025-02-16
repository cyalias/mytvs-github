# coding=utf-8
# !/usr/bin/python
# 嗷呜
import sys

sys.path.append("..")
import re
from base.spider import Spider
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
import json
import time


class Spider(Spider):

    def getName(self):
        return "次元"

    def init(self, extend=""):
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def action(self, action):
        pass

    def destroy(self):
        pass

    host = "http://www.ecydm.top"
    t = str(int(time.time()))

    def header(self):
        header = {
            "User-Agent": "okhttp/3.14.9",
            "app-version-code": "167",
            "app-ui-mode": "light",
            "app-user-device-id": "25f869d32598d3d3089a929453dff0bb7",
            "app-api-verify-time": self.t,
            "app-api-verify-sign": self.aes("encrypt", self.t),
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        return header

    def homeContent(self, filter):
        data = self.fetch(
            "{0}/api.php/getappapi.index/initV119".format(self.host),
            headers=self.header(),
        ).json()
        data1 = self.aes("decrypt", data["data"])
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
        json_data = json.loads(data1)["type_list"]
        self.homedata = json.loads(data1)["banner_list"]
        for item in json_data:
            if item["type_name"] == "全部":
                continue
            has_non_empty_field = False
            jsontype_extend = json.loads(item["type_extend"])
            self.homedata.extend(item["recommend_list"])
            jsontype_extend["sort"] = "最新,最热,最赞,日榜,月榜,周榜"
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
                        value_array = [
                            {"n": value.strip(), "v": value.strip()}
                            for value in values
                            if value.strip() != ""
                        ]
                        filters[str(item["type_id"])].append(
                            {"key": dkey, "name": dy[dkey], "value": value_array}
                        )
        result = {}
        result["class"] = classes
        result["filters"] = filters
        return result

    def homeVideoContent(self):
        result = {"list": self.homedata}
        return result

    def categoryContent(self, tid, pg, filter, extend):
        body = {
            "area": extend.get('area', '全部'),
            "year": extend.get('year', '全部'),
            "type_id": tid,
            "page": pg,
            "sort": extend.get('sort', '最新'),
            "lang": extend.get('lang', '全部'),
            "class": extend.get('class', '全部')
        }
        result = {}
        url = "{0}/api.php/getappapi.index/typeFilterVodList".format(self.host)
        data = self.post(url, headers=self.header(), data=body).json()
        data1 = self.aes("decrypt", data["data"])
        result["list"] = json.loads(data1)["recommend_list"]
        result["page"] = pg
        result["pagecount"] = 9999
        result["limit"] = 90
        result["total"] = 999999
        return result

    def detailContent(self, ids):
        body = f"vod_id={ids[0]}"
        url = "{0}/api.php/getappapi.index/vodDetail".format(self.host)
        data = self.post(url, headers=self.header(), data=body).json()
        data1 = json.loads(self.aes("decrypt", data["data"]))
        vod = data1["vod"]
        play = []
        names = []

        for itt in data1["vod_play_list"]:
            a = []
            names.append(itt["player_info"]["show"])
            parse = itt["player_info"]["parse"]
            for it in itt["urls"]:
                if re.search(r"mp4|m3u8", it["url"]):
                    a.append(f"{it['name']}${it['url']}")
                elif re.search(r"www.yemu.xyz", it["parse_api_url"]):
                    a.append(f"{it['name']}${it['parse_api_url']}")
                else:
                    a.append(
                        f"{it['name']}${'parse_api=' + parse + '&url=' + self.aes('encrypt', it['url']) + '&token=' + it['token']}")
            play.append("#".join(a))
        vod["vod_play_from"] = "$$$".join(names)
        vod["vod_play_url"] = "$$$".join(play)
        result = {"list": [vod]}
        return result

    def searchContent(self, key, quick, pg="1"):
        body = f"keywords={key}&type_id=0&page={pg}"
        url = "{0}/api.php/getappapi.index/searchList".format(self.host)
        data = self.post(url, headers=self.header(), data=body).text
        data1 = json.loads(data)["data"]
        data2 = self.aes("decrypt", data1)
        result = {"list": json.loads(data2)["search_list",'page':pg]}
        return result

    def playerContent(self, flag, id, vipFlags):
        def edu(str):
            def replacer(match):
                from urllib.parse import quote_plus
                return match.group(1) + quote_plus(match.group(2)) + match.group(3)

            return re.sub(r"(url=)(.*?)(&token)", replacer, str)

        url = id
        p = 0
        if "m3u8" not in url and "mp4" not in url:
            try:
                body = edu(url)
                data = self.post("{0}/api.php/getappapi.index/vodParse".format(self.host), headers=self.header(),
                                 data=body).json()
                data1 = json.loads(self.aes("decrypt", data["data"]))["json"]
                url = json.loads(data1)["url"]
            except Exception as e:
                url = id
                p = 1
                if not url.startswith("https://www.yemu.xyz"):
                    url = "https://www.yemu.xyz/?url={0}".format(id)
        result = {}
        headers = self.header().copy()
        del headers["Content-Type"]
        result["parse"] = p
        result["url"] = url
        result["header"] = headers
        return result
    def localProxy(self, param):
        pass
        
    def aes(self, operation, text):
        key = "20c79c979da8db0f".encode("utf-8")
        iv = key
        if operation == "encrypt":
            cipher = AES.new(key, AES.MODE_CBC, iv)
            ct_bytes = cipher.encrypt(pad(text.encode("utf-8"), AES.block_size))
            ct = b64encode(ct_bytes).decode("utf-8")
            return ct
        elif operation == "decrypt":
            cipher = AES.new(key, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(b64decode(text)), AES.block_size)
            return pt.decode("utf-8")
