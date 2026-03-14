var rule = {
author: '小可乐/v5.12.1',
title: '爱看机器人',
类型: '影视',
host: 'https://v.aikanbot.com',
headers: {'User-Agent': MOBILE_UA},
编码: 'utf-8',
timeout: 5000,
图片替换: 'http=>https://imgp.aikanbot.com/proxy?url=http',
homeUrl: '/',
url: '/hot/index-fyclass-fyfilter-p-fypage.html[/hot/index-fyclass-fyfilter.html]',
filter_url: '{{fl.class or "热门"}}',
searchUrl: '/search?q=**&p=fypage[/search?q=**]',
detailUrl: '',

limit: 9,
double: false,
class_name: '电影&剧集&榜单',
class_url: 'movie&tv&billboard',
pagecount: {"billboard": 1}, 

推荐: '*',
一级: $js.toString(() => {
    if (/billboard/.test(input)) {input = `${HOST}/billboard.html`;}
    let klists = pdfa(fetch(input), 'a:has([alt])');
    VODS = [];
    klists.forEach((it) => {
        VODS.push({
            vod_name: pdfh(it, 'img&&alt') || '名称',
            vod_pic: pdfh(it, 'img&&data-src') || '图片',
            vod_remarks: '无状态',
            vod_id: pdfh(it, 'a&&href') || 'Id',
        });
    });
}),
搜索: '.media;.title-text&&Text;img&&data-src;.label&&Text;a&&href',
二级: $js.toString(() => {
    let khtml = fetch(input);
    const getToken = html => {
        let [currentId, eToken] = [pdfh(html, '#current_id&&value') || '', pdfh(html, '#e_token&&value') || ''];
        if (!currentId || !eToken || !/^\d+$/.test(currentId)) {return '';}
        let remainEToken = eToken;
        let finalToken = currentId.slice(-4).split('').map(it => {
            let startPos = (parseInt(it, 10) % 3) + 1;
            let endPos = startPos + 8;
            if (startPos >= remainEToken.length) {return '';}
            let segment = remainEToken.substring(startPos, endPos);
            remainEToken = remainEToken.substring(endPos);
            return segment;
        }).filter(Boolean).join('');
        return finalToken;
    };
    const tabName = {"dyttm3u8":"天堂","360zy":"360","iqym3u8":"爱奇艺","mtm3u8":"茅台","subm3u8":"速播","nnm3u8":"牛牛","okm3u8":"欧克","tym3u8":"TY","yym3u8":"歪歪","bfzym3u8":"暴风","1080zyk":"优质","kuaikan":"快看","lzm3u8":"量子","ffm3u8":"非凡","snm3u8":"索尼","qhm3u8":"奇虎","hym3u8":"虎牙","haiwaikan":"海外看","gsm3u8":"光速","zuidam3u8":"最大","bjm3u8":"八戒","wolong":"卧龙","xlm3u8":"新浪","yhm3u8":"樱花","tkm3u8":"天空","jsm3u8":"极速","wjm3u8":"无尽","sdm3u8":"闪电","kcm3u8":"快车","jinyingm3u8":"金鹰","fsm3u8":"飞速","tpm3u8":"淘片","lem3u8":"鱼乐","dbm3u8":"百度","tomm3u8":"番茄","ukm3u8":"优酷","ikm3u8":"爱坤","hnzym3u8":"红牛资源","hnm3u8":"红牛","68zy_m3u8":"六八","kdm3u8":"酷点","bdxm3u8":"北斗星","hhm3u8":"豪华","kbm3u8":"快播","mzm3u8":"MZ"};
    let kid = pdfh(khtml, '#current_id&&value');
    let token = getToken(khtml);
    let deUrl = `${HOST}/api/getResN?videoId=${kid}&mtype=2&token=${token}`;
    let resList = rule.safeParseJSON(fetch(deUrl))?.data?.list ?? [];
    let [ktabs, kurls] = [[], []];
    resList.forEach(it => {
        let resData = rule.safeParseJSON(it.resData.replace(/#{2,}/g, '#'))?.[0] ?? {};
        let tab = resData?.flag ?? '线路';
        ktabs.push(tabName[tab] || tab);
        kurls.push(resData?.url || '');
    });
    ktabs = rule.dealSameEle(ktabs);
    VOD = {
        vod_id: kid,
        vod_name: pdfh(khtml, 'h2&&Text') || '名称',
        vod_pic: pdfh(khtml, '.item-root&&img&&data-src') || '图片',
        type_name: '类型',
        vod_remarks: '状态',
        vod_year: pdfh(khtml, '.meta:eq(-3)&&Text') || '1000',
        vod_area: pdfh(khtml, '.meta:eq(-2)&&Text') || '地区',
        vod_lang: '语言',
        vod_director: '导演',
        vod_actor: pdfh(khtml, '.meta:eq(-1)&&Text') || '演员',
        vod_content: pdfh(khtml, 'meta[name*=description]&&content') || '简介',
        vod_play_from: ktabs.join('$$$'),
        vod_play_url: kurls.join('$$$')
    };
}),

tab_order: ['天堂', '360'],
play_parse: true,
lazy: $js.toString(() => {
    input = { jx: 0, parse: 0, url: input, header: rule.headers };
}),

safeParseJSON: function(jStr) {
    try {
        return JSON.parse(jStr);
    } catch (e) {
        return null;
    }
},

dealSameEle: function(arr) {
    try {
        if (!Array.isArray(arr)) {throw new Error('输入参数非数组');}
        const countMap = new Map();
        let newArr = arr.map(item => {
            let count = countMap.get(item) || 0;
            let currentCount = count + 1;
            countMap.set(item, currentCount);
            return currentCount > 1 ? `${item}${currentCount}` : item;
        });
        return newArr;
    } catch (e) {
        return [];
    }
},

filter: {
    "movie": [
        {"key": "class","name": "剧情","value": [{"n": "热门","v": "热门"}, {"n": "最新","v": "最新"}, {"n": "经典","v": "经典"}, {"n": "豆瓣高分","v": "豆瓣高分"}, {"n": "冷门佳片","v": "冷门佳片"}, {"n": "华语","v": "华语"}, {"n": "欧美","v": "欧美"}, {"n": "韩国","v": "韩国"}, {"n": "日本","v": "日本"}, {"n": "动作","v": "动作"}, {"n": "喜剧","v": "喜剧"}, {"n": "爱情","v": "爱情"}, {"n": "科幻","v": "科幻"}, {"n": "悬疑","v": "悬疑"}, {"n": "恐怖","v": "恐怖"}, {"n": "成长","v": "成长"}, {"n": "豆瓣top250","v": "豆瓣top250"}]}
    ],
    "tv": [
        {"key": "class","name": "剧情","value": [{"n": "热门","v": "热门"}, {"n": "美剧","v": "美剧"}, {"n": "英剧","v": "英剧"}, {"n": "韩剧","v": "韩剧"}, {"n": "日剧","v": "日剧"}, {"n": "国产剧","v": "国产剧"}, {"n": "港剧","v": "港剧"}, {"n": "日本动画","v": "日本动画"}, {"n": "综艺","v": "综艺"}, {"n": "纪录片","v": "纪录片"}]}
    ]
}
}