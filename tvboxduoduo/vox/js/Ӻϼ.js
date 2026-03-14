var rule = {
    title:'央视频',
    host:'https://api.cntv.cn',
    homeUrl: '/lanmu/columnSearch?&fl=&fc=&cid=&p=1&n=500&serviceId=tvcctv&t=json',
  //  url:'/list/getVideoAlbumList?fyfilter&area=&letter=&n=24&serviceId=tvcctv&t=json',
  url: '/NewVideo/getVideoListByColumn?id=fyclass&n=10&sort=desc&p=fypage&mode=0&serviceId=tvcctv',
  url:'/lanmu/columnSearch?&fl=&fc=fyclass&cid=&p=fypage&n=500&serviceId=tvcctv&t=json',
    searchUrl:'',
    searchable:0,
    quickSearch:0,
    
   class_name: '体育&综艺&健康&生活&科教&经济&农业&法治&军事&少儿&动画',
class_url:'体育&综艺&健康&生活&科教&经济&农业&法治&军事&少儿&动画',

    filterable: 1,  
    headers:{
        'User-Agent':'PC_UA'
    },
    timeout:10000,
    play_parse:true,
    
    limit:6,
    double:false,

    一级: $js.toString(() => {
        var d = [];
        var list = JSON.parse(request(input)).response.docs;
        list.forEach(it => {
        let guid1 = it.lastVIDE.videoSharedCode;
            // 一级标题
            let title1 = it.column_name;
            // 一级描述
            let desc1 =  it.column_playdate + it.channel_name ;
            // 一级图片URL
            let picUrl1 = it.column_logo;
            // 一级URL（id 地区 类型 标题 演员 年份 频道 简介 图片 更新至）
            let url1 = it.lastVIDE.videoSharedCode + '|' + '' + '|' + it.column_firstclass + '|' + it.column_name + '|' + '' + '|' + it.column_playdate + '|' + it.channel_name + '|' + it.column_brief + '|' + it.column_logo + '|' + '' + '|' + it.lastVIDE.videoTitle;

            d.push({
                desc : desc1,
                title : title1,
                pic_url : picUrl1,
                url : url1
            })
        })
        setResult(d);
    }),

二级 : $js.toString(() => {
let info = input.split("|");
let guid = info[0].replaceAll('https://api.cntv.cn/lanmu/', '');
    VOD = {
            vod_id: info[1],
            vod_name: info[3],
            vod_pic: info[5],
            type_name: info[2],
            vod_year: info[2],
            vod_area: info[1],
            vod_remarks: 'ƪ(˘⌣˘)ʃ优雅',
            vod_director: 'ƪ(˘⌣˘)ʃ优雅',
            vod_actor: 'ƪ(˘⌣˘)ʃ优雅',
            vod_content: info[7],
        vod_play_from: '央视频',
        //https://hls.cntv.myalicdn.com//asp/hls/2000/0303000a/3/default/https://api.cntv.cn/lanmu/1a01871d6d5f4d4bbe82b9c62650f100/2000.m3u8
        vod_play_url: '立即播放$https://cntv.playdreamer.cn/proxy/asp/hls/2000/0303000a/3/default/' + guid + '/2000.m3u8'
    };

}),
    搜索:'',
}