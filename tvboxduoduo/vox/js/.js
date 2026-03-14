/**
    title: "灯泡网盘菠菜",
    author: "",
    logo: "https://www.dp88.net/wp-content/themes/dp/cx-func/image/logo.png",
    more: {
        sourceTag: "网盘"
    }
*/

import { cheerio, load, _ } from 'assets://js/lib/cat.js';
let HOST = 'https://www.dp88.net';
let siteKey = "", siteType = "", sourceKey = "", ext = "";
let parseMap = {};
const UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36';
function init(cfg) {
    siteKey = cfg.skey;
    siteType = cfg.stype;
    sourceKey = cfg.sourceKey;
    ext = cfg.ext;
    if (ext && ext.indexOf('http') === 0) HOST = ext;
}
async function request(url) {
    try {
        const resp = await req(url, {
            method: 'GET',
            headers: {
                'user-agent': 'Mozilla/5.0 (Linux; Android 12; ALN-AL00 Build/HUAWEIALN-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36',
                'referer': HOST
            }
        });
        return resp.content;
    } catch (error) {
        return null;
    }
}


async function home() {
    const classes = [
        { type_id: "3", type_name: "电影"},
        { type_id: "2", type_name: "电视剧" },
        { type_id: "4", type_name: "动漫" }
    ];

    const filterObj={
       
     "3":[{"key":"cateId","name":"类型","value":[{"n":"全部","v":"0"},{"n":"传记","v":"26"},{"n":"冒险","v":"16"},{"n":"剧情","v":"18"},{"n":"动作","v":"9"},{"n":"动画","v":"30"},{"n":"历史","v":"25"},{"n":"古装","v":"20"},{"n":"同性","v":"27"},{"n":"喜剧","v":"7"},{"n":"奇幻","v":"15"},{"n":"家庭","v":"29"},{"n":"恐怖","v":"13"},{"n":"悬疑","v":"11"},{"n":"情爱","v":"28"},{"n":"惊悚","v":"12"},{"n":"战争","v":"19"},{"n":"歌舞","v":"23"},{"n":"武侠","v":"21"},{"n":"灾难","v":"14"},{"n":"爱情","v":"8"},{"n":"犯罪","v":"17"},{"n":"科幻","v":"10"},{"n":"纪录片","v":"31"},{"n":"西部","v":"22"},{"n":"运动","v":"32"},{"n":"音乐","v":"24"}]},{"key":"year","name":"年代","value":[{"n":"全部","v":"0"},{"n":"2025","v":"187"},{"n":"2024","v":"185"},{"n":"2023","v":"62"},{"n":"2022","v":"66"},{"n":"2021","v":"67"},{"n":"2020","v":"68"},{"n":"2019","v":"65"},{"n":"2018","v":"56"},{"n":"2017","v":"69"},{"n":"2016","v":"70"},{"n":"2015","v":"71"},{"n":"2014","v":"72"},{"n":"2013","v":"73"},{"n":"2012","v":"64"},{"n":"2011","v":"74"},{"n":"2010","v":"184"},{"n":"2009","v":"75"},{"n":"2008","v":"76"},{"n":"2007","v":"77"},{"n":"2006","v":"58"},{"n":"2005","v":"78"},{"n":"2004","v":"79"},{"n":"2003","v":"80"},{"n":"2002","v":"81"},{"n":"2001","v":"82"},{"n":"2000","v":"83"},{"n":"1999","v":"84"},{"n":"1998","v":"85"},{"n":"1997","v":"86"},{"n":"1996","v":"87"},{"n":"1995","v":"88"},{"n":"1994","v":"89"},{"n":"1993","v":"90"},{"n":"1992","v":"91"},{"n":"1991","v":"92"},{"n":"1990","v":"93"}]},{"key":"area","name":"地区","value":[{"n":"全部","v":"0"},{"n":"大陆","v":"33"},{"n":"美国","v":"34"},{"n":"韩国","v":"35"},{"n":"日本","v":"36"},{"n":"香港","v":"37"},{"n":"台湾","v":"38"},{"n":"英国","v":"39"},{"n":"法国","v":"40"},{"n":"德国","v":"41"},{"n":"意大利","v":"42"},{"n":"西班牙","v":"43"},{"n":"印度","v":"44"},{"n":"泰国","v":"45"},{"n":"俄罗斯","v":"46"},{"n":"加拿大","v":"47"},{"n":"爱尔兰","v":"48"},{"n":"瑞典","v":"49"},{"n":"巴西","v":"50"},{"n":"丹麦","v":"51"},{"n":"伊朗","v":"52"},{"n":"波兰","v":"53"},{"n":"澳大利亚","v":"54"},{"n":"其他地区","v":"55"}]},{"key":"sort","name":"排序","value":[{"n":"时间","v":"0"},{"n":"评分","v":"1"}]}],

     "2":[{"key":"cateId","name":"类型","value":[{"n":"全部","v":"0"},{"n":"传记","v":"26"},{"n":"冒险","v":"16"},{"n":"剧情","v":"18"},{"n":"动作","v":"9"},{"n":"动画","v":"30"},{"n":"历史","v":"25"},{"n":"古装","v":"20"},{"n":"同性","v":"27"},{"n":"喜剧","v":"7"},{"n":"奇幻","v":"15"},{"n":"家庭","v":"29"},{"n":"恐怖","v":"13"},{"n":"悬疑","v":"11"},{"n":"情爱","v":"28"},{"n":"惊悚","v":"12"},{"n":"战争","v":"19"},{"n":"歌舞","v":"23"},{"n":"武侠","v":"21"},{"n":"灾难","v":"14"},{"n":"爱情","v":"8"},{"n":"犯罪","v":"17"},{"n":"科幻","v":"10"},{"n":"纪录片","v":"31"},{"n":"西部","v":"22"},{"n":"运动","v":"32"},{"n":"音乐","v":"24"}]},{"key":"year","name":"年代","value":[{"n":"全部","v":"0"},{"n":"2025","v":"187"},{"n":"2024","v":"185"},{"n":"2023","v":"62"},{"n":"2022","v":"66"},{"n":"2021","v":"67"},{"n":"2020","v":"68"},{"n":"2019","v":"65"},{"n":"2018","v":"56"},{"n":"2017","v":"69"},{"n":"2016","v":"70"},{"n":"2015","v":"71"},{"n":"2014","v":"72"},{"n":"2013","v":"73"},{"n":"2012","v":"64"},{"n":"2011","v":"74"},{"n":"2010","v":"184"},{"n":"2009","v":"75"},{"n":"2008","v":"76"},{"n":"2007","v":"77"},{"n":"2006","v":"58"},{"n":"2005","v":"78"},{"n":"2004","v":"79"},{"n":"2003","v":"80"},{"n":"2002","v":"81"},{"n":"2001","v":"82"},{"n":"2000","v":"83"},{"n":"1999","v":"84"},{"n":"1998","v":"85"},{"n":"1997","v":"86"},{"n":"1996","v":"87"},{"n":"1995","v":"88"},{"n":"1994","v":"89"},{"n":"1993","v":"90"},{"n":"1992","v":"91"},{"n":"1991","v":"92"},{"n":"1990","v":"93"}]},{"key":"area","name":"地区","value":[{"n":"全部","v":"0"},{"n":"大陆","v":"33"},{"n":"美国","v":"34"},{"n":"韩国","v":"35"},{"n":"日本","v":"36"},{"n":"香港","v":"37"},{"n":"台湾","v":"38"},{"n":"英国","v":"39"},{"n":"法国","v":"40"},{"n":"德国","v":"41"},{"n":"意大利","v":"42"},{"n":"西班牙","v":"43"},{"n":"印度","v":"44"},{"n":"泰国","v":"45"},{"n":"俄罗斯","v":"46"},{"n":"加拿大","v":"47"},{"n":"爱尔兰","v":"48"},{"n":"瑞典","v":"49"},{"n":"巴西","v":"50"},{"n":"丹麦","v":"51"},{"n":"伊朗","v":"52"},{"n":"波兰","v":"53"},{"n":"澳大利亚","v":"54"},{"n":"其他地区","v":"55"}]},{"key":"sort","name":"排序","value":[{"n":"时间","v":"0"},{"n":"评分","v":"1"}]}],

     "4":[{"key":"cateId","name":"类型","value":[{"n":"全部","v":"0"},{"n":"传记","v":"26"},{"n":"冒险","v":"16"},{"n":"剧情","v":"18"},{"n":"动作","v":"9"},{"n":"动画","v":"30"},{"n":"历史","v":"25"},{"n":"古装","v":"20"},{"n":"同性","v":"27"},{"n":"喜剧","v":"7"},{"n":"奇幻","v":"15"},{"n":"家庭","v":"29"},{"n":"恐怖","v":"13"},{"n":"悬疑","v":"11"},{"n":"情爱","v":"28"},{"n":"惊悚","v":"12"},{"n":"战争","v":"19"},{"n":"歌舞","v":"23"},{"n":"武侠","v":"21"},{"n":"灾难","v":"14"},{"n":"爱情","v":"8"},{"n":"犯罪","v":"17"},{"n":"科幻","v":"10"},{"n":"纪录片","v":"31"},{"n":"西部","v":"22"},{"n":"运动","v":"32"},{"n":"音乐","v":"24"}]},{"key":"year","name":"年代","value":[{"n":"全部","v":"0"},{"n":"2025","v":"187"},{"n":"2024","v":"185"},{"n":"2023","v":"62"},{"n":"2022","v":"66"},{"n":"2021","v":"67"},{"n":"2020","v":"68"},{"n":"2019","v":"65"},{"n":"2018","v":"56"},{"n":"2017","v":"69"},{"n":"2016","v":"70"},{"n":"2015","v":"71"},{"n":"2014","v":"72"},{"n":"2013","v":"73"},{"n":"2012","v":"64"},{"n":"2011","v":"74"},{"n":"2010","v":"184"},{"n":"2009","v":"75"},{"n":"2008","v":"76"},{"n":"2007","v":"77"},{"n":"2006","v":"58"},{"n":"2005","v":"78"},{"n":"2004","v":"79"},{"n":"2003","v":"80"},{"n":"2002","v":"81"},{"n":"2001","v":"82"},{"n":"2000","v":"83"},{"n":"1999","v":"84"},{"n":"1998","v":"85"},{"n":"1997","v":"86"},{"n":"1996","v":"87"},{"n":"1995","v":"88"},{"n":"1994","v":"89"},{"n":"1993","v":"90"},{"n":"1992","v":"91"},{"n":"1991","v":"92"},{"n":"1990","v":"93"}]},{"key":"area","name":"地区","value":[{"n":"全部","v":"0"},{"n":"大陆","v":"33"},{"n":"美国","v":"34"},{"n":"韩国","v":"35"},{"n":"日本","v":"36"},{"n":"香港","v":"37"},{"n":"台湾","v":"38"},{"n":"英国","v":"39"},{"n":"法国","v":"40"},{"n":"德国","v":"41"},{"n":"意大利","v":"42"},{"n":"西班牙","v":"43"},{"n":"印度","v":"44"},{"n":"泰国","v":"45"},{"n":"俄罗斯","v":"46"},{"n":"加拿大","v":"47"},{"n":"爱尔兰","v":"48"},{"n":"瑞典","v":"49"},{"n":"巴西","v":"50"},{"n":"丹麦","v":"51"},{"n":"伊朗","v":"52"},{"n":"波兰","v":"53"},{"n":"澳大利亚","v":"54"},{"n":"其他地区","v":"55"}]},{"key":"sort","name":"排序","value":[{"n":"时间","v":"0"},{"n":"评分","v":"1"}]}]};

    return JSON.stringify({
        class: classes,
        filters: filterObj
    });
}

async function homeVod() {
    const link = `${HOST}/`;
    const html = await request(link);
    const $ = load(html);
    const items = $('.pic-list li');
    const videos = [];

    _.map(items, (item) => {
        const $item = $(item);
        const a = $item.find('a');
        const vod_id = a.attr('href') || '';
        const vod_name = $item.find('h3 b').text().trim() || '未知标题';
        const img = $item.find('img');
        const vod_pic_url = img.attr('data-original') || img.attr('src') || '';
        const vod_remarks = $item.find('.s1').text().trim() || "暂无分类";
        const vod_score = $item.find('.s2').text().trim() || "暂无评分";

        videos.push({
            'vod_id': JSON.stringify({ id: vod_id, title: vod_name }),
            'vod_name': vod_name,
            'vod_pic': vod_pic_url,
            'vod_remarks': vod_remarks + (vod_score !== 'N/A' ? ` ${vod_score}分` : '')
        });
    });

    return JSON.stringify({ list: videos });
}

async function category(tid, pg, filter, extend) {
    if (pg <= 0) pg = 1;
    const homeResult = JSON.parse(await home());
    const filterObj = homeResult.filters;
    if (!filterObj) return null;
    const filterGroup = filterObj[tid];
    if (!filterGroup) return null;
    const area = getFilterValue(filterGroup, 'area', extend);
    const by = getFilterValue(filterGroup,'sort', extend);
    const classValue = getFilterValue(filterGroup, 'class', extend);
    const year = getFilterValue(filterGroup, 'year', extend);
    const cateId = getFilterValue(filterGroup, 'cateId', extend);

    const link = `${HOST}/list/${by}_${area}_${year}_${cateId}_${tid}/${pg}/`;
    const html = await request(link);
    const $ = load(html);
    const items = $('.pic-list li');
    const videos = [];
    _.map(items, (item) => {
        const $item = $(item);
        const a = $item.find('a');
        const vod_id = a.attr('href');
        const vod_name = $item.find('h3 b').text().trim() || '未知标题';
        const img = $item.find('img');
        const vod_pic_url = img.attr('data-original') || img.attr('src') || '';
        const vod_remarks = $item.find('.s1').text().trim() || "暂无备注";
        const vod_score = $item.find('.s2').text().trim() || "暂无评分";

        videos.push({
            'vod_id': JSON.stringify({ id: vod_id, title: vod_name }),
            'vod_name': vod_name,
            'vod_pic': vod_pic_url,
            'vod_remarks': vod_remarks + (vod_score !== 'N/A' ? ` ${vod_score}分` : '')
        });
    });

    return JSON.stringify({ list: videos });
}

function getFilterValue(filterGroup, key, extend) {
    if (!Array.isArray(filterGroup) || filterGroup.length === 0) return '';
    const filterItem = filterGroup.find(item => item.key === key);
    if (!filterItem) return '';
    if (!Array.isArray(filterItem.value) || filterItem.value.length === 0) return '';
    const userValue = extend[key];
    if (userValue) {
        const option = filterItem.value.find(opt => opt.v === userValue);
        return option? option.v : '';
    }
    return filterItem.value[0].v;
}

async function search(wd) {
    const searchUrl = `${HOST}/?s=${encodeURIComponent(wd)}`;

    try {
        const html = await request(searchUrl);
        const $ = load(html);

        const items = $('.sr_lists li');
        const videos = [];

        Array.from(items).forEach((item) => {
            const $item = $(item);
            const a = $item.find('h3 a');
            const img = $item.find('.sr_img img');
            const vod_id = a.attr('href');
            if (!vod_id) return;
            const vod_name = a.text().trim() || '未知标题';
            const vod_pic = img.attr('src');
            if (vod_name.toLowerCase().includes(wd.toLowerCase())) {
                videos.push({
                    'vod_id': JSON.stringify({ id: vod_id, title: vod_name }),
                    'vod_name': vod_name,
                    'vod_pic': vod_pic
                });
            }
        });

        return JSON.stringify({ list: videos });
    } catch (error) {
        throw error;
    }
}

async function detail(id) {
    const ids = JSON.parse(id);

    try {
        const html = await request(ids.id);
        if (!html) return JSON.stringify({ list: [], error: 'HTML内容为空' });
        const $ = load(html);
        const vod = {
            vod_id: ids.id,
            vod_name: $('h1').text().trim(),
            vod_type: $('.content-rt p:contains("类型：") a').map((_, el) => $(el).text().trim()).get().join('/'),
            vod_year: $('.content-rt .year').text().replace(/[()]/g, '').trim(),
            vod_area: $('.content-rt p:contains("地区：")').text().replace('地区：', '').trim(),
            vod_actor: $('.content-rt p:contains("主演：")').text().replace('主演：', '').trim(),
            vod_director: $('.content-rt p:contains("导演：")').text().replace('导演：', '').trim(),
            vod_pic: $('.img img').attr('src'),
            vod_content: $('.movie-introduce .zk_a').text().replace('展开', '').trim(),
            vod_play_from: '',
            vod_play_url: ''
        };
        const diskGroups = {};
        $('.pd-row').each((_, row) => {
            const sourceName = $(row).find('h2').text().trim();
            $(row).find('.lip a').each((_, link) => {
                const href = $(link).attr('href');
                if (href && href.startsWith('magnet:?')) return;            
                const title = $(link).attr('title') || $(link).text();
                if (!diskGroups[sourceName]) {                    diskGroups[sourceName] = [];
                }
                diskGroups[sourceName].push(`${title}$push://${href}`);
            });
        });
        const diskPlayFrom = [];
        const diskPlayUrl = [];
        for (const [sourceName, items] of Object.entries(diskGroups)) {
            if (items.length > 0) {
                diskPlayFrom.push(sourceName);
                diskPlayUrl.push(items.join('#'));
            }
        }
        const onlinePlayFrom = [];
        const onlinePlayUrl = [];
        $('#playlist-js option').each((_, option) => {
            const sourceName = $(option).text().trim();
            const sourceId = $(option).val();
            const episodes = [];            
            $(`#tabid-${sourceId} a`).each((_, link) => {
                const href = $(link).attr('href');
                if (href && href.startsWith('magnet:?')) return;           
                const epName = $(link).text().trim();
                episodes.push(`${epName}$${href}`);
            });
            if (episodes.length) {
                onlinePlayFrom.push(sourceName);
                onlinePlayUrl.push(episodes.join('#'));
            }
        });
        vod.vod_play_from = [
            ...diskPlayFrom,
            ...onlinePlayFrom
        ].join('$$$');        
        vod.vod_play_url = [
            ...diskPlayUrl,
            ...onlinePlayUrl
        ].join('$$$');
        return JSON.stringify({ list: [vod] });
    } catch (error) {
        return JSON.stringify({ 
            list: [], 
            error: `解析失败: ${error.message}` 
        });
    }
}

async function play(flag, id, flags) {
    try {
        if (id.startsWith('push://')) {
            return JSON.stringify({
                parse: 0,
                url: id,
                header: {}
            });
        }
        const html = await request(id);
        const $ = load(html);
        const iframeSrc = $('iframe').attr('src');
        let m3u8Url;
        if (iframeSrc.includes('?url=')) {
            const parts = iframeSrc.split('?url=');
            m3u8Url = parts[1];
        } else {
            m3u8Url = iframeSrc;
        }
        if (!m3u8Url.match(/https?:\/\/[^\s]+\.m3u8/)) {
            throw new Error('未找到有效的 m3u8 链接');
        }
        return JSON.stringify({
            parse: 0,
            url: m3u8Url,
            header: {
                'User-Agent': UA,
                'Referer': id
            }
        });
    } catch (error) {
        return JSON.stringify({
            parse: 1,
            error: error.message
        });
    }
}


export function __jsEvalReturn() {
    return {
        init: init,
        home: home,
        homeVod: homeVod,
        detail: detail,
        category: category,
        play: play,
        proxy: null,
        search: search,
        extResult: null
    };
}