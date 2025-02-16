var rule = {
  title: '厂长资源',
  host:'https://www.czzy.site/',
  //host: 'https://www.czys01.com',
  //hostJs: 'print(HOST);let html=request(HOST,{headers:{"User-Agent":PC_UA}});HOST = jsp.pdfh(html,"h3&&a&&href")',
  hostJs:'print(HOST);let html=request(HOST,{headers:{"User-Agent":PC_UA}});HOST = html.match(/推荐访问<a href="(.*)"/)[1];print("厂长跳转地址 =====> " + HOST)',
  //hostJs:'print(HOST);let html=request(HOST,{headers:{"User-Agent":PC_UA}});HOST = $("div.jumbotron >h2:first >a:first[href]").attr("href");print("厂长跳转地址 =====> " + HOST)',
  url: '/fyclassfyfilter',
  class_name: '动漫&全部&国产剧&美剧&日剧&韩剧&海外剧&最新电影&豆瓣top250电影&华语电影&欧美电影&日本电影&韩国电影&软件下载地址tvbox.plus',
  class_url: 'movie_bt_series/dohua&/movie_bt&/movie_bt_series/guochanju&meiju&riju&hanju&haiwaiju&zuixindianying&dbtop250&huayudianying&oumeidianying&ribendianying&hanguodianying&yingguodianying',
  filterable: 1,//是否启用分类筛选,
  filter_url: '{{fl.cateId}}{{fl.class}}{{fl.area}}/page/fypage',
  filter: {
    "movie_bt": [
      {
        "key": "area",
        "name": "分类",
        "value": [
          {
            "v": "",
            "n": "全部"
          },
          {
            "v": "/movie_bt_series/dohua",
            "n": "动漫"
          },
          {
            "v": "/movie_bt_series/dianshiju",
            "n": "电视剧"
          },
          {
            "v": "/movie_bt_series/guochanju",
            "n": "国产剧"
          },
          {
            "v": "/movie_bt_series/mj",
            "n": "美剧"
          },
          {
            "v": "/movie_bt_series/rj",
            "n": "美剧"
          },
          {
            "v": "/movie_bt_series/hj",
            "n": "美剧"
          },
          {
            "v": "/movie_bt_series/hwj",
            "n": "海外剧（其他）"
          },
          {
            "v": "/movie_bt_series/dyy",
            "n": "电影"
          },
          {
            "v": "/movie_bt_series/huayudianying",
            "n": "华语电影"
          },
          {
            "v": "/movie_bt_series/meiguodianying",
            "n": "欧美电影"
          },
          {
            "v": "/movie_bt_series/ribendianying",
            "n": "日本电影"
          },
          {
            "v": "/movie_bt_series/hanguodianying",
            "n": "韩国电影"
          },
          {
            "v": "/movie_bt_series/yingguodianying",
            "n": "英国电影"
          },
          {
            "v": "/movie_bt_series/faguodianying",
            "n": "法国电影"
          },
          {
            "v": "/movie_bt_series/yindudianying",
            "n": "印度电影"
          },
          {
            "v": "/movie_bt_series/eluosidianying",
            "n": "俄罗斯电影"
          },
          {
            "v": "/movie_bt_series/jianadadianying",
            "n": "加拿大电影"
          },
          {
            "v": "/movie_bt_series/huiyuanzhuanqu",
            "n": "会员专区"
          }
        ]
      }
    ]
  },
  searchUrl: '/page/fypage?s=**',
  searchable: 2,
  filterable: 0,
  headers: {
    'User-Agent': 'MOBILE_UA',
    'Cookie': 'esc_search_captcha=1'
  },
  play_parse: true,

  // lazy代码:源于海阔香雅情大佬 / 小程序：香情影视 https://pastebin.com/L4tHdvFn
  lazy: `js:
        pdfh = jsp.pdfh;
        var html = request(input);
        var ohtml = pdfh(html, '.videoplay&&Html');
        var url = pdfh(ohtml, "body&&iframe&&src");
        if (/Cloud/.test(url)) {
            var ifrwy = request(url);
            let code = ifrwy.match(/var url = '(.*?)'/)[1].split('').reverse().join('');
            let temp = '';
            for (let i = 0x0; i < code.length; i = i + 0x2) {
                temp += String.fromCharCode(parseInt(code[i] + code[i + 0x1], 0x10))
            }
            input = {
                jx: 0,
                url: temp.substring(0x0, (temp.length - 0x7) / 0x2) + temp.substring((temp.length - 0x7) / 0x2 + 0x7),
                parse: 0
            }
        } else if (/decrypted/.test(ohtml)) {
            var phtml = pdfh(ohtml, "body&&script:not([src])&&Html");
            eval(getCryptoJS());
            var scrpt = phtml.match(/var.*?\\)\\);/g)[0];
            var data = [];
            eval(scrpt.replace(/md5/g, 'CryptoJS').replace('eval', 'data = '));
            input = {
                jx: 0,
                url: data.match(/url:.*?[\\'\\"](.*?)[\\'\\"]/)[1],
                parse: 0
            }
        } else {
            input
        }
	`,
  double: true,
  一级: '.bt_img&&ul&&li;h3.dytit&&Text;img.lazy&&data-original;.jidi&&Text;a&&href',
  二级: {
    "title": "h1&&Text;.moviedteail_list li&&a&&Text",
    "img": "div.dyimg img&&src",
    "desc": ".moviedteail_list li:eq(3) a&&Text;.moviedteail_list li:eq(2) a&&Text;.moviedteail_list li:eq(1) a&&Text;.moviedteail_list li:eq(7)&&Text;.moviedteail_list li:eq(5)&&Text",
    "content": ".yp_context&&Text",
    "tabs": ".mi_paly_box span",
    "lists": ".paly_list_btn:eq(#id) a"
  }
}
