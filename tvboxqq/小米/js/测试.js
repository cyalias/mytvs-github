//获取vodlist  http://124.220.133.60:6868
globalThis.vodlist = function (t, pg) {
    let time = Date.now();
    const options = {
        method: 'GET',
        headers: {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        }
    };
    let html = fetch('http://111.173.114.61:8762/apptov5/v1/vod/lists?type_id=' + t + '&area=&year=&order=time&type_name=&page=' + pg + '&pageSize=21', options);
    return JSON.parse(html);
}


globalThis.vodids = function (ids) {
        const options = {
            method: 'GET',
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            }
        };
        let html = fetch('http://111.173.114.61:8762/apptov5/v1/vod/getVod?id=' + ids, options)
        let bata = JSON.parse(html);
        let rdata = bata.data;

        // 创建 data 对象并初始化
        let data = {
            vod_id: ids,
            vod_name: rdata.vod_name,
            vod_remarks: rdata.vod_remarks,
            vod_actor: rdata.vod_actor,
            vod_director: rdata.vod_director,
            vod_content: rdata.vod_content,
            vod_play_from: '',
            vod_play_url: ''
        };

        // 遍历 vod_play_list 数组
        rdata.vod_play_list.forEach((value) => {
            data.vod_play_from += value.player_info.show + '|广告勿信$$$';

            // 遍历 urls 数组
            value.urls.forEach((v) => {
                data.vod_play_url += v.name + "$" + value.player_info.from + '|' + v.url + '|' + rdata.vod_name + '|' + v.name + "#";
            });

            data.vod_play_url += '$$$';
        });
        return data;
    }
    //console.log(vodids(153367));

globalThis.svodlist = function (wd) {
    const options = {
        method: 'GET',
        headers: {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        }
    };
    let html = fetch('http://111.173.114.61:8762/apptov5/v1/search/lists?wd=' + wd + '&page=1&type=', options)
    return JSON.parse(html);
}

globalThis.jxx = function (id, nid) {
    let label;
    if (id == 'NBY') {
        label = 'mayi';
    }
    if (id == 'BBA') {
        label = 'bba';
    }
    if (id == 'xlink') {
        label = 'xlzy';
    }
    if (id == 'ffm3u8') {
        label = 'delad';
    }
    if (id == 'lzm3u8') {
        label = 'delad';
    }
    if (id == 'rym3u8') {
        label = 'delad';
    }
    if (id == '360zy') {
        label = 'delad';
    }
    if (id == 'qiyi') {
        label = 'mitu';
    }
    if (id == 'qq') {
        label = 'mitu';
    }
    if (id == 'nmlink') {
        label = 'wwzy';
    }
    if (id == 'xlink') {
        label = 'xlzy';
    }
    if (id == 'duanju') {
        label = '1';
    }
    if (id == 'duboku') {
        label = '1';
    }
    if (id == 'rebo') {
        label = '1';
    }
    if (id == 'oule') {
        label = '1';
    }
    if (id == 'duboku') {
        label = '1';
    }
    if (id == 'bilibili') {
        label = 'yt';
    }
    if (id == 'youku') {
        label = 'yt';
    }
    if (id == 'mgtv') {
        label = 'yt';
    }
    if (id == 'qiyi') {
        label = 'yt';
    }
    if (id == 'yhdm') {
        label = '1';
    }
    if (id == 'dmbs1') {
        label = 'w';
    }
    if (id == 'tkyun') {
        label = '1';
    }
    if (id == 'cxyun') {
        label = '1';
    }
    if (id == 'yd189') {
        label = '1';
    }
    if (id == 'jqq') {
        label = '1';
    }
     if (id == 'ty_new1') {
        label = '1';
    }
    if (id == 'hjkk') {
        label = '1';
    }
    if (id == '4kav') {
        label = '1';
    }
    if (id == '4kvip') {
        label = '3';
    }
    if (id == 'Cloud') {
        label = '云盘';
    }
    const options = {
        method: 'POST',
        headers: {
            'User-Agent': 'Dart/2.19 (dart:io)',
            'appto-local-uuid': '58c9aa5a-ff7b-4ac0-9627-7dca80c23bd4'
        },
        body: {
            'play_url': nid,
            'label': label,
            'key': id
        }
    };
    let html = fetch('http://111.173.114.61:8762/apptov5/v1/parsing/proxy', options)
    console.log(html);
    return JSON.parse(html).data.url !==undefined ? JSON.parse(html).data.url : "解析失败";
    if ("104847347" == '104847347') {
        return JSON.parse(html1).data.url;
    } else {
        return '';
    }
}

globalThis.sss = function (wd) {
    let dm = request('' + wd);
    var html1 = fetch('', {
        method: 'POST',
        headers: {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        },
        body: {
            data: btoa(encodeURIComponent(dm)),
        }
    });
    return html1;
}

var rule = {
    title: '九龙',
    host: '',
    detailUrl: 'fyid',
    searchUrl: '**',
    url: 'fyclass',
    searchable: 2,
    quickSearch: 1,
    filterable: 0,
    class_name: '电影&电视剧&综艺&动漫',
    class_url: '1&2&3&4',
    play_parse: true,
    lazy: $js.toString(() => {
        const parts = input.split('|');
        input = {
            parse: 0,
            url: jxx(parts[0], parts[1]),
            jx: 0,
            danmaku: '' + '&jm=' + parts[2] + '&js=' + parts[3] + '&key=104847347'
        };

    }),
    推荐: $js.toString(() => {
        let bdata = vodlist(1, 1);
        console.log(bdata);
        let bata = bdata.data.data;
        bata.forEach(it => {
            d.push({
                url: it.vod_id,
                title: it.vod_name,
                img: it.vod_pic,
                desc: it.vod_remarks
            });
        });
        setResult(d);
    }),
    一级: $js.toString(() => {
        let bdata = vodlist(input, MY_PAGE);
        console.log(bdata);
        let bata = bdata.data.data;
        bata.forEach(it => {
            d.push({
                url: it.vod_id,
                title: it.vod_name,
                img: it.vod_pic,
                desc: it.vod_remarks
            });
        });
        setResult(d);
    }),
    二级: $js.toString(() => {
        console.log("调试信息2" + input);
        let data = vodids(input);
        //console.log(data);
        VOD = data;
    }),
    搜索: $js.toString(() => {
        let ddata = svodlist(input);
        console.log(ddata);
        ddata.data.data.forEach(it => {
            d.push({
                url: it.vod_id,
                title: it.vod_name,
                img: it.vod_pic,
                desc: it.vod_remarks
            });
        });
        //  console.log(data);
        setResult(d);
    }),
}
