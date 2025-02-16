# -*- coding: utf-8 -*-
# @Author  : Doubebly
# @Time    : 2024/7/19 22:20
# @Function:

import sys
import requests
import json
import base64
from lxml import etree
import re

sys.path.append('..')
from base.spider import Spider


class Spider(Spider):
    def getName(self):
        return "DM84"

    def init(self, extend):
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def homeContent(self, filter):
        return {
            'class': [{'type_id': '1', 'type_name': '国产动漫'},
                      {'type_id': '2', 'type_name': '日本动漫'},
                      {'type_id': '3', 'type_name': '欧美动漫'},
                      {'type_id': '4', 'type_name': '电影'}],
            'filters': {
                '1': [{'key': 'type',
                       'name': '类型',
                       'value': [{'n': '全部', 'v': ''},
                                 {'n': '奇幻', 'v': '奇幻'},
                                 {'n': '战斗', 'v': '战斗'},
                                 {'n': '玄幻', 'v': '玄幻'},
                                 {'n': '穿越', 'v': '穿越'},
                                 {'n': '科幻', 'v': '科幻'},
                                 {'n': '武侠', 'v': '武侠'},
                                 {'n': '热血', 'v': '热血'},
                                 {'n': '耽美', 'v': '耽美'},
                                 {'n': '搞笑', 'v': '搞笑'},
                                 {'n': '动态漫画', 'v': '动态漫画'}]},
                      {'key': 'year',
                       'name': '时间',
                       'value': [{'n': '全部', 'v': ''},
                                 {'n': '2024', 'v': '2024'},
                                 {'n': '2023', 'v': '2023'},
                                 {'n': '2022', 'v': '2022'},
                                 {'n': '2021', 'v': '2021'},
                                 {'n': '2020', 'v': '2020'},
                                 {'n': '2019', 'v': '2019'},
                                 {'n': '2018', 'v': '2018'},
                                 {'n': '2017', 'v': '2017'},
                                 {'n': '2016', 'v': '2016'},
                                 {'n': '2015', 'v': '2015'}]},
                      {'key': 'by',
                       'name': '排序',
                       'value': [{'n': '按时间', 'v': 'time'},
                                 {'n': '按人气', 'v': 'hits'},
                                 {'n': '按评分', 'v': 'score'}]}],
                '2': [{'key': 'type',
                       'name': '类型',
                       'value': [{'n': '全部', 'v': ''},
                                 {'n': '冒险', 'v': '冒险'},
                                 {'n': '奇幻', 'v': '奇幻'},
                                 {'n': '战斗', 'v': '战斗'},
                                 {'n': '后宫', 'v': '后宫'},
                                 {'n': '热血', 'v': '热血'},
                                 {'n': '励志', 'v': '励志'},
                                 {'n': '搞笑', 'v': '搞笑'},
                                 {'n': '校园', 'v': '校园'},
                                 {'n': '机战', 'v': '机战'},
                                 {'n': '悬疑', 'v': '悬疑'},
                                 {'n': '治愈', 'v': '治愈'},
                                 {'n': '百合', 'v': '百合'},
                                 {'n': '恐怖', 'v': '恐怖'},
                                 {'n': '泡面番', 'v': '泡面番'},
                                 {'n': '恋爱', 'v': '恋爱'},
                                 {'n': '推理', 'v': '推理'}]},
                      {'key': 'year',
                       'name': '时间',
                       'value': [{'n': '全部', 'v': ''},
                                 {'n': '2024', 'v': '2024'},
                                 {'n': '2023', 'v': '2023'},
                                 {'n': '2022', 'v': '2022'},
                                 {'n': '2021', 'v': '2021'},
                                 {'n': '2020', 'v': '2020'},
                                 {'n': '2019', 'v': '2019'},
                                 {'n': '2018', 'v': '2018'},
                                 {'n': '2017', 'v': '2017'},
                                 {'n': '2016', 'v': '2016'},
                                 {'n': '2015', 'v': '2015'}]},
                      {'key': 'by',
                       'name': '排序',
                       'value': [{'n': '按时间', 'v': 'time'},
                                 {'n': '按人气', 'v': 'hits'},
                                 {'n': '按评分', 'v': 'score'}]}],
                '3': [{'key': 'type',
                       'name': '类型',
                       'value': [{'n': '全部', 'v': ''},
                                 {'n': '科幻', 'v': '科幻'},
                                 {'n': '冒险', 'v': '冒险'},
                                 {'n': '战斗', 'v': '战斗'},
                                 {'n': '百合', 'v': '百合'},
                                 {'n': '奇幻', 'v': '奇幻'},
                                 {'n': '热血', 'v': '热血'},
                                 {'n': '搞笑', 'v': '搞笑'}]},
                      {'key': 'year',
                       'name': '时间',
                       'value': [{'n': '全部', 'v': ''},
                                 {'n': '2024', 'v': '2024'},
                                 {'n': '2023', 'v': '2023'},
                                 {'n': '2022', 'v': '2022'},
                                 {'n': '2021', 'v': '2021'},
                                 {'n': '2020', 'v': '2020'},
                                 {'n': '2019', 'v': '2019'},
                                 {'n': '2018', 'v': '2018'},
                                 {'n': '2017', 'v': '2017'},
                                 {'n': '2016', 'v': '2016'},
                                 {'n': '2015', 'v': '2015'}]},
                      {'key': 'by',
                       'name': '排序',
                       'value': [{'n': '按时间', 'v': 'time'},
                                 {'n': '按人气', 'v': 'hits'},
                                 {'n': '按评分', 'v': 'score'}]}],
                '4': [{'key': 'type',
                       'name': '类型',
                       'value': [{'n': '全部', 'v': ''},
                                 {'n': '搞笑', 'v': '搞笑'},
                                 {'n': '奇幻', 'v': '奇幻'},
                                 {'n': '治愈', 'v': '治愈'},
                                 {'n': '科幻', 'v': '科幻'},
                                 {'n': '喜剧', 'v': '喜剧'},
                                 {'n': '冒险', 'v': '冒险'},
                                 {'n': '动作', 'v': '动作'},
                                 {'n': '爱情', 'v': '爱情'}]},
                      {'key': 'year',
                       'name': '时间',
                       'value': [{'n': '全部', 'v': ''},
                                 {'n': '2024', 'v': '2024'},
                                 {'n': '2023', 'v': '2023'},
                                 {'n': '2022', 'v': '2022'},
                                 {'n': '2021', 'v': '2021'},
                                 {'n': '2020', 'v': '2020'},
                                 {'n': '2019', 'v': '2019'},
                                 {'n': '2018', 'v': '2018'},
                                 {'n': '2017', 'v': '2017'},
                                 {'n': '2016', 'v': '2016'},
                                 {'n': '2015', 'v': '2015'}]},
                      {'key': 'by',
                       'name': '排序',
                       'value': [{'n': '按时间', 'v': 'time'},
                                 {'n': '按人气', 'v': 'hits'},
                                 {'n': '按评分', 'v': 'score'}]}]
            }
        }

    def homeVideoContent(self):
        video_list = []
        try:
            res = requests.get('https://dm84.org')
            root = etree.HTML(res.text)
            data_list = root.xpath('//li/div[@class="item"]')
            print(len(data_list))
            for i in data_list:
                video_list.append(
                    {
                        'vod_id': i.xpath('./a[2]/@href')[0].split('/')[-1].split('.')[0],
                        'vod_name': i.xpath('./a[2]/@title')[0],
                        'vod_pic': i.xpath('./a[1]/@data-bg')[0],
                        'vod_remarks': i.xpath('./span/text()')[0]
                    }
                )


        except requests.RequestException as e:
            return {'list': [], 'msg': e}
        return {'list': video_list}

    def categoryContent(self, cid, page, filter, ext):
        _by = ''
        _type = ''
        _year = ''
        if ext.get('by'):
            _by = ext.get('by')
        if ext.get('type'):
            _type = ext.get('type')
        if ext.get('year'):
            _type = ext.get('year')
        video_list = []
        try:
            res = requests.get(f'https://dm84.org/show-{cid}--{_by}-{_type}--{_year}-{page}.html')
            root = etree.HTML(res.text)
            data_list = root.xpath('//li/div[@class="item"]')
            print(len(data_list))
            for i in data_list:
                video_list.append(
                    {
                        'vod_id': i.xpath('./a[2]/@href')[0].split('/')[-1].split('.')[0],
                        'vod_name': i.xpath('./a[2]/@title')[0],
                        'vod_pic': i.xpath('./a[1]/@data-bg')[0],
                        'vod_remarks': i.xpath('./span/text()')[0]
                    }
                )


        except requests.RequestException as e:
            return {'list': [], 'msg': e}

        return {'list': video_list}

    def detailContent(self, did):
        video_list = []
        try:
            res = requests.get(f'https://dm84.org/v/{did[0]}.html')
            root = etree.HTML(res.text)
            vod_play_from = '$$$'.join(root.xpath('//ul[contains(@class, "play_from")]/li/text()'))
            play_list = root.xpath('//ul[contains(@class, "play_list")]')
            vod_play_url = []
            for i in play_list:
                name_list = i.xpath('./li/a/text()')
                url_list = i.xpath('./li/a/@href')
                vod_play_url.append(
                    '#'.join([_name + '$' + _url for _name, _url in zip(name_list, url_list)])
                )
            video_list.append(
                {
                    'type_name': '',
                    'vod_id': did[0],
                    'vod_name': '',
                    'vod_remarks': '',
                    'vod_year': '',
                    'vod_area': '',
                    'vod_actor': '',
                    'vod_director': '沐辰_为爱发电',
                    'vod_content': '',
                    'vod_play_from': vod_play_from,
                    'vod_play_url': '$$$'.join(vod_play_url)

                }
            )


        except requests.RequestException as e:
            return {'list': [], 'msg': e}
        return {"list": video_list}

    def searchContent(self, key, quick):
        return self.searchContentPage(key, quick, '1')

    def searchContentPage(self, keywords, quick, page):
        video_list = []
        try:
            res = requests.get(f'https://dm84.org/s----------.html?wd={keywords}')
            root = etree.HTML(res.text)
            data_list = root.xpath('//li/div[@class="item"]')
            for i in data_list:
                video_list.append(
                    {
                        'vod_id': i.xpath('./a[2]/@href')[0].split('/')[-1].split('.')[0],
                        'vod_name': i.xpath('./a[2]/@title')[0],
                        'vod_pic': i.xpath('./a[1]/@data-bg')[0],
                        'vod_remarks': i.xpath('./span/text()')[0]
                    }
                )


        except requests.RequestException as e:
            return {'list': [], 'msg': e}
        return {'list': video_list}

    def playerContent(self, flag, pid, vipFlags):
        play_url = 'https://gitee.com/dobebly/my_img/raw/c1977fa6134aefb8e5a34dabd731a4d186c84a4d/x.mp4'
        try:
            res = requests.get(f'https://dm84.org{pid}')
            a_url = re.findall('iframe src="(.*?)"', res.text)[0]
            res1 = requests.get(a_url)
            url = re.findall('var url = "(.*?)"', res1.text)[0]
            t = re.findall('var t = "(.*?)"', res1.text)[0]
            key = re.findall('var key = "(.*?)"', res1.text)[0]
            act = re.findall('var act = "(.*?)"', res1.text)[0]
            play = re.findall('var play = "(.*?)"', res1.text)[0]
            data = {
                'url': url,
                't': t,
                'key': key,
                'act': act,
                'play': play
            }
            headers = {
                'authority': 'hhjx.hhplayer.com',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://hhjx.hhplayer.com',
                'referer': a_url,
                'user-agent': 'okhttp/3.12.0',
                'x-requested-with': 'XMLHttpRequest',
            }
            res2 = requests.post('https://hhjx.hhplayer.com/api.php', data=data, headers=headers)
            if res2.json()['code'] == 200:
                play_url = res2.json()['url']

        except requests.RequestException as e:
            return {'url': play_url, 'msg': e, 'parse': 0, 'jx': 0, 'header': self.header}

        return {"url": play_url, "header": self.header, "parse": 0, "jx": 0}

    def localProxy(self, params):
        pass

    header = {"User-Agent": "okhttp/3.12.0"}


if __name__ == '__main__':
    pass
