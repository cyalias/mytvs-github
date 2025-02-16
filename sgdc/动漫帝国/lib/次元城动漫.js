var rule = {
    title: '次元城动漫', // csp_AppYsV2
    host: 'http://app.95189371.cn/ciyuancheng.php/v6/',
    url: 'video?tid=fyclassfyfilter&limit=20&pg=fypage',
    filter_url:'&class={{fl.class}}&year={{fl.year}}&order={{fl.order}}',
    filter:{
        "20":[{"key":"order","name":"最新","value":[{"n":"最热","v":"hits"},{"n":"好评","v":"score"}]},{"key":"class","name":"分类","value":[{"n":"全部","v":""},{"n":"原创","v":"原创"},{"n":"漫画改","v":"漫画改"},{"n":"小说改","v":"小说改"},{"n":"游戏改","v":"游戏改"},{"n":"特摄","v":"特摄"},{"n":"热血","v":"热血"},{"n":"穿越","v":"穿越"},{"n":"奇幻","v":"奇幻"},{"n":"战斗","v":"战斗"},{"n":"搞笑","v":"搞笑"},{"n":"日常","v":"日常"},{"n":"科幻","v":"科幻"},{"n":"治愈","v":"治愈"},{"n":"校园","v":"校园"},{"n":"泡面","v":"泡面"},{"n":"恋爱","v":"恋爱"},{"n":"少女","v":"少女"},{"n":"魔法","v":"魔法"},{"n":"冒险","v":"冒险"},{"n":"历史","v":"历史"},{"n":"架空","v":"架空"},{"n":"机战","v":"机战"},{"n":"运动","v":"运动"},{"n":"励志","v":"励志"},{"n":"音乐","v":"音乐"},{"n":"推理","v":"推理"},{"n":"社团","v":"社团"},{"n":"智斗","v":"智斗"},{"n":"催泪","v":"催泪"},{"n":"美食","v":"美食"},{"n":"偶像","v":"偶像"},{"n":"乙女","v":"乙女"},{"n":"职场","v":"职场"}]},{"key":"year","name":"年份","value":[{"n":"全部","v":""},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"2014","v":"2014"},{"n":"2013","v":"2013"},{"n":"2012","v":"2012"},{"n":"2011","v":"2011"},{"n":"2010","v":"2010"},{"n":"2009","v":"2009"},{"n":"2008","v":"2008"},{"n":"2006","v":"2006"},{"n":"2005","v":"2005"},{"n":"2004","v":"2004"},{"n":"2003","v":"2003"},{"n":"2002","v":"2002"},{"n":"2001","v":"2001"},{"n":"2000","v":"2000"}]}],
        "21":[{"key":"order","name":"最新","value":[{"n":"最热","v":"hits"},{"n":"好评","v":"score"}]},{"key":"year","name":"年份","value":[{"n":"全部","v":""},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"2014","v":"2014"},{"n":"2013","v":"2013"},{"n":"2012","v":"2012"},{"n":"2011","v":"2011"},{"n":"2010","v":"2010"},{"n":"2009","v":"2009"},{"n":"2008","v":"2008"},{"n":"2006","v":"2006"},{"n":"2005","v":"2005"},{"n":"2004","v":"2004"},{"n":"2003","v":"2003"},{"n":"2002","v":"2002"},{"n":"2001","v":"2001"},{"n":"2000","v":"2000"}]}]
    },
    detailUrl:'/detail?vod_id=fyid',
    searchUrl: '/search?text=**&pg=fypage',
    searchable: 2,
    quickSearch: 1,
    filterable:1,//是否启用分类筛选,
    headers:{'User-Agent':'Dart/2.18 (dart:io)'},
    timeout:5000,
    class_name:'TV动画&剧场版&4K专区',
    class_url:'20&21&26',
    play_parse: true,
    lazy:'js:if(/m3u8|mp4/.test(input)){input}else{let purl=request(input);input={jx:0,url:JSON.parse(purl).url,parse:0}}',
    limit:6,
    // 图片来源:'@Referer=https://api.douban.com/@User-Agent=Mozilla/5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/113.0.0.0%20Safari/537.36',
    推荐:`js:
        let d = [];
        let jsondata = [];
        let videoList = [];
        if (/v1\\.vod/.test(HOST)) {
            if(HOST.endsWith('/')){
                jsondata = JSON.parse(request(HOST + 'vodPhbAll'));
            } else {
                jsondata = JSON.parse(request(HOST + '/vodPhbAll'));
            }
            videoList = jsondata.data.list;
        } else {
            if(HOST.endsWith('/')){
                jsondata = JSON.parse(request(HOST + 'index_video'));
            } else {
                jsondata = JSON.parse(request(HOST + '/index_video?token='));
            }
            videoList = /ciyuancheng/.test(HOST) ? jsondata.data : jsondata.list;
        }
        // log('videoList =========> '+stringify(videoList));
        videoList.forEach((it,idex) => {
            let vlist = /v1\\.vod/.test(HOST) ? videoList[idex].vod_list : videoList[idex].vlist ;
            vlist.forEach(it => {
                d.push({
                    url:it.vod_id,
                    title:it.vod_name,
                    img:it.vod_pic.startsWith('http') ? it.vod_pic : it.vod_pic.startsWith('//') ? 'https:' + it.vod_pic : it.vod_pic.startsWith('/') ? getHome(HOST) + it.vod_pic : getHome(HOST) + '/' + it.vod_pic,
                    desc:it.vod_remarks,
                });
            });
        });
        setResult(d);
    `,
    一级:`js:
        let d = [];
        let jsondata = [];
        let videoList = [];
        if (/v1\\.vod/.test(HOST)) {
            input = input.replace('video','v1.vod').replace('tid','type').replace('pg=','page=');
            jsondata = JSON.parse(request(input));
            videoList = jsondata.data.list;
        } else {
            input = HOST + '/'+ input.split('/')[4];
            jsondata = JSON.parse(request(input));
            videoList = jsondata.list || jsondata.data;
        }
        // log('videoList =========> '+stringify(videoList));
        videoList.forEach(it => {
            d.push({
                url:it.vod_id,
                title:it.vod_name,
                img:it.vod_pic.startsWith('http') ? it.vod_pic : it.vod_pic.startsWith('//') ? 'https:' + it.vod_pic : it.vod_pic.startsWith('/') ? getHome(HOST) + it.vod_pic : getHome(HOST) + '/' + it.vod_pic,
                desc:it.vod_remarks,
            });
        });
        setResult(d);
    `,
	二级:`js: 
        if (/v1\\.vod/.test(HOST)) {
            input = HOST + '/'+ input.split('/')[3];
        } else {
            input = HOST + '/'+ input.split('/')[3].replace('detail','video_detail').replace('vod_id','id');
        }
        try {
            let html = request(input);
            html = JSON.parse(html);
            let node = /ciyuancheng/.test(HOST) ? html.data.vod_info : html.data;
            VOD = {
                vod_id: node.vod_id,
                vod_name: node.vod_name,
                vod_pic: node.vod_pic,
                type_name: node.vod_class,
                vod_year: node.vod_year,
                vod_area: node.vod_area,
                vod_remarks: node.vod_remarks,
                vod_actor: node.vod_actor,
                vod_director: node.vod_director,
                vod_content: node.vod_content.strip()
            };
            if (typeof play_url === 'undefined') {
                var play_url = ''
            }
            let episodes = /v1\\.vod/.test(HOST)?node.vod_play_list:node.vod_url_with_player;
            if (episodes != '') {
                let playMap = {};
                episodes.forEach(ep => {
                    let from = [];
                    if (/v1\\.vod/.test(HOST)) {
                        from = ep.player_info.from||ep.player_info.show||ep.from||ep.show;
                    } else {
                        from = ep.code||ep.name;
                    }
                    if (!playMap.hasOwnProperty(from)) {
                        playMap[from] = []
                    }
                    let parse_api = '';
                    if (/v1\\.vod/.test(HOST)) {
                        parse_api = ep.player_info.parse != null ? ep.player_info.parse : ep.player_info.parse2;
                        // parse_api = /,/.test(parse_api) ? parse_api.split(',')[1] : parse_api;
                    } else {
                        parse_api = ep.parse_api;
                    }
                    log('parse_api =========> '+parse_api);
                    if (parse_api != null && !/\\.m3u8|\\.mp4/.test(ep.url)) {
                        parse_api = parse_api.replaceAll('..','.') ;
                        ep.url = ep.url.replaceAll('$','$'+parse_api);
                    }
                    playMap[from].push(ep.url)
                });
                let playFrom = ['次元城'];
                let playList = [];
                Object.keys(playMap).forEach(key => {
                    playFrom.push(key);
                    playList.push(playMap[key])
                });
                VOD.vod_play_from = playFrom.join('$$$');
                VOD.vod_play_url = playList.join('$$$');
            } else {
                VOD.vod_play_from = node.vod_play_from;
                VOD.vod_play_url = node.vod_play_url;
            }
        } catch (e) {
            log("获取二级详情页发生错误:" + e.message);
        }
	`,
	搜索:`js:
		let d = [];
		let jsondata = [];
		let videoList = [];
		if (/v1\\.vod/.test(HOST)) {
			input = (HOST + '/'+ input.split('/')[3]).replace('/search','').replace('text=','wd=').replace('pg=','page=');
			jsondata = JSON.parse(request(input));
			videoList = jsondata.data.list;
		} else {
			input = HOST + '/'+ input.split('/')[3]
			jsondata = JSON.parse(request(input));
			videoList = jsondata.list || jsondata.data;
		}
		// log('videoList =========> '+stringify(videoList));
		videoList.forEach(it => {
			d.push({
				url:it.vod_id,
				title:it.vod_name,
				img:it.vod_pic.startsWith('http') ? it.vod_pic : it.vod_pic.startsWith('//') ? 'https:' + it.vod_pic : it.vod_pic.startsWith('/') ? getHome(HOST) + it.vod_pic : getHome(HOST) + '/' + it.vod_pic,
				desc:it.vod_remarks,
			});
		});
		setResult(d);
	`,
}