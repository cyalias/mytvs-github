# coding = utf-8
#!/usr/bin/python
# 新时代青年 2025.06.25 getApp第三版  后续平凡哥 七月大姐等大佬魔改 最后更新2026.01.14 增加特殊搜索签名模式
# 2026.01.15 增加搜索验证码自动和使用指定值功能
# 2026.01.17 优化外置签名逻辑：当signature_name和signature_value都为空时，不启用签名算法
# 修复：搜索请求中认证参数只放在header中，不在body中重复
# 2026.02.15 增加请求方法开关：可配置init请求使用GET或POST
# 2026.03.03 增加滑块验证功能：自动判断滑块验证，支持滑块+验证码组合验证
# 2026.03.04 增加验证码重试机制，支持外置配置重试次数

import re,sys,uuid,json,base64,urllib3,random,time,hashlib,requests
from Crypto.Cipher import AES
from base.spider import Spider
from Crypto.Util.Padding import pad,unpad
sys.path.append('..')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Spider(Spider):
    xurl,key,iv,init_data,search_verify = '','','','',''
    username, password, device_id = '', '', ''
    header = {}
    sort_rule = []
    playua = ''
    playcookie = ''
    playreferer = ''
    line_specific_settings = {}
    vip_duration = ''
    vip_config = {}
    enable_delay = False
    current_domain_index = 0
    available_domains = []
    
    host_ua = ''
    config_ua = ''
    home_ua = ''
    category_ua = ''
    search_ua = ''
    parse_ua = ''
    player_ua = ''
    
    auto_params_level = 0
    ext_timestamp = ''
    ext_sign = ''
    ext_android_id = ''
    ext_device_id = ''
    
    app_version_code = ''
    app_verify_sign = ''

    user_token = ''
    auth_token = ''

    login_timestamp = ''
    login_sign = ''
    login_device_id = ''
    login_uuid = ''

    category_sort_rule = []
    login_verify = False
    sign_mode = '1'  
    header_mode = 'simple'  
    custom_headers = {}
    search_suffix = 'searchList'  
    
    external_search_headers = {}
    
    external_sign_enabled = False  
    external_sign_name = ''       
    external_sign_value = ''       
    external_value_process = ''    
    external_algorithm_order = ''  
    external_sign_format = ''      
    external_request_order = ''    
    external_search_suffix = ''    
    
    init_api_suffix = 'initV119'  
    use_box_config = False  
    box_config_data = {}  
    box_api_headers = {}  
    box_search_suffix = ''  
    box_signature_name = ''  
    box_signature_value = ''
    
    search_captcha_auto_value = ''
    search_captcha_auto_mode = False
    
    init_request_method = 'GET'
    
    slider_id = ''
    slider_target_x = 0
    slider_attempted = False
    captcha_attempted = False
    temp_captcha_data = None
    captcha_retry_count = 0
    max_captcha_retries = 3

    def __init__(self):
        self.header = {'User-Agent': 'okhttp/3.14.9'}
        self.current_domain_index = 0
        self.available_domains = []
        self.login_timestamp = ''
        self.login_sign = ''
        self.login_device_id = ''
        self.login_uuid = ''
        self.category_sort_rule = []
        self.login_verify = False
        self.sign_mode = '1'  
        self.header_mode = 'simple'
        self.custom_headers = {}
        self.search_suffix = 'searchList'
        
        self.external_sign_enabled = False
        self.external_sign_name = ''
        self.external_sign_value = ''
        self.external_value_process = ''
        self.external_algorithm_order = ''
        self.external_sign_format = ''
        self.external_request_order = ''
        self.external_search_suffix = ''
        
        self.external_search_headers = {}
        self.init_api_suffix = 'initV119'
        self.use_box_config = False
        self.box_config_data = {}
        self.box_api_headers = {}
        self.box_search_suffix = ''
        self.box_signature_name = ''
        self.box_signature_value = ''
        
        self.search_captcha_auto_value = ''
        self.search_captcha_auto_mode = False
        
        self.init_request_method = 'GET'
        
        self.slider_id = ''
        self.slider_target_x = 0
        self.slider_attempted = False
        self.captcha_attempted = False
        self.temp_captcha_data = None
        self.captcha_retry_count = 0
        self.max_captcha_retries = 3

    def getName(self):
        return "首页"

    def init(self, extend=''):
        chinese_param_map = {
            '域名': 'host',
            '指定域名': 'host_index',
            '数据密钥': 'datakey',
            '数据向量': 'dataiv',
            '接口版本': 'api',
            '用户代理': 'ua',
            '设备标识': 'deviceid',
            '登录类型': 'login_type',
            '登录账号': 'username',
            '登录密码': 'password',
            '令牌': 'token',
            '认证令牌': 'auth_token',
            '用户id': 'user_id',
            '刷新令牌': 'refresh_token',
            '令牌过期': 'token_expire',
            'host': 'host',
            'host_index': 'host_index',
            'datakey': 'datakey',
            'dataiv': 'dataiv',
            'api': 'api',
            'ua': 'ua',
            'deviceid': 'deviceid',
            'login_type': 'login_type',
            'username': 'username',
            'password': 'password',
            'token': 'token',
            'auth_token': 'auth_token',
            'user_id': 'user_id',
            'refresh_token': 'refresh_token',
            'token_expire': 'token_expire',
            'appversioncode': 'app_version_code',
            'appverifySign': 'app_verify_sign',
            'AppVersionCode': 'app_version_code',
            'AppverifySign': 'app_verify_sign',
            '签名': 'sign',
            '时间戳': 'timestamp',
            '安卓ID': 'android_id',
            'app版本号': 'app_version_code',
            'app验证签名': 'app_verify_sign',
            'version': 'app_version_code',
            'Version': 'app_version_code',
            '版本': 'app_version_code',
            '分类排序': 'category_sort',
            '登录地址': 'login_url',
            '登录验证': 'login_verify',
            '签名模式': 'sign_mode',
            '请求头模式': 'header_mode',
            '请求头': 'header_mode',
            '自定义请求头': 'custom_headers',
            '自定义头': 'custom_headers',
            '搜索后缀': 'search_suffix',
            '搜索接口': 'search_suffix',
            'searchsuffix': 'search_suffix',
            'searchSuffix': 'search_suffix',
            '初始化后缀': 'init_suffix',
            'init后缀': 'init_suffix',
            'initSuffix': 'init_suffix',
            
            '启用搜索签名': 'external_sign',
            '搜索签名': 'external_sign',
            '外置签名值': 'external_sign_value',
            '密钥处理': 'external_value_process',
            '值处理方式': 'external_value_process',
            '第一层': 'external_value_process',
            '第1层': 'external_value_process',
            '算法顺序': 'external_algorithm_order',
            '第二层': 'external_algorithm_order',
            '第2层': 'external_algorithm_order',
            '算法输入': 'external_algorithm_order',
            '算法排序': 'external_algorithm_order',
            '签名格式': 'external_sign_format',
            '最终签名格式': 'external_sign_format',
            '请求顺序': 'external_request_order',
            '参数顺序': 'external_request_order',
            '第三层': 'external_request_order',
            '第3层': 'external_request_order',
            '外置搜索后缀': 'external_search_suffix',
            'external_sign': 'external_sign',
            'external_sign_value': 'external_sign_value',
            'external_value_process': 'external_value_process',
            'external_algorithm_order': 'external_algorithm_order',
            'external_sign_format': 'external_sign_format',
            'external_request_order': 'external_request_order',
            'external_search_suffix': 'external_search_suffix',
            
            '搜索自定义请求头': 'external_search_headers',
            '外置搜索请求头': 'external_search_headers',
            '搜索请求头': 'external_search_headers',
            'external_search_headers': 'external_search_headers',
            
            '搜索验证码': 'search_captcha_value',
            '搜索验证码自动': 'search_captcha_auto',
            'search_captcha_value': 'search_captcha_value',
            'search_captcha_auto': 'search_captcha_auto',
            
            '请求方法': 'init_method',
            'init_method': 'init_method',
            '初始化请求方法': 'init_method',
            
            '验证码重试次数': 'captcha_retry',
            'captcha_retry': 'captcha_retry',
            '验证码重试': 'captcha_retry'
        }
        
        ua_chinese_map = {
            '首页ua': 'homeua',
            '首页UA': 'homeua',
            '配置ua': 'configua',
            '配置UA': 'configua',
            '分类ua': 'categoryua',
            '分类UA': 'categoryua',
            '搜索ua': 'searchua',
            '搜索UA': 'searchua',
            '解析ua': 'parseua',
            '解析UA': 'parseua',
            '播放ua': 'playerua',
            '播放UA': 'playerua',
            'hostua': 'hostua',
            'hostUA': 'hostua',
            'configua': 'configua',
            'configUA': 'configua',
            'homeua': 'homeua',
            'homeUA': 'homeua',
            'categoryua': 'categoryua',
            'categoryUA': 'categoryua',
            'searchua': 'searchua',
            'searchUA': 'searchua',
            'parseua': 'parseua',
            'parseUA': 'parseua',
            'playerua': 'playerua',
            'playerUA': 'playerua'
        }
        
        ext = json.loads(extend.strip())
        
        english_ext = {}
        for key, value in ext.items():
            lower_key = key.lower()
            if lower_key in chinese_param_map:
                english_ext[chinese_param_map[lower_key]] = value
            elif key in ua_chinese_map:
                english_ext[ua_chinese_map[key]] = value
            else:
                english_ext[key] = value
        
        init_method_raw = english_ext.get('init_method', 'GET')
        if init_method_raw.upper() in ['GET', 'POST']:
            self.init_request_method = init_method_raw.upper()
        else:
            self.init_request_method = 'GET'
        
        host = english_ext['host']
        
        self.enable_delay = english_ext.get('延迟', english_ext.get('enable_delay', '0')) == '1'
        
        auto_params_str = english_ext.get('auto_params', english_ext.get('自动参数', '0'))
        try:
            self.auto_params_level = int(auto_params_str)
        except ValueError:
            self.auto_params_level = 0
        
        self.ext_timestamp = english_ext.get('timestamp', english_ext.get('时间戳', ''))
        self.ext_sign = english_ext.get('sign', english_ext.get('签名', ''))
        self.ext_android_id = english_ext.get('android_id', english_ext.get('安卓ID', ''))
        self.ext_device_id = english_ext.get('deviceid', english_ext.get('devideid', ''))
        
        app_version_raw = english_ext.get('app_version_code', english_ext.get('AppVersionCode', ''))
        self.app_version_code = self._format_version_code(app_version_raw) if app_version_raw else ''
        
        app_verify_raw = english_ext.get('app_verify_sign', english_ext.get('AppverifySign', ''))
        self.app_verify_sign = self._format_verify_sign(app_verify_raw) if app_verify_raw else ''
        
        self.sign_mode = english_ext.get('sign_mode', english_ext.get('签名模式', '1'))
        
        header_mode_raw = english_ext.get('header_mode', english_ext.get('请求头模式', english_ext.get('请求头', '简单')))
        if header_mode_raw in ['简单', '简易', 'simple']:
            self.header_mode = 'simple'
        elif header_mode_raw in ['完整', '完全', 'complete']:
            self.header_mode = 'complete'
        else:
            self.header_mode = 'simple'
        
        custom_headers_str = english_ext.get('custom_headers', english_ext.get('自定义请求头', ''))
        self.custom_headers = self._parse_custom_headers(custom_headers_str)
        
        search_suffix_raw = english_ext.get('search_suffix', 'searchList')
        self.search_suffix = str(search_suffix_raw).strip()
        if not self.search_suffix:
            self.search_suffix = 'searchList'
        
        init_suffix_raw = english_ext.get('init_suffix', '')
        if init_suffix_raw:
            self.init_api_suffix = str(init_suffix_raw).strip()
        else:
            self.init_api_suffix = self._determine_init_suffix(english_ext)
        
        external_search_headers_str = english_ext.get('external_search_headers', '')
        self.external_search_headers = self._parse_external_search_headers(external_search_headers_str)
        
        external_sign_raw = english_ext.get('external_sign', '0')
        self.external_sign_enabled = external_sign_raw == '1'
        
        search_captcha_value = english_ext.get('search_captcha_value', '')
        search_captcha_auto_raw = english_ext.get('search_captcha_auto', '0')
        
        self.search_captcha_auto_mode = search_captcha_auto_raw == '1'
        self.search_captcha_auto_value = search_captcha_value
        
        captcha_retry_raw = english_ext.get('captcha_retry', '3')
        try:
            self.max_captcha_retries = int(captcha_retry_raw)
        except ValueError:
            self.max_captcha_retries = 3
        
        if self.external_sign_enabled:
            self.external_sign_name = ''
            self.external_sign_value = english_ext.get('external_sign_value', '')
            self.external_value_process = english_ext.get('external_value_process', '')
            self.external_algorithm_order = english_ext.get('external_algorithm_order', '/{name}-{timestamp}-sb-0-{value}')
            self.external_sign_format = english_ext.get('external_sign_format', '{timestamp}-sb-0-{hash}')
            self.external_request_order = english_ext.get('external_request_order', 'keywords>type_id>{name}>page')
            self.external_search_suffix = english_ext.get('external_search_suffix', '')
            
            if self.external_search_suffix:
                self.search_suffix = self.external_search_suffix
        
        host_index_str = str(english_ext.get('host_index', '1')).strip()
        try:
            host_index = int(host_index_str) if host_index_str else 1
        except ValueError:
            host_index = 1
        
        self.available_domains = self._get_available_domains(host, host_index)
        if not self.available_domains:
            return
            
        host = self.available_domains[0]
        
        ua = english_ext.get('ua')
        if ua:
            self.header['User-Agent'] = ua
        else:
            api = english_ext.get('api', '/api.php/getappapi')
            if str(api) == '2' or '/api.php/qijiappapi' in str(api):
                self.header['User-Agent'] = 'okhttp/3.10.0'
            else:
                self.header['User-Agent'] = 'okhttp/3.14.9'
        
        self.host_ua = self._get_ua_param(english_ext, ['hostua', 'hostUA', '首页ua', '首页UA'])
        self.config_ua = self._get_ua_param(english_ext, ['configua', 'configUA', '配置ua', '配置UA'])
        self.home_ua = self._get_ua_param(english_ext, ['homeua', 'homeUA', '首页ua', '首页UA'])
        self.category_ua = self._get_ua_param(english_ext, ['categoryua', 'categoryUA', '分类ua', '分类UA'])
        self.search_ua = self._get_ua_param(english_ext, ['searchua', 'searchUA', '搜索ua', '搜索UA'])
        self.parse_ua = self._get_ua_param(english_ext, ['parseua', 'parseUA', '解析ua', '解析UA'])
        self.player_ua = self._get_ua_param(english_ext, ['playerua', 'playUA', '播放ua', '播放UA'])
        
        login_verify_str = english_ext.get('login_verify', english_ext.get('登录验证', '0'))
        self.login_verify = login_verify_str == '1'
        
        self.vip_config = {
            'type': english_ext.get('login_type', 'token'),
            'duration': english_ext.get('会员时长', ''),
            'username': english_ext.get('username', ''),
            'password': english_ext.get('password', ''),
            'token': english_ext.get('token', ''),
            'auth_token': english_ext.get('auth_token', ''),
            'user_id': english_ext.get('user_id', ''),
            'refresh_token': english_ext.get('refresh_token', ''),
            'token_expire': english_ext.get('token_expire', '0'),
            'login_url': english_ext.get('login_url', '')
        }
        
        self._handle_device_id_generation()
        
        if self.device_id:
            self.header['app-user-device-id'] = self.device_id
        
        api = english_ext.get('api', '/api.php/getappapi')
        if str(api) == '2':
            api = '/api.php/qijiappapi'
        self.xurl = host + api
        
        datakey = english_ext.get('datakey', '')
        dataiv = english_ext.get('dataiv', '')
        
        if datakey:
            self.key = datakey
            self.iv = dataiv if dataiv else datakey
        else:
            self.key = ''
            self.iv = ''
        
        sort_rule_str = english_ext.get('排序', '')
        if sort_rule_str:
            self.sort_rule = [s.strip().lower() for s in sort_rule_str.split('>')]
        else:
            self.sort_rule = []
        
        category_sort_str = english_ext.get('category_sort', english_ext.get('分类排序', ''))
        if category_sort_str:
            self.category_sort_rule = [s.strip() for s in category_sort_str.split('>')]
        else:
            self.category_sort_rule = []
        
        self._init_login()
        
        self._handle_vip_verification()
        
        self.playua = self._get_ua_param(english_ext, ['playua', 'playUA', '播放ua', '播放UA'], 'Dalvik/2.1.0 (Linux; U; Android 14; 23113RK12C Build/SKQ1.231004.001)')
        self.playcookie = self._get_param(english_ext, ['playcookie', 'playCookie', '播放cookie', '播放Cookie'], '')
        self.playreferer = self._get_param(english_ext, ['playreferer', 'playReferer', '播放referer', '播放Referer'], '')
        
        self.line_specific_settings = {}
        for key, value in english_ext.items():
            if key.startswith('line_'):
                line_key = key.replace('line_', '')
                if '|' in value:
                    parts = value.split('|', 1)
                    ua_part = ''
                    referer_part = ''
                    for part in parts:
                        part = part.strip()
                        if part:
                            if part.startswith('http://') or part.startswith('https://'):
                                referer_part = part
                            else:
                                ua_part = part
                    if line_key not in self.line_specific_settings:
                        self.line_specific_settings[line_key] = {}
                    if ua_part:
                        self.line_specific_settings[line_key]['ua'] = ua_part
                    if referer_part:
                        self.line_specific_settings[line_key]['referer'] = referer_part
                elif '_ua' in key or '_UA' in key:
                    line_name = key.replace('line_', '').replace('_ua', '').replace('_UA', '')
                    if line_name not in self.line_specific_settings:
                        self.line_specific_settings[line_name] = {}
                    self.line_specific_settings[line_name]['ua'] = value
                elif '_referer' in key or '_Referer' in key:
                    line_name = key.replace('line_', '').replace('_referer', '').replace('_Referer', '')
                    if line_name not in self.line_specific_settings:
                        self.line_specific_settings[line_name] = {}
                    self.line_specific_settings[line_name]['referer'] = value
                else:
                    if line_key not in self.line_specific_settings:
                        self.line_specific_settings[line_key] = {}
                    if value.startswith('http://') or value.startswith('https://'):
                        self.line_specific_settings[line_key]['referer'] = value
                    else:
                        self.line_specific_settings[line_key]['ua'] = value
        
        init_headers = self.header.copy()
        if self.config_ua:
            init_headers['User-Agent'] = self.config_ua
            
        init_payload = {}
        init_payload, init_headers = self._add_all_params_to_request(init_payload, init_headers)
        
        success = False
        for domain in self.available_domains:
            try:
                self.xurl = domain + api
                init_headers = self._build_headers(init_headers)
                init_url = f"{self.xurl}.index/{self.init_api_suffix}"
                
                if self.init_request_method == 'GET':
                    res = self.fetch(init_url, headers=init_headers, params=init_payload, verify=False)
                else:
                    res = self.post(init_url, headers=init_headers, data=init_payload, verify=False)
                
                if res.status_code != 200:
                    continue
                    
                res_data = res.json()
                encrypted_data = res_data['data']
                response = self.decrypt(encrypted_data)
                init_data = json.loads(response)
                
                if init_data:
                    self.init_data = init_data
                    self.search_verify = init_data['config'].get('system_search_verify_status', False)
                    success = True
                    
                    self._auto_extract_and_judge_signature()
                    
                    self._extract_search_captcha_config()
                    
                    break
            except Exception as e:
                continue
        
        if not success:
            pass

    def _extract_search_captcha_config(self):
        if not self.init_data:
            return
            
        if self.search_captcha_auto_mode and not self.search_captcha_auto_value:
            if 'hot_search_list' in self.init_data:
                hot_search_list = self.init_data.get('hot_search_list', [])
                for item in hot_search_list:
                    if isinstance(item, str) and '验证码' in item:
                        import re
                        captcha_patterns = [
                            r'验证码都是?(\d{4})',
                            r'验证码[:：]\s*(\d{4})',
                            r'验证码(\d{4})',
                            r'(\d{4})\s*验证码'
                        ]
                        for pattern in captcha_patterns:
                            match = re.search(pattern, item)
                            if match:
                                extracted_captcha = match.group(1)
                                if extracted_captcha and len(extracted_captcha) == 4 and extracted_captcha.isdigit():
                                    self.search_captcha_auto_value = extracted_captcha
                                    return
        
        if 'notice' in self.init_data:
            notice_data = self.init_data.get('notice', {})
            if isinstance(notice_data, dict):
                content_fields = ['content', 'intro', 'title']
                for field in content_fields:
                    if field in notice_data:
                        content = notice_data[field]
                        if content and self.search_captcha_auto_mode and not self.search_captcha_auto_value:
                            import re
                            clean_text = re.sub(r'<[^>]+>', ' ', content)
                            clean_text = re.sub(r'\s+', ' ', clean_text).strip()
                            captcha_patterns = [
                                r'验证码都是?(\d{4})',
                                r'验证码[:：]\s*(\d{4})',
                                r'验证码(\d{4})',
                                r'(\d{4})\s*验证码',
                                r'搜索.*?验证码.*?(\d{4})',
                                r'求片.*?验证码.*?(\d{4})',
                                r'反馈.*?验证码.*?(\d{4})'
                            ]
                            for pattern in captcha_patterns:
                                match = re.search(pattern, clean_text)
                                if match:
                                    extracted_captcha = match.group(1)
                                    if extracted_captcha and len(extracted_captcha) == 4 and extracted_captcha.isdigit():
                                        self.search_captcha_auto_value = extracted_captcha
                                        return
            elif isinstance(notice_data, str):
                if self.search_captcha_auto_mode and not self.search_captcha_auto_value:
                    import re
                    clean_text = re.sub(r'<[^>]+>', ' ', notice_data)
                    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
                    for pattern in [r'验证码都是?(\d{4})', r'验证码[:：]\s*(\d{4})', r'验证码(\d{4})']:
                        match = re.search(pattern, clean_text)
                        if match:
                            extracted_captcha = match.group(1)
                            if extracted_captcha and len(extracted_captcha) == 4 and extracted_captcha.isdigit():
                                self.search_captcha_auto_value = extracted_captcha
                                return
        
        if 'config' in self.init_data:
            config = self.init_data['config']
            if 'search_captcha' in config:
                search_captcha_config = config['search_captcha']
                if isinstance(search_captcha_config, str):
                    self.search_captcha_auto_value = search_captcha_config
                elif isinstance(search_captcha_config, dict):
                    self.search_captcha_auto_value = search_captcha_config.get('value', '')

    def _auto_extract_and_judge_signature(self):
        if self.external_sign_enabled and self.external_sign_value:
            return
        
        if not self.box_config_data and self.init_data and 'box_config' in self.init_data:
            self._process_box_config()
        
        if self.box_config_data:
            signature_name = self.box_config_data.get('signature_name', '')
            signature_value = self.box_config_data.get('signature_value', '')
            search_name = self.box_config_data.get('search_name', '')
            
            if search_name:
                self.external_search_suffix = search_name
            
            if signature_name and signature_value:
                if not self.external_sign_value:
                    self.external_sign_value = signature_value
                
                if not self.external_sign_name:
                    self.external_sign_name = signature_name
                
                self._auto_judge_signature_algorithm(signature_value)
                self.external_sign_enabled = True
            else:
                self.external_sign_enabled = False
                self.external_sign_name = ''
                self.external_sign_value = ''

    def _auto_judge_signature_algorithm(self, signature_value):
        if not signature_value:
            return
        
        length = len(signature_value)
        take_from_end = length - 8
        self.external_value_process = f'reverse+{take_from_end}+8'
        
        if not self.external_sign_enabled:
            self.external_sign_enabled = True
        
        if not self.external_sign_name and 'signature_name' in self.box_config_data:
            self.external_sign_name = self.box_config_data['signature_name']
        
        if not self.external_algorithm_order:
            self.external_algorithm_order = '/{name}-{timestamp}-sb-0-{value}'
        
        if not self.external_sign_format:
            self.external_sign_format = '{timestamp}-sb-0-{hash}'
        
        if not self.external_request_order:
            self.external_request_order = 'keywords>type_id>{name}>page'
        
        if not self.external_search_suffix and 'search_name' in self.box_config_data:
            self.external_search_suffix = self.box_config_data['search_name']

    def _universal_signature_processing(self, signature_value):
        if not signature_value:
            return ''
        
        length = len(signature_value)
        reversed_value = signature_value[::-1]
        
        if length < 8:
            return ''
        
        take_from_end = length - 8
        
        if take_from_end > 0:
            part_from_end = reversed_value[8:]
        else:
            part_from_end = ""
        
        part_from_start = reversed_value[:8]
        result = part_from_end + part_from_start
        
        return result

    def _process_signature_value_layer1(self, value):
        if not value:
            return ''
        
        if not self.external_value_process:
            self.external_value_process = self._get_signature_processing_mode()
        
        process_method = self.external_value_process
        if not process_method:
            process_method = 'reverse+8+8'
        
        if '+' in process_method:
            parts = process_method.split('+')
            
            if len(parts) == 3 and parts[0] == 'reverse' and parts[2] == '8':
                try:
                    expected_take_from_end = int(parts[1])
                    actual_length = len(value)
                    
                    if expected_take_from_end == actual_length - 8:
                        return self._universal_signature_processing(value)
                except ValueError:
                    pass
        
        try:
            parts = process_method.split('+')
            
            should_reverse = False
            if 'reverse' in parts[0].lower():
                should_reverse = True
                parts = parts[1:]
            
            if should_reverse:
                value = value[::-1]
            
            if not parts or parts[0] == 'full':
                return value
            
            if len(parts) >= 2:
                try:
                    part1_len = int(parts[0].strip())
                    part2_len = int(parts[1].strip())
                    
                    total_len = part1_len + part2_len
                    if len(value) >= total_len:
                        part1 = value[-part1_len:] if part1_len > 0 else ''
                        part2 = value[:part2_len] if part2_len > 0 else ''
                        result = part1 + part2
                        return result
                    else:
                        return value
                except ValueError:
                    pass
            
            if process_method == 'first8':
                result = value[:8] if len(value) >= 8 else value
                return result
            elif process_method == 'last8':
                result = value[-8:] if len(value) >= 8 else value
                return result
            elif process_method == 'middle8':
                if len(value) >= 16:
                    result = value[4:12]
                    return result
                else:
                    return value
            else:
                return self._universal_signature_processing(value if not should_reverse else value[::-1])
                
        except Exception:
            return self._universal_signature_processing(value)

    def _determine_init_suffix(self, english_ext):
        suffix = 'initV119'
        
        api = english_ext.get('api', '/api.php/getappapi')
        is_qijiapp = str(api) == '2' or '/api.php/qijiappapi' in str(api)
        
        external_sign_raw = english_ext.get('external_sign', '0')
        is_external_sign = external_sign_raw == '1'
        
        if is_external_sign:
            suffix = 'initV122'
        elif is_qijiapp:
            suffix = 'initV120'
        
        return suffix

    def _process_box_config(self):
        if not self.init_data or 'box_config' not in self.init_data:
            return
        
        encrypted_box = self.init_data['box_config']
        if not encrypted_box:
            return
        
        try:
            raw_key = self.key
            if not raw_key:
                return
            
            box_key = raw_key[::-1]
            key_md5 = hashlib.md5(box_key.encode()).hexdigest()
            box_iv = key_md5[:16]
            
            decrypted = self._decrypt_aes(encrypted_box, box_key, box_iv)
            if decrypted:
                self.box_config_data = json.loads(decrypted)
                self.use_box_config = True
                self._apply_box_config()
        except Exception:
            pass

    def _decrypt_aes(self, encrypted_b64, key_str, iv_str):
        try:
            key_bytes = key_str.encode('utf-8')
            iv_bytes = iv_str.encode('utf-8')
            
            if len(key_bytes) < 16:
                key_bytes = key_bytes.ljust(16, b'\x00')
            if len(iv_bytes) < 16:
                iv_bytes = iv_bytes.ljust(16, b'\x00')
            
            encrypted_data = base64.b64decode(encrypted_b64)
            cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
            decrypted_padded = cipher.decrypt(encrypted_data)
            decrypted = unpad(decrypted_padded, AES.block_size)
            return decrypted.decode('utf-8')
        except Exception:
            return None

    def _apply_box_config(self):
        if not self.box_config_data:
            return
        
        config = self.box_config_data
        
        if 'api_header' in config and isinstance(config['api_header'], dict):
            api_header = config['api_header']
            header_key = api_header.get('key', '')
            header_value = api_header.get('value', '')
            if header_key and header_value:
                self.box_api_headers[header_key] = header_value
        
        if 'search_name' in config:
            self.box_search_suffix = config['search_name']
            if not self.external_search_suffix:
                self.external_search_suffix = config['search_name']
        
        if 'signature_name' in config:
            self.external_sign_name = config['signature_name']
            self.box_signature_name = config['signature_name']
        
        if 'signature_value' in config:
            box_sig_value = config['signature_value']
            self.box_signature_value = box_sig_value
            
            signature_name = config.get('signature_name', '')
            if signature_name and box_sig_value:
                if not self.external_sign_value:
                    self.external_sign_value = box_sig_value

    def _parse_external_search_headers(self, headers_str):
        search_headers = {}
        if not headers_str:
            return search_headers
            
        try:
            if headers_str.strip().startswith('{'):
                headers_dict = json.loads(headers_str)
                for key, value in headers_dict.items():
                    if isinstance(value, (str, int, float)):
                        search_headers[str(key)] = str(value)
                return search_headers
            
            lines = []
            if '\n' in headers_str:
                lines = headers_str.split('\n')
            elif '$' in headers_str:
                lines = headers_str.split('$')
            else:
                lines = [headers_str]
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                found_separator = False
                for sep in [':', '=', '=>']:
                    if sep in line:
                        key_value = line.split(sep, 1)
                        if len(key_value) == 2:
                            key = key_value[0].strip()
                            value = key_value[1].strip()
                            if key and value:
                                if key.lower() == 'user-agent':
                                    key = 'User-Agent'
                                search_headers[key] = value
                                found_separator = True
                                break
                
                if not found_separator and line:
                    search_headers[line] = line
                    
        except Exception:
            pass
            
        return search_headers

    def _get_signature_processing_mode(self):
        if self.external_value_process:
            return self.external_value_process
        
        signature_value = self.external_sign_value or self.box_signature_value
        if signature_value:
            length = len(signature_value)
            take_from_end = length - 8
            auto_mode = f'reverse+{take_from_end}+8'
            return auto_mode
        
        return 'reverse+8+8'

    def _generate_external_signature_payload(self, keyword, page=1):
        try:
            if not self.external_sign_name or not self.external_sign_value:
                return {
                    'keywords': keyword,
                    'type_id': '0',
                    'page': str(page)
                }
            
            timestamp = str(int(time.time()))
            processed_value = self._process_signature_value_layer1(self.external_sign_value)
            final_signature = self._generate_signature_layer2(timestamp, processed_value, keyword, page)
            request_params = self._build_request_params_layer3(keyword, page, timestamp, final_signature)
            
            return request_params
            
        except Exception:
            return {
                'keywords': keyword,
                'type_id': '0',
                'page': str(page)
            }

    def _generate_signature_layer2(self, timestamp, processed_value, keyword, page):
        try:
            algorithm_template = self.external_algorithm_order
            if not algorithm_template:
                algorithm_template = '/{name}-{timestamp}-sb-0-{value}'
            
            algorithm_input = algorithm_template
            algorithm_input = algorithm_input.replace('{name}', self.external_sign_name)
            algorithm_input = algorithm_input.replace('{timestamp}', timestamp)
            algorithm_input = algorithm_input.replace('{value}', processed_value)
            algorithm_input = algorithm_input.replace('{salt}', 'sb-0')
            algorithm_input = algorithm_input.replace('{keywords}', keyword)
            algorithm_input = algorithm_input.replace('{page}', str(page))
            algorithm_input = algorithm_input.replace('{type_id}', '0')
            
            md5_hash = hashlib.md5(algorithm_input.encode()).hexdigest()
            
            sign_format = self.external_sign_format
            if not sign_format:
                sign_format = '{timestamp}-sb-0-{hash}'
            
            final_signature = sign_format
            final_signature = final_signature.replace('{timestamp}', timestamp)
            final_signature = final_signature.replace('{hash}', md5_hash)
            final_signature = final_signature.replace('{name}', self.external_sign_name)
            final_signature = final_signature.replace('{value}', processed_value)
            final_signature = final_signature.replace('{keywords}', keyword)
            final_signature = final_signature.replace('{page}', str(page))
            
            return final_signature
            
        except Exception:
            raise

    def _build_request_params_layer3(self, keyword, page, timestamp, final_signature):
        try:
            request_order = self.external_request_order
            if not request_order:
                request_order = 'keywords>type_id>{name}>page'
            
            param_names = request_order.split('>')
            request_params = {}
            
            for param in param_names:
                param = param.strip()
                if not param:
                    continue
                    
                if param == '{name}':
                    request_params[self.external_sign_name] = final_signature
                elif param == 'keywords':
                    request_params['keywords'] = keyword
                elif param == 'type_id':
                    request_params['type_id'] = '0'
                elif param == 'page':
                    request_params['page'] = str(page)
                elif param == self.external_sign_name:
                    request_params[self.external_sign_name] = final_signature
                elif param == 'timestamp':
                    request_params['timestamp'] = timestamp
                elif param == 'sign':
                    request_params['sign'] = final_signature
                elif param == 'signature':
                    request_params['signature'] = final_signature
                else:
                    if '=' in param:
                        key, value = param.split('=', 1)
                        request_params[key] = value
            
            return request_params
            
        except Exception:
            return {
                'keywords': keyword,
                'type_id': '0',
                'page': str(page),
                self.external_sign_name: final_signature
            }

    def get_slider_data(self):
        timestamp = str(int(time.time()))
        sign = self._generate_api_sign(timestamp)
        headers = self._build_headers()
        headers.update({
            'app-api-verify-time': timestamp,
            'app-api-verify-sign': sign,
            'Accept-Encoding': 'gzip',
            'app-ui-mode': 'light'
        })
        
        url = f"{self.xurl}.index/getSlider"
        
        try:
            session = requests.Session()
            response = session.get(url, headers=headers, verify=False, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('code') == 1 and 'data' in data:
                    encrypted_data = data['data']
                    decrypted = self.decrypt(encrypted_data)
                    if decrypted:
                        slider_data = json.loads(decrypted)
                        self.slider_id = slider_data.get('slider_id', '')
                        self.slider_target_x = slider_data.get('target_x', 0)
                        return slider_data
            return None
        except Exception as e:
            return None

    def verify_slider(self, slider_id, target_x):
        timestamp = str(int(time.time()))
        sign = self._generate_api_sign(timestamp)
        headers = self._build_headers()
        headers.update({
            'app-api-verify-time': timestamp,
            'app-api-verify-sign': sign,
            'Accept-Encoding': 'gzip',
            'app-ui-mode': 'light'
        })
        
        url = f"{self.xurl}.index/verifySlider"
        
        data = {
            "slider_id": slider_id,
            "pos_x": target_x,
            "timestamp": timestamp
        }
        
        try:
            session = requests.Session()
            response = session.post(url, headers=headers, data=data, verify=False, timeout=10)
            if response.status_code == 200:
                result = response.json()
                if result.get('code') == 1 and '成功' in result.get('msg', ''):
                    return True
            return False
        except Exception as e:
            return False

    def reset_verification_flags(self):
        self.slider_attempted = False
        self.captcha_attempted = False
        self.temp_captcha_data = None
        self.captcha_retry_count = 0

    def get_search_verification_code(self):
        random_uuid = str(uuid.uuid4())
        
        if self.search_captcha_auto_mode or self.search_captcha_auto_value:
            try:
                self.fetch(f'{self.xurl}.verify/create?key={random_uuid}', 
                          headers=self.header, verify=False)
            except Exception:
                pass
            
            if self.search_captcha_auto_value:
                return {
                    'uuid': random_uuid,
                    'code': self.search_captcha_auto_value
                }
            elif self.search_captcha_auto_mode:
                return self.verification()
            else:
                return None
        else:
            return self.verification()

    def add_captcha_to_payload(self, payload, verification_data):
        if not verification_data:
            return payload
        
        payload['code'] = verification_data['code']
        payload['key'] = verification_data['uuid']
        payload['captcha'] = verification_data['code']
        payload['captcha_key'] = verification_data['uuid']
        
        return payload

    def searchContent(self, key, quick, pg=1):
        self.reset_verification_flags()
        max_attempts = 10
        attempt = 0
        
        while attempt < max_attempts:
            attempt += 1
            headers = self.header.copy()
            
            if self.search_ua:
                headers['User-Agent'] = self.search_ua
            
            if self.external_search_headers:
                for key_name, value in self.external_search_headers.items():
                    headers[key_name] = value
            
            if self.use_box_config and self.box_api_headers:
                for header_key, header_value in self.box_api_headers.items():
                    headers[header_key] = header_value
            
            videos = []
            
            has_valid_signature = (self.external_sign_name and self.external_sign_value)
            
            search_suffix_to_use = self.search_suffix
            
            if self.external_search_suffix:
                search_suffix_to_use = self.external_search_suffix
            elif self.use_box_config and self.box_search_suffix:
                search_suffix_to_use = self.box_search_suffix
            
            if has_valid_signature:
                payload = self._generate_external_signature_payload(key, pg)
            else:
                if 'xiaohys.com' in self.xurl:
                    host = self.xurl.split('api.php')[0]
                    data = self.fetch(f'{host}index.php/ajax/suggest?mid=1&wd={key}').json()
                    for i in data['list']:
                        videos.append({
                            "vod_id": i['id'],
                            "vod_name": i['name'],
                            "vod_pic": i.get('pic')
                        })
                    return {'list': videos, 'page': pg, 'pagecount': 9999, 'limit': 90, 'total': 999999}
                
                payload = {
                    'keywords': key,
                    'type_id': "0",
                    'page': str(pg)
                }
            
            if self.temp_captcha_data:
                payload = self.add_captcha_to_payload(payload, self.temp_captcha_data)
                self.temp_captcha_data = None
            
            headers = self._add_all_params_to_search_request(headers)
            
            url = f'{self.xurl}.index/{search_suffix_to_use}'
            
            try:
                response = self.post(url=url, data=payload, headers=headers, verify=False)
                res = response.json()
                
                need_slider = False
                need_captcha = False
                msg = res.get('msg', '')
                
                if res.get('code') == 1001 and res.get('need_slider'):
                    need_slider = True
                elif res.get('code') == 1002:
                    need_captcha = True
                elif res.get('code') == 0:
                    if '滑块' in msg:
                        need_slider = True
                    if '验证码' in msg:
                        need_captcha = True
                
                if need_slider or need_captcha:
                    if need_slider:
                        if self.slider_attempted:
                            return {'list':[], 'msg': f'滑块验证失败: {msg}'}
                        
                        self.slider_attempted = True
                        slider_data = self.get_slider_data()
                        if not slider_data or not slider_data.get('slider_id') or not slider_data.get('target_x'):
                            return {'list':[], 'msg': '获取滑块数据失败'}
                        
                        slider_id = slider_data.get('slider_id')
                        target_x = slider_data.get('target_x')
                        
                        if self.verify_slider(slider_id, target_x):
                            continue
                        else:
                            return {'list':[], 'msg': '滑块验证失败'}
                    
                    if need_captcha:
                        if self.captcha_attempted:
                            if self.captcha_retry_count < self.max_captcha_retries:
                                self.captcha_retry_count += 1
                                new_captcha = self.get_search_verification_code()
                                if new_captcha:
                                    self.temp_captcha_data = new_captcha
                                    continue
                            return {'list':[], 'msg': f'验证码错误，已重试{self.captcha_retry_count}次: {msg}'}
                        
                        self.captcha_attempted = True
                        captcha_data = self.get_search_verification_code()
                        if not captcha_data:
                            return {'list':[], 'msg': '获取验证码失败'}
                        
                        self.temp_captcha_data = captcha_data
                        continue
                
                if not res.get('data'):
                    return {'list':[], 'msg': res.get('msg', '搜索失败')}
                    
                encrypted_data = res['data']
                kjson = self.decrypt(encrypted_data)
                kjson1 = json.loads(kjson)
                
                for i in kjson1.get('search_list', []):
                    id = i['vod_id']
                    name = i['vod_name']
                    pic = i['vod_pic']
                    remarks = i.get('vod_year', '') + ' ' + i.get('vod_class', '')
                    videos.append({
                        "vod_id": id,
                        "vod_name": name,
                        "vod_pic": pic,
                        "vod_remarks": remarks
                    })
                    
                return {'list': videos, 'page': pg, 'pagecount': 9999, 'limit': 90, 'total': 999999}
                
            except Exception as e:
                continue
        
        return {'list':[], 'msg': '搜索失败，多次尝试后无法完成验证'}

    def _add_all_params_to_search_request(self, headers=None):
        if headers is None:
            headers = self.header.copy()
        
        headers = self._add_search_auth_headers(headers)
        headers = self._add_app_params_to_headers(headers)
        
        return headers
    
    def _add_search_auth_headers(self, headers):
        if self.ext_device_id:
            self.device_id = self.ext_device_id
            headers['app-user-device-id'] = self.device_id
        elif self.device_id:
            headers['app-user-device-id'] = self.device_id
        
        has_external_ts = bool(self.ext_timestamp)
        has_external_sign = bool(self.ext_sign)
        
        if has_external_ts or has_external_sign:
            if self.ext_timestamp:
                timestamp = self.ext_timestamp
            else:
                timestamp = str(int(time.time()))
            
            if self.ext_sign:
                sign = self.ext_sign
            else:
                sign = self._generate_api_sign(timestamp)
            
            headers.update({
                'app-api-verify-time': timestamp,
                'app-api-verify-sign': sign,
                'Accept-Encoding': "gzip",
                'app-ui-mode': "light"
            })
        
        if self.ext_android_id:
            headers['app-android-id'] = self.ext_android_id
        
        return headers

    def _parse_custom_headers(self, headers_str):
        custom_headers = {}
        if not headers_str:
            return custom_headers
            
        try:
            if headers_str.strip().startswith('{'):
                headers_dict = json.loads(headers_str)
                for key, value in headers_dict.items():
                    if isinstance(value, (str, int, float)):
                        custom_headers[str(key)] = str(value)
            else:
                lines = headers_str.split('\n')
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    
                    for sep in [':', '=', '=>']:
                        if sep in line:
                            parts = line.split(sep, 1)
                            if len(parts) == 2:
                                key = parts[0].strip()
                                value = parts[1].strip()
                                if key and value:
                                    custom_headers[key] = value
                                break
        except Exception:
            pass
            
        return custom_headers

    def _build_simple_headers(self, headers=None):
        if headers is None:
            headers = self.header.copy()
        
        base_headers = {
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive',
        }
        
        for key, value in base_headers.items():
            key_exists = False
            for existing_key in headers.keys():
                if existing_key.lower() == key.lower():
                    key_exists = True
                    break
            if not key_exists:
                headers[key] = value
        
        if self.app_version_code:
            headers['app-version-code'] = self.app_version_code
            
        if self.app_verify_sign:
            headers['app-verify-sign'] = self.app_verify_sign
        
        if self.device_id:
            headers['app-user-device-id'] = self.device_id
            
        if self.user_token:
            headers['app-user-token'] = self.user_token
        elif self.auth_token:
            headers['app-user-token'] = self.auth_token
            
        if self.ext_timestamp:
            headers['app-api-verify-time'] = self.ext_timestamp
        if self.ext_sign:
            headers['app-api-verify-sign'] = self.ext_sign
            
        return headers

    def _build_complete_headers(self, headers=None):
        if headers is None:
            headers = self.header.copy()
            
        base_headers = {
            'Accept-Encoding': 'gzip',
            'User-Agent': self.header.get('User-Agent', 'okhttp/3.14.9'),
            'app-ui-mode': 'light'
        }
        
        for key, value in base_headers.items():
            key_exists = False
            for existing_key in headers.keys():
                if existing_key.lower() == key.lower():
                    key_exists = True
                    break
            if not key_exists:
                headers[key] = value
        
        if self.app_version_code:
            headers['app-version-code'] = self.app_version_code
            
        if self.app_verify_sign:
            headers['app-verify-sign'] = self.app_verify_sign
            
        if self.device_id:
            headers['app-user-device-id'] = self.device_id
            
        if self.user_token:
            headers['app-user-token'] = self.user_token
        elif self.auth_token:
            headers['app-user-token'] = self.auth_token
            
        if self.ext_timestamp:
            headers['app-api-verify-time'] = self.ext_timestamp
        if self.ext_sign:
            headers['app-api-verify-sign'] = self.ext_sign
            
        return headers

    def _build_headers(self, headers=None):
        base_headers = self.header.copy()
        
        if headers is not None:
            base_headers.update(headers)
        
        if self.header_mode == 'complete':
            base_headers = self._build_complete_headers(base_headers)
        else:
            base_headers = self._build_simple_headers(base_headers)
        
        if self.custom_headers:
            protected_headers = [
                'User-Agent', 'user-agent',
                'app-version-code', 'app-verify-sign',
                'app-user-token', 'app-user-device-id',
                'app-api-verify-time', 'app-api-verify-sign',
                'app-android-id'
            ]
            
            custom_copy = self.custom_headers.copy()
            
            for protected in protected_headers:
                if protected in base_headers:
                    custom_copy.pop(protected, None)
                    protected_variants = [protected.lower(), protected.upper(), protected.title()]
                    for variant in protected_variants:
                        custom_copy.pop(variant, None)
            
            base_headers.update(custom_copy)
        
        return base_headers

    def _init_login(self):
        if self.vip_config['type'] == 'login' and self.vip_config['username'] and self.vip_config['password']:
            success = self.login()
            if success:
                return True
        
        if self.vip_config.get('token'):
            self.header['app-user-token'] = self.vip_config['token']
            self.user_token = self.vip_config['token']
            return True
            
        if self.vip_config.get('auth_token'):
            self.header['app-user-token'] = self.vip_config['auth_token']
            self.auth_token = self.vip_config['auth_token']
            return True
                
        return False

    def _generate_aes_timestamp_signature(self, timestamp):
        if self.ext_sign:
            return self.ext_sign
            
        if not self.key:
            return ''
            
        try:
            key_bytes = self.key.encode('utf-8')
            iv_bytes = self.iv.encode('utf-8')
            
            if len(key_bytes) < 16:
                key_bytes = key_bytes.ljust(16, b'\x00')
            else:
                key_bytes = key_bytes[:16]
                
            if len(iv_bytes) < 16:
                iv_bytes = iv_bytes.ljust(16, b'\x00')
            else:
                iv_bytes = iv_bytes[:16]
            
            cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
            data = pad(timestamp.encode('utf-8'), AES.block_size)
            encrypted = cipher.encrypt(data)
            
            return base64.b64encode(encrypted).decode('utf-8')
            
        except Exception:
            return ''

    def _generate_api_sign(self, timestamp):
        if self.ext_sign:
            return self.ext_sign
            
        if not timestamp:
            return ''
            
        if self.sign_mode == '2' or self.sign_mode.lower() == 'aes':
            return self._generate_aes_timestamp_signature(timestamp)
        
        sign_data = f"{timestamp}"
        sign_hash = hashlib.md5(sign_data.encode()).digest()
        sign = base64.b64encode(sign_hash).decode()
        return sign

    def _format_version_code(self, version_raw):
        if not version_raw:
            return ''
        
        version_clean = re.sub(r'[^\d]', '', str(version_raw))
        
        if not version_clean:
            return ''
            
        if len(version_clean) > 4:
            version_clean = version_clean[:4]
            
        return version_clean

    def _format_verify_sign(self, verify_raw):
        if not verify_raw:
            return ''
        
        verify_str = str(verify_raw).strip()
        if verify_str.endswith('.'):
            verify_str = verify_str[:-1]
            
        return verify_str

    def _add_all_params_to_request(self, payload=None, headers=None):
        if headers is None:
            headers = self.header.copy()
        if payload is None:
            payload = {}
            
        headers, payload = self._add_external_params_to_request(headers, payload)
        payload, headers = self._add_auto_params_to_request(payload, headers)
        headers = self._add_app_params_to_headers(headers)
        
        return payload, headers

    def _add_external_params_to_request(self, headers, payload):
        if self.ext_device_id:
            self.device_id = self.ext_device_id
            headers['app-user-device-id'] = self.device_id
            if payload is not None:
                payload['device_id'] = self.device_id
        elif self.device_id:
            headers['app-user-device-id'] = self.device_id
            if payload is not None:
                payload['device_id'] = self.device_id
        
        has_external_ts = bool(self.ext_timestamp)
        has_external_sign = bool(self.ext_sign)
        
        if has_external_ts or has_external_sign:
            if self.ext_timestamp:
                timestamp = self.ext_timestamp
            else:
                timestamp = str(int(time.time()))
            
            if self.ext_sign:
                sign = self.ext_sign
            else:
                sign = self._generate_api_sign(timestamp)
            
            headers.update({
                'app-api-verify-time': timestamp,
                'app-api-verify-sign': sign,
                'Accept-Encoding': "gzip",
                'app-ui-mode': "light"
            })
            if payload is not None:
                payload.update({
                    'timestamp': timestamp,
                    'sign': sign
                })
        
        if self.ext_android_id:
            headers['app-android-id'] = self.ext_android_id
            if payload is not None:
                payload['android_id'] = self.ext_android_id
        
        return headers, payload

    def _add_app_params_to_headers(self, headers):
        if self.app_version_code:
            headers['app-version-code'] = self.app_version_code
        
        if self.app_verify_sign:
            headers['app-verify-sign'] = self.app_verify_sign
            
        return headers

    def _get_available_domains(self, host, host_index=1):
        domains = []
        
        if re.match(r'^https?:\/\/[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(:\d+)?(\/)?$', host):
            domains.append(host.rstrip('/'))
            return domains
        
        try:
            response = self.fetch(host, headers=self.header, timeout=10, verify=False)
            text = response.text.strip()
            
            domain_lines = [line.strip() for line in text.splitlines() if line.strip()]
            
            for line in domain_lines:
                domain = line.rstrip('/')
                if not domain.startswith(('http://', 'https://')):
                    domain = 'https://' + domain
                domains.append(domain)
                
            if domains:
                try:
                    index = host_index - 1
                    if 0 <= index < len(domains):
                        selected_domain = domains[index]
                        return [selected_domain]
                    else:
                        return [domains[0]]
                except ValueError:
                    return [domains[0]]
            else:
                return []
                
        except Exception:
            return []

    def _switch_domain(self):
        if len(self.available_domains) <= 1:
            return False
            
        self.current_domain_index = (self.current_domain_index + 1) % len(self.available_domains)
        new_domain = self.available_domains[self.current_domain_index]
        
        api = self.xurl.split('/api.php')[1] if '/api.php' in self.xurl else '/api.php/getappapi'
        self.xurl = new_domain + api
        
        return True

    def _handle_device_id_generation(self):
        if self.ext_device_id:
            return
        
        if self.auto_params_level >= 1:
            self.device_id = str(uuid.uuid4()).replace('-', '')
        else:
            self.device_id = ''

    def _get_ua_param(self, ext, param_names, default=''):
        for name in param_names:
            value = ext.get(name)
            if value:
                return value
        return default

    def _get_param(self, ext, param_names, default=''):
        for name in param_names:
            value = ext.get(name)
            if value:
                return value
        return default

    def _apply_request_delay(self):
        if self.enable_delay:
            delay_time = random.uniform(1, 3)
            time.sleep(delay_time)

    def fetch(self, url, **kwargs):
        if 'playerContent' not in sys._getframe(2).f_code.co_name:
            self._apply_request_delay()
        
        max_retries = 2
        response = None
        for retry in range(max_retries + 1):
            try:
                if 'headers' in kwargs:
                    kwargs['headers'] = self._build_headers(kwargs['headers'])
                else:
                    kwargs['headers'] = self._build_headers()
                
                response = super().fetch(url, **kwargs)
                if response.status_code == 200:
                    return response
                elif response.status_code >= 500 and retry < max_retries:
                    self._switch_domain()
                    time.sleep(1)
            except Exception as e:
                if retry < max_retries:
                    self._switch_domain()
                    time.sleep(1)
                else:
                    raise e
        return response

    def post(self, url, **kwargs):
        if 'playerContent' not in sys._getframe(2).f_code.co_name:
            self._apply_request_delay()
        
        max_retries = 2
        response = None
        for retry in range(max_retries + 1):
            try:
                if 'headers' in kwargs:
                    kwargs['headers'] = self._build_headers(kwargs['headers'])
                else:
                    kwargs['headers'] = self._build_headers()
                
                response = super().post(url, **kwargs)
                if response.status_code == 200:
                    return response
                elif response.status_code >= 500 and retry < max_retries:
                    self._switch_domain()
                    time.sleep(1)
            except Exception as e:
                if retry < max_retries:
                    self._switch_domain()
                    time.sleep(1)
                else:
                    raise e
        return response

    def get(self, url, **kwargs):
        if 'playerContent' not in sys._getframe(2).f_code.co_name:
            self._apply_request_delay()
        
        max_retries = 2
        response = None
        for retry in range(max_retries + 1):
            try:
                if 'headers' in kwargs:
                    kwargs['headers'] = self._build_headers(kwargs['headers'])
                else:
                    kwargs['headers'] = self._build_headers()
                
                response = super().get(url, **kwargs)
                if response.status_code == 200:
                    return response
                elif response.status_code >= 500 and retry < max_retries:
                    self._switch_domain()
                    time.sleep(1)
            except Exception as e:
                if retry < max_retries:
                    self._switch_domain()
                    time.sleep(1)
                else:
                    raise e
        return response

    def _handle_vip_verification(self):
        vip_type = self.vip_config['type']
        
        if vip_type == 'token':
            if self.vip_config['token']:
                self.header['app-user-token'] = self.vip_config['token']
                self.user_token = self.vip_config['token']
                self.vip_duration = self.vip_config['duration']
            else:
                self.vip_duration = ''
        
        elif vip_type == 'login':
            if self.vip_config['username'] and self.vip_config['password']:
                if not (self.user_token or self.auth_token):
                    self.vip_duration = ''
                else:
                    self.vip_duration = self.vip_config['duration']
            else:
                self.vip_duration = ''
        
        else:
            self.vip_duration = ''

    def get_login_verification(self, verify_url):
        try:
            verify_payload = {
                'device_id': self.login_device_id,
                'timestamp': self.login_timestamp,
                'sign': self.login_sign,
                'key': self.login_uuid
            }
            
            verify_headers = self._build_headers()
            
            response = self.fetch(verify_url, headers=verify_headers, params=verify_payload, verify=False)
            
            if response.status_code == 200:
                return response.content
            else:
                return None
                
        except Exception:
            return None

    def login(self):
        try:
            if not self.vip_config['username'] or not self.vip_config['password']:
                return False
                
            if self.ext_device_id:
                self.login_uuid = self.ext_device_id
            else:
                self.login_uuid = str(uuid.uuid4())
            
            self.login_device_id = self.device_id
            
            if self.ext_timestamp:
                self.login_timestamp = self.ext_timestamp
            elif self.ext_device_id or self.auto_params_level >= 1:
                self.login_timestamp = str(int(time.time()))
            else:
                self.login_timestamp = ''
            
            if self.ext_sign:
                self.login_sign = self.ext_sign
            elif self.ext_device_id or self.auto_params_level >= 1:
                if self.login_timestamp:
                    self.login_sign = self._generate_api_sign(self.login_timestamp)
                else:
                    self.login_sign = ''
            else:
                self.login_sign = ''
            
            payload = {
                'password': self.vip_config['password'],
                'code': "",
                'device_id': self.login_device_id,
                'user_name': self.vip_config['username'],
                'invite_code': "",
                'is_emulator': "0",
                'timestamp': self.login_timestamp,
                'sign': self.login_sign,
                'version': '1.0.0',
                'platform': 'android',
                'key': self.login_uuid
            }
            
            if not (self.ext_device_id or self.auto_params_level >= 1):
                if 'timestamp' in payload:
                    del payload['timestamp']
                if 'sign' in payload:
                    del payload['sign']
            
            if self.vip_config.get('login_url'):
                login_url = self.vip_config['login_url']
                if '.index/' in login_url:
                    base_verify_url = login_url.split('.index/')[0]
                else:
                    base_verify_url = login_url.rsplit('/', 1)[0]
            else:
                base_verify_url = self.xurl
                login_url = f'{self.xurl}.index/appLogin'
        
            verify_url = f"{base_verify_url}.verify/create"
            
            if self.login_verify:
                dat = self.get_login_verification(verify_url)
                if not dat:
                    return False
                    
                base64_img = base64.b64encode(dat).decode('utf-8')
                code = self.ocr(base64_img)
                if not code:
                    return False
                    
                code = self.replace_code(code)
                if not (len(code) == 4 and code.isdigit()):
                    return False
                    
                payload['code'] = code
        
            headers = self._build_headers()
            headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
            
            response = self.post(login_url, data=payload, headers=headers, verify=False)
            
            if response.status_code == 200:
                response_data = response.json()
                
                if not self.login_verify and response_data.get('code') == 0 and '验证码' in response_data.get('msg', ''):
                    dat = self.get_login_verification(verify_url)
                    if not dat:
                        return False
                        
                    base64_img = base64.b64encode(dat).decode('utf-8')
                    code = self.ocr(base64_img)
                    if not code:
                        return False
                        
                    code = self.replace_code(code)
                    if not (len(code) == 4 and code.isdigit()):
                        return False
                    
                    payload['code'] = code
                    
                    response = self.post(login_url, data=payload, headers=headers, verify=False)
                    
                    if response.status_code == 200:
                        response_data = response.json()
                    else:
                        return False
                
                if response_data.get('code') == 1:
                    encrypted_data = response_data['data']
                    decrypted_data = self.decrypt(encrypted_data)
                    user_info = json.loads(decrypted_data)
                    
                    if 'user' in user_info and 'auth_token' in user_info['user']:
                        auth_token = user_info['user']['auth_token']
                        self.header['app-user-token'] = auth_token
                        self.user_token = auth_token
                        self.auth_token = auth_token
                        
                        user_id = user_info['user'].get('user_id', '')
                        vip_days = user_info['user'].get('vip_days', 0)
                        
                        vip_data = {
                            'user_id': user_id,
                            'auth_token': auth_token,
                            'vip_days': vip_days,
                            'login_time': int(time.time()),
                            'is_vip': user_info['user'].get('is_vip', False)
                        }
                        self.vip_duration = base64.b64encode(json.dumps(vip_data).encode()).decode()
                        
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
                
        except Exception:
            return False

    def homeContent(self, filter):
        kjson = self.init_data
        result = {"class": [], "filters": {}}
        
        all_categories = []
        for i in kjson['type_list']:
            if not(i['type_name'] in {'全部', 'QQ', 'juo.one'} or '企鹅群' in i['type_name']):
                all_categories.append({
                    "type_id": i['type_id'],
                    "type_name": i['type_name']
                })
        
        if self.category_sort_rule:
            def category_sort_key(item):
                type_name = item['type_name']
                
                for idx, rule in enumerate(self.category_sort_rule):
                    if rule == type_name:
                        return idx
                
                for idx, rule in enumerate(self.category_sort_rule):
                    if rule in type_name or type_name in rule:
                        return idx + 100
                
                return 999 + hash(type_name) % 100
            
            all_categories.sort(key=category_sort_key)
        
        result['class'] = all_categories
        
        name_mapping = {'class': '类型', 'area': '地区', 'lang': '语言', 'year': '年份', 'sort': '排序'}
        for i in kjson['type_list']:
            filter_items = []
            for filter_type in i.get('filter_type_list', []):
                filter_name = filter_type.get('name')
                values = filter_type.get('list', [])
                if not values:
                    continue
                value_list = [{"n": value, "v": value} for value in values]
                display_name = name_mapping.get(filter_name, filter_name)
                key = 'by' if filter_name == 'sort' else filter_name
                filter_items.append({
                    "key": key,
                    "name": display_name,
                    "value": value_list
                })
            type_id = i.get('type_id')
            if filter_items:
                result["filters"][str(type_id)] = filter_items
                
        return result

    def homeVideoContent(self):
        headers = self.header.copy()
        if self.home_ua:
            headers['User-Agent'] = self.home_ua
            
        videos = []
        kjson = self.init_data
        for i in kjson['type_list']:
            for item in i['recommend_list']:
                vod_id = item['vod_id']
                name = item['vod_name']
                pic = item['vod_pic']
                remarks = item['vod_remarks']
                video = {
                    "vod_id": vod_id,
                    "vod_name": name,
                    "vod_pic": pic,
                    "vod_remarks": remarks
                }
                videos.append(video)
        return {'list': videos}

    def categoryContent(self, cid, pg, filter, ext):
        headers = self.header.copy()
        if self.category_ua:
            headers['User-Agent'] = self.category_ua
            
        videos = []
        payload = {
            'area': ext.get('area','全部'),
            'year': ext.get('year','全部'),
            'type_id': cid,
            'page': str(pg),
            'sort': ext.get('sort','最新'),
            'lang': ext.get('lang','全部'),
            'class': ext.get('class','全部')
        }
        
        payload, headers = self._add_all_params_to_request(payload, headers)
        
        url = f'{self.xurl}.index/typeFilterVodList'
        res = self.post(url=url, headers=headers, data=payload, verify=False).json()
        encrypted_data = res['data']
        kjson = self.decrypt(encrypted_data)
        kjson1 = json.loads(kjson)
        for i in kjson1['recommend_list']:
            id = i['vod_id']
            name = i['vod_name']
            pic = i['vod_pic']
            remarks = i['vod_remarks']
            video = {
                "vod_id": id,
                "vod_name": name,
                "vod_pic": pic,
                "vod_remarks": remarks
            }
            videos.append(video)
        return {'list': videos, 'page': pg, 'pagecount': 9999, 'limit': 90, 'total': 999999}

    def detailContent(self, ids):
        did = ids[0]
        payload = {'vod_id': did}
        
        payload, headers = self._add_all_params_to_request(payload)
        
        api_endpoints = ['vodDetail', 'vodDetail2']

        for endpoint in api_endpoints:
            url = f'{self.xurl}.index/{endpoint}'
            response = self.post(url=url, headers=headers, data=payload, verify=False)

            if response.status_code == 200:
                response_data = response.json()
                if '到期' in response_data.get('msg', '') or response_data.get('code', 1) == 0:
                    return None
                encrypted_data = response_data['data']
                kjson1 = self.decrypt(encrypted_data)
                kjson = json.loads(kjson1)
                break
        
        videos = []
        play_form = ''
        play_url = ''
        lineid = 1
        name_count = {}
        
        if self.sort_rule:
            def sort_key(line):
                line_name = line['player_info']['show'].lower()
                for idx, rule in enumerate(self.sort_rule):
                    if rule in line_name:
                        return idx
                return len(self.sort_rule)
            kjson['vod_play_list'].sort(key=sort_key)
        
        for line in kjson['vod_play_list']:
            keywords = {'防走丢', '群', '防失群', '官网'}
            player_show = line['player_info']['show']
            if any(keyword in player_show for keyword in keywords):
                import re
                match = re.search(r'^([a-zA-Z0-9\u4e00-\u9fa5]+)', player_show)
                if match:
                    new_name = match.group(1)
                else:
                    new_name = f'{lineid}线'
                line['player_info']['show'] = new_name
                player_show = new_name
            count = name_count.get(player_show, 0) + 1
            name_count[player_show] = count
            if count > 1:
                line['player_info']['show'] = f"{player_show}{count}"
            play_form += line['player_info']['show'] + '$$$'
            parse = line['player_info']['parse']
            parse_type = line['player_info']['parse_type']
            player_parse_type = line['player_info']['player_parse_type']
            kurls = ""
            for vod in line['urls']:
                token = 'token+' + vod['token']
                kurls += f"{str(vod['name'])}${parse},{vod['url']},{token},{player_parse_type},{parse_type}#"
            kurls = kurls.rstrip('#')
            play_url += kurls + '$$$'
            lineid += 1
        
        play_form = play_form.rstrip('$$$')
        play_url = play_url.rstrip('$$$')
        videos.append({
            "vod_id": did,
            "vod_name": kjson['vod']['vod_name'],
            "vod_actor": kjson['vod']['vod_actor'].replace('演员', ''),
            "vod_director": kjson['vod'].get('vod_director', '').replace('导演', ''),
            "vod_content": kjson['vod']['vod_content'],
            "vod_remarks": kjson['vod']['vod_remarks'],
            "vod_year": kjson['vod']['vod_year'] + '年',
            "vod_area": kjson['vod']['vod_area'],
            "vod_play_from": play_form,
            "vod_play_url": play_url
        })
        return {'list': videos}

    def playerContent(self, flag, id, vipFlags):
        line_name = flag
        play_header = {'User-Agent': self.player_ua or self.playua}
        
        line_settings = self.line_specific_settings.get(line_name, {})
        
        if 'ua' in line_settings:
            play_header['User-Agent'] = line_settings['ua']
        else:
            for line_key, settings in self.line_specific_settings.items():
                if line_key in line_name or line_name in line_key:
                    if 'ua' in settings:
                        play_header['User-Agent'] = settings['ua']
                    break
        
        if 'referer' in line_settings:
            play_header['Referer'] = line_settings['referer']
        else:
            for line_key, settings in self.line_specific_settings.items():
                if line_key in line_name or line_name in line_key:
                    if 'referer' in settings:
                        play_header['Referer'] = settings['referer']
                    break
        
        if self.playcookie:
            play_header['Cookie'] = self.playcookie
        
        if self.playreferer and 'Referer' not in play_header:
            play_header['Referer'] = self.playreferer
            
        if self.vip_duration:
            play_header['vip-duration'] = self.vip_duration
        
        payload, play_header = self._add_all_params_to_request(None, play_header)
            
        url = ''
        aid = id.split(',')
        uid = aid[0]
        kurl = aid[1]
        token = aid[2].replace('token+', '')
        player_parse_type = aid[3]
        parse_type = aid[4]
        
        if parse_type == '0':
            res =  {"parse": 0, "url": kurl, "header": play_header}
        elif parse_type == '2':
            res = {"parse": 1, "url": uid+kurl, "header": play_header}
        elif player_parse_type == '2':
            response = self.fetch(url=f'{uid}{kurl}', headers=play_header, verify=False)
            if response.status_code == 200:
                kjson1 = response.json()
                res = {"parse": 0, "url": kjson1['url'], "header": play_header}
        else:
            id1 = self.encrypt(kurl)
            payload = {
                'parse_api': uid,
                'url': id1,
                'player_parse_type': player_parse_type,
                'token': token
            }
            
            if self.vip_duration:
                payload['vip_duration'] = self.vip_duration
                
            payload, parse_headers = self._add_all_params_to_request(payload, self.header.copy())
                
            if self.parse_ua:
                parse_headers['User-Agent'] = self.parse_ua
                
            url1 = f"{self.xurl}.index/vodParse"
            response = self.post(url=url1, headers=parse_headers, data=payload, verify=False)
            if response.status_code == 200:
                response_data = response.json()
                encrypted_data = response_data['data']
                kjson = self.decrypt(encrypted_data)
                kjson1 = json.loads(kjson)
                kjson2 = kjson1['json']
                kjson3 = json.loads(kjson2)
                url = kjson3['url']
            res = {"parse": 0, "playUrl": '', "url": url, "header": play_header}
        return res

    def verification(self):
        random_uuid = str(uuid.uuid4())
        dat = self.fetch(f'{self.xurl}.verify/create?key={random_uuid}', headers=self.header, verify=False).content
        base64_img = base64.b64encode(dat).decode('utf-8')
        if not dat:
            return None
        code = self.ocr(base64_img)
        if not code:
            return None
        code = self.replace_code(code)
        if not (len(code) == 4 and code.isdigit()):
            return None
        return {'uuid': random_uuid, 'code': code}

    def replace_code(self, text):
        replacements = {'y': '9', '口': '0', 'q': '0', 'u': '0', 'o': '0', '>': '1', 'd': '0', 'b': '8', '已': '2','D': '0', '五': '5'}
        if len(text) == 3:
            text = text.replace('566', '5066')
            text = text.replace('066', '1666')
        return ''.join(replacements.get(c, c) for c in text)

    def ocr(self, base64img):
        dat2 = self.post("https://api.nn.ci/ocr/b64/text", data=base64img, headers=self.header, verify=False).text
        if dat2:
            return dat2
        else:
            return None

    def localProxy(self, params):
        if params['type'] == "m3u8":
            return self.proxyM3u8(params)
        elif params['type'] == "media":
            return self.proxyMedia(params)
        elif params['type'] == "ts":
            return self.proxyTs(params)
        return None

    def proxyM3u8(self, params):
        action = {
            'url': params['url'],
            'header': params.get('header', {}),
            'param': params.get('param', ''),
            'type': 'm3u8'
        }
        return action

    def proxyMedia(self, params):
        action = {
            'url': params['url'],
            'header': params.get('header', {}),
            'param': params.get('param', ''),
            'type': 'media'
        }
        return action

    def proxyTs(self, params):
        action = {
            'url': params['url'],
            'header': params.get('header', {}),
            'param': params.get('param', ''),
            'type': 'ts'
        }
        return action

    def isVideoFormat(self, url):
        video_formats = ['.m3u8', '.mp4', '.avi', '.mkv', '.flv', '.ts']
        return any(url.lower().endswith(fmt) for fmt in video_formats)

    def manualVideoCheck(self):
        pass

    def decrypt(self, encrypted_data_b64):
        key_bytes = self.key.encode('utf-8')
        iv_bytes = self.iv.encode('utf-8')
        encrypted_data = base64.b64decode(encrypted_data_b64)
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
        decrypted_padded = cipher.decrypt(encrypted_data)
        decrypted = unpad(decrypted_padded, AES.block_size)
        return decrypted.decode('utf-8')

    def encrypt(self, sencrypted_data):
        key_bytes = self.key.encode('utf-8')
        iv_bytes = self.iv.encode('utf-8')
        data_bytes = sencrypted_data.encode('utf-8')
        padded_data = pad(data_bytes, AES.block_size)
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
        encrypted_bytes = cipher.encrypt(padded_data)
        encrypted_data_b64 = base64.b64encode(encrypted_bytes).decode('utf-8')
        return encrypted_data_b64

    def _generate_random_ua(self):
        return 'okhttp/3.14.9'

    def _generate_android_id(self):
        return ''.join(random.choice('0123456789abcdef') for _ in range(16))

    def _add_auto_params_to_request(self, payload=None, headers=None):
        if headers is None:
            headers = self.header.copy()
        if payload is None:
            payload = {}
            
        if self.auto_params_level > 0:
            if self.auto_params_level >= 1 and not self.ext_device_id and not self.device_id:
                self.device_id = str(uuid.uuid4()).replace('-', '')
                headers['app-user-device-id'] = self.device_id
                if payload is not None:
                    payload['device_id'] = self.device_id
                
            if self.auto_params_level >= 2 and not self.ext_timestamp and not self.ext_sign:
                timestamp = str(int(time.time()))
                sign = self._generate_api_sign(timestamp)
                
                headers.update({
                    'app-api-verify-time': timestamp,
                    'app-api-verify-sign': sign,
                    'Accept-Encoding': "gzip",
                    'app-ui-mode': "light"
                })
                if payload is not None:
                    payload.update({
                        'timestamp': timestamp,
                        'sign': sign
                    })
        
        if (self.vip_config['type'] == 'login' and 
            self.user_token and  
            self.login_timestamp and self.login_sign and
            not self.ext_timestamp and not self.ext_sign and
            (self.auto_params_level < 2 or (self.auto_params_level >= 2 and not self.ext_timestamp and not self.ext_sign))):
            
            headers.update({
                'app-api-verify-time': self.login_timestamp,
                'app-api-verify-sign': self.login_sign,
                'Accept-Encoding': "gzip",
                'app-ui-mode': "light"
            })
            if payload is not None:
                payload.update({
                    'timestamp': self.login_timestamp,
                    'sign': self.login_sign
                })
            
        return payload, headers

if __name__ == '__main__':
    pass