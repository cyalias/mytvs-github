<?php
$domain = $_SERVER['HTTP_HOST'];
$referer = isset($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : 'Direct access';

echo "您访问的域名是：{$domain}<br>";
echo "您的访问来源是：{$referer}";
?>