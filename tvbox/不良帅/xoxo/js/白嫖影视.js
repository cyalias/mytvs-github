muban.首图2.二级.title = '.stui-content__detail .title--span&&Text;.stui-content__detail p&&a&&Text';
muban.首图2.二级.content = 'p.col-pd&&Text';
muban.首图2.二级.tabs = '.stui-pannel_hd h3';
muban.首图2.二级.lists = '.stui-content__playlist:eq(#id) li';
muban.首图2.二级.desc = 'p.data:eq(3)&&Text;p.data&&a:eq(-1)&&Text;p.data&&a:eq(-2)&&Text;p.data:eq(1)&&Text;p.data:eq(2)&&Text';
var rule = {
	title: '白嫖影视',
	模板: '首图2',
	host: 'https://www.baipiaoys.com:9092',
	url: '/show/id/fyclass/page/fypage.html',
    searchUrl:'/search/page/fypage/wd/**.html',
	filterable: 0,//是否启用分类筛选,
	tab_exclude:'影片|评论|榜单',
	lazy: ``,
}