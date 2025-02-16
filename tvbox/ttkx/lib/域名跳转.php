<?php
// 判断浏览器类型
$ua = $_SERVER['HTTP_USER_AGENT'];
if (strpos($ua, 'okhttp/') !== false) {
    // 获取域名
    $domain = $_SERVER['HTTP_HOST'];
    // 根据域名进行逻辑判断
    switch ($domain) {
        case 'rihou.cc:55':
        case 'rihou.vip:55':
            // 引入hccx.json文件
            include './lib/kx2024.txt';
            break;
        default:
            // 默认跳转
            include './lib/kx2024.txt';
            break;
    }
    exit;
} elseif (strpos($ua, 'MicroMessenger') !== false) {
    header('Location: https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzkwODQ5NDI2Mw==#wechat_redirect');
    exit;
} else {
    $html = <<<HTML
    <!DOCTYPE html>
    <html>
    <head>
        <title>日后魔改</title>
    </head>
    <body>
        <p style="font-size: 100px; text-align: center; color: #ff0033;">关注微信公众号</p>
        <p style="font-size: 180px; text-align: center; color: #ff0033;">日后魔改</p>
        <p style="font-size: 100px; text-align: center; color: #ff0033;">QQ群：237658557</p>
        <p style="font-size: 100px; text-align: center; color: #ff0033;">天天开心路线</p>
    </body>
    <script type="text/javascript" src="https://js.users.51.la/21590635.js"></script>
    </html>
HTML;
    echo $html;
}
?>