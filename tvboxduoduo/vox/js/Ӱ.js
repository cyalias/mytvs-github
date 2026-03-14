var rule = {

safeParseJSON: function(jStr){
    try {return JSON.parse(jStr);} catch(e) {return null;}
},
    
getkvods: function (url, panSet = '0') {
    let kvods = [];
    let panType = rule.safeParseJSON(fetch(url))?.data?.merged_by_type ?? {}; 
    Object.entries(panType).forEach(([k,v]) => {
        let kpic = rule.panPics[k] || '图片';
        v.forEach(it => {
            let kname = it.note || '名称';
            let kremarks = `${k}|${it.datetime}`;
            kvods.push({
                vod_name: kname,
                vod_pic: kpic,
                vod_remarks: kremarks,
                vod_id: `${it.url}@${kname}@${kpic}@${kremarks}`
            });
        });
    });
    if (panSet = '1') {
        kvods = kvods.filter(it => rule.keepPan.includes(it.vod_remarks.split('|')[0])); 
    }
    return kvods;
},

author: '小可乐/v5.12.1',
title: '影子网盘',
类型: '影视',
host: 'https://tv.yingzi.ee',
headers: {'User-Agent': MOBILE_UA},
编码: 'utf-8',
timeout: 5000,

homeUrl: '/api/drive/search?kw=美剧',
url: '/api/drive/search?kw=fyclass',
searchUrl: '/api/drive/search?kw=**',

limit: 9,
double: false,
class_name: '短剧&TVB&Netflix',
class_url: '短剧&TVB&Netflix',

panSet: '1',
keepPan: ['aliyun', 'quark',  'baidu',  'uc',  'xunlei'],
panPics: {
    "aliyun": "https://so.slowread.net/static/img/ali.jpg",
    "quark": "https://so.slowread.net/static/img/quark.jpg",
    "baidu": "https://so.slowread.net/static/img/baidu.jpg",
    "uc": "https://so.slowread.net/static/img/uc.jpg",
    "xunlei": "https://so.slowread.net/static/img/xunlei.jpg"
},

推荐: '*',
一级: $js.toString(() => {
    VODS = rule.getkvods(input, rule.panSet);
}),
搜索: '*',
二级: $js.toString(() => {
    let [kid, kname, kpic, kremarks] = input.split('@');
    let [type, remark='状态'] = kremarks.split('|');
    let kurl = `合集$${kid}@${type}`;
    VOD = {
        vod_id: kid,
        vod_name: kname,
        vod_pic: kpic,
        type_name: type,
        vod_remarks: remark,
        vod_year: '1000',
        vod_area: '地区',
        vod_lang: '语言',
        vod_director: '导演',
        vod_actor: '演员',
        vod_content: `${kname}_${kid}`,
        vod_play_from: type,
        vod_play_url: kurl
    };
}),

pagecount: {"短剧": 1}, 

play_parse: true,
lazy: $js.toString(() => {
    let [kurl, flag] = input.split('@');
    kurl = (flag !== 'magnet') ? `push://${kurl}` : kurl;
    input = { jx: 0, parse: 0, url: kurl };
}),
}