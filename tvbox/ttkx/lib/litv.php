<?php
error_reporting(0);
header('Content-Type: text/json;charset=UTF-8',true,200);
$id = $_GET["id"];
$ids = array(
"dsxw"=>"4gtv-4gtv152",//东森新闻台
"hsxw"=>"4gtv-4gtv052",//华视新闻
"msxw"=>"litv-ftv13",//民视新闻台
"tvbsxw"=>"4gtv-4gtv072",//TVBS新闻
"tvbs"=>"4gtv-4gtv073",//TVBS
"dscjxw"=>"4gtv-4gtv153",//东森财经新闻台
"zsxw"=>"4gtv-4gtv074",//中视新闻
"ztxw"=>"4gtv-4gtv009",//中天新闻台
"hyxw"=>"litv-longturn14",//寰宇新闻台
"msly"=>"litv-ftv07",//民视旅游台
"yzly"=>"litv-longturn17",//亚洲旅游台
"snhrjs"=>"4gtv-4gtv013",//视纳华仁纪实频道
"jtdy"=>"4gtv-4gtv061",//靖天电影台
"lhdy"=>"litv-longturn03",//龙华电影台
"ymswdy"=>"4gtv-4gtv011",//影迷数位电影台
"amc"=>"4gtv-4gtv017",//AMC最爱电影
);
$keys = array(
"dsxw"=>"avc1_2000000=3-mp4a_138000_zho=6",//东森新闻台
"hsxw"=>"avc1_3000000=3-mp4a_133000_zho=2",//华视新闻
"msxw"=>"avc1_2000000=3-mp4a_122000_zho=7",//民视新闻台
"tvbsxw"=>"avc1_3000000=3-mp4a_130000_zho=2",//TVBS新闻
"tvbs"=>"avc1_3000000=3-mp4a_130000_zho=2",//TVBS
"dscjxw"=>"avc1_2000000=3-mp4a_129000=6",//东森财经新闻台
"zsxw"=>"avc1_3000000=3-mp4a_116000_zho=2",//中视新闻
"ztxw"=>"avc1_3000000=8-mp4a_136000_zho=7",//中天新闻台
"hyxw"=>"avc1_2000000=3-mp4a_166000_zho=6",//寰宇新闻台
"msly"=>"avc1_2000000=3-mp4a_134000_zho=7",//民视旅游台
"yzly"=>"avc1_2936000=4-mp4a_128000=2",//亚洲旅游台
"snhrjs"=>"avc1_2000000=3-mp4a_122000_zho=2",//视纳华仁纪实频道
"jtdy"=>"avc1_2000000=3-mp4a_132000_zho=7",//靖天电影台
"lhdy"=>"avc1_2936000=4-mp4a_127000=2",//龙华电影台
"ymswdy"=>"avc1_2000000=3-mp4a_136000=6",//影迷数位电影台
"amc"=>"avc1_2000000=3-mp4a_139000_zho=6",//AMC最爱电影
);
$time = time();
$seq = intval(explode(".",strval(($time - 1420070500) / 4))[0]);
$begin_ts = $seq * 4;
$tss = 12;//切多少个ts
$current = "#EXTM3U"."\r\n";
$current.="#EXT-X-VERSION:3"."\r\n";
$current.="#EXT-X-TARGETDURATION:4"."\r\n";
$current.="#EXT-X-MEDIA-SEQUENCE:".strval($seq)."\r\n";
for($i=0;$i<$tss;$i++){
$current.="#EXTINF:4,"."\r\n";
$current.="https://litvpc-hichannel.cdn.hinet.net/live/pool/{$ids[$id]}/litv-pc/{$ids[$id]}-{$keys[$id]}-begin=".strval($begin_ts)."0000000-dur=40000000-seq=".strval($seq).".ts"."\r\n";
$begin_ts = $begin_ts + 4;
$seq_m3u8 = $seq + 1;
}
print_r($current);
?>