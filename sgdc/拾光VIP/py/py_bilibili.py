Cv='Referer'
Cu='application/dash+xml'
Ct='interaction'
Cs='subtitle'
Cr='mimeType'
Cq='192000'
Cp='media_ft'
Co='media_bangumi'
Cn='stream'
Cm='playurl_info'
Cl='vod_actor'
Ck='\u3000👥 '
Cj='setting'
Ci='message'
Ch='totalrank'
Cg='room_id'
Cf='favorite'
Ce='attention'
Cd='videos'
Cc='  个人主页'
Cb='vod_pc'
Ca='series'
CZ='oldest'
CY='description'
CX='user_cover'
CW='roomid'
CV='text_small'
CU='watched_show'
CT='live_status'
CS='查看直播细化标签'
CR='https:'
CQ='fav_list'
CP='https://api.bilibili.com/x/web-interface/nav'
CO='bangumi_pay_parse'
CN='bangumi_vip_parse'
CM='raw_cookie_vip'
CL='raw_cookie_line'
CJ='contentType'
CI='header'
CH='mpd'
CG='codecid'
CF='playurl'
CE='season_title'
CD='edgeid'
CC='vod_list'
CB='AllPt'
CA='vod_year'
C9='title_type'
C8='bangumi'
C7='bili_user'
C6='seasons'
C5='sort'
C4='season_status'
C3='all'
C2='special'
C1='悄悄关注'
C0='最近关注'
B_='like_num'
Bz='crname'
By='part'
Bx='play'
Bw='%H:%M:%S'
Bv='module_author'
Bu='isVIP'
Bt='isLogin'
Bs='https://'
Br='utf-8'
Bq='排行榜'
Bp='showLiveFilterTag'
Bo='vodDefaultCodec'
Bn='vodDefaultQn'
Bm='favMode'
Bl='maxHomeVideoContent'
Bf='deadline'
Be='durl'
Bd='csrf'
Bc='codec'
Bb='AllPu'
Ba='🆙 '
BZ='vod_director'
BY='fromep'
BX='@thisepisode@'
BW='预告'
BV='000'
BU='最近访问'
BT='最常访问'
BS='coin'
BR='danmaku'
BQ='稍后再看'
BP='vod_count'
BO='episodes'
BN='view'
BM='stat'
BL='  ▶'
BK='archive'
BJ='UP主'
BI='modules'
BH='type_name'
BG=None
BF='历史'
BE='关注'
BD='rankingLis'
BC='tuijianLis'
BB='cateManual'
BA='heartbeatInterval'
B9=float
B7='s_title'
B6='graph_version'
B5='ssid'
B4='pages'
B3='ugc_season'
B2='parse'
B1='特别关注'
B0='正在直播'
A_='[/a]'
Az='"}/]'
Ay='pubdate'
Ax='new_ep'
Aw='index_show'
Av='content'
Au='pic'
At='keyword'
As='登录'
Ar='userid'
Aq='搜索'
Ap='vodDefaultAudio'
Ao='@@@'
An='\n'
Am='like'
Al='desc'
Ak='[a=cr:{"id": "'
Aj='fans'
Ai='up'
Ah='owner'
Ag='  🆙'
Af='mlid'
Ae='收藏'
Ad='直播'
Ac='影视'
Ab=True
Aa=type
AZ='audio'
AY='qn'
AX='format'
AW='vod_content'
AV='redirect_url'
AU='\u3000'
AT='ep'
AS='following'
AR='/'
AQ='4'
AP='User-Agent'
AO='cateLive'
AN='动态'
AM='推荐'
AL='3'
AK=round
AJ='﹩'
AI='this_array'
AH='\\"'
AG='live'
AF='vip'
AE='cookies_dic'
AD='_tmp'
AC='vod_play_url'
AB='vod_play_from'
AA='"'
A9='ss'
A8='season_id'
A7=' '
A6='uname'
A5='face'
A4='cateManualLiveExtra'
A3='热门'
A2='﹟'
A1='tid'
A0='2'
z=list
w='$'
v='cid'
u='result'
t='id'
s='mid'
r='cateManualLive'
q='order'
p='video'
o='epid'
n='duration'
m='av'
l='filter'
k='type'
j='users'
i='$$$'
h='cover'
g='limit'
f='pagecount'
e='master'
d=dict
c='total'
b='url'
a='page'
Z='page_size'
Y='vod_remarks'
W='key'
V='1'
U=len
T='aid'
S='vod_pic'
R='vod_id'
Q='fake'
P='title'
O='vod_name'
N='_'
M='code'
L='0'
K='value'
J=map
I='#'
H='name'
G='list'
F=int
E='data'
D='n'
C='v'
B=''
A=str
import sys,os,json as Bg,threading as x,hashlib,time as X,random as B8
from base.spider import Spider
from requests import session as Bh,utils as Bi,head
from requests.adapters import HTTPAdapter as Cw,Retry
from concurrent.futures import ThreadPoolExecutor as Cx,as_completed as Bj
from functools import reduce
from urllib.parse import quote as CK,urlencode as Bk
sys.path.append('..')
y,Cy=os.path.split(os.path.abspath(__file__))
if y.startswith('/data/'):y=os.path.abspath(os.path.join(y,'..'));y=os.path.abspath(os.path.join(y,'..'));y=f"{y}/files"
sys.path.append(y)
class Spider(Spider):
	defaultConfig={'currentVersion':'20240815_1',CL:B,CM:B,Bl:AL,Bm:L,Z:12,BA:'15',Bn:'80',Bo:'7',Ap:'30280',CN:Ab,CO:Ab,Bp:L,BB:[AM,Ac,Ad,AN,Ae,BE,BF,Aq],BC:[A3,Bq,'每周必看','入站必刷','番剧时间表','国创时间表'],BD:['动画','音乐','舞蹈','游戏','鬼畜','知识','科技','运动','生活','美食','动物','汽车','时尚','娱乐',Ac,'原创','新人']};focus_on_up_list=[];focus_on_search_key=[]
	def getName(A):return'哔哩哔哩'
	def load_config(A):
		try:
			with open(f"{y}/config.json",encoding=Br)as C:A.userConfig=Bg.load(C)
			B=A.userConfig.get(j,{})
			if B.get(e)and B[e].get(AE):A.session_master.cookies=Bi.cookiejar_from_dict(B[e][AE]);A.userid=B[e][Ar]
			if B.get(Q)and B[Q].get(AE):A.session_fake.cookies=Bi.cookiejar_from_dict(B[Q][AE])
		except:A.userConfig={}
		A.userConfig={**A.defaultConfig,**A.userConfig}
	dump_config_lock=x.Lock()
	def dump_config(A):
		F=[j,AO,r,A4];C={}
		for(B,D)in A.userConfig.items():
			E=A.defaultConfig.get(B)
			if E!=BG and D!=E or B in F:C[B]=D
		A.dump_config_lock.acquire()
		with open(f"{y}/config.json",'w',encoding=Br)as G:H=Bg.dumps(C,indent=1,ensure_ascii=False);G.write(H)
		A.dump_config_lock.release()
	pool=Cx(max_workers=8);task_pool=[]
	def homeContent(A,filter):
		A.pool.submit(A.add_live_filter);A.pool.submit(A.add_search_key);A.pool.submit(A.add_focus_on_up_filter);A.pool.submit(A.get_tuijian_filter);A.pool.submit(A.add_fav_filter);F=[AN,Ae,BE,BF];B=A.userConfig[BB]
		if not A.userid and not As in B:B+=[As]
		D=[]
		for C in B:
			if C in F and not A.userid:continue
			D.append({BH:C,'type_id':C})
		E={'class':D};A.add_focus_on_up_filter_event.wait();A.add_live_filter_event.wait();A.add_fav_filter_event.wait();A.add_search_key_event.wait()
		if filter:E['filters']=A.config[l]
		A.pool.submit(A.dump_config);return E
	userid=csrf=B;session_master=Bh();session_vip=Bh();session_fake=Bh();con=x.Condition();getCookie_event=x.Event();retries=Retry(total=5,backoff_factor=.1);adapter=Cw(max_retries=retries);session_master.mount(Bs,adapter);session_vip.mount(Bs,adapter);session_fake.mount(Bs,adapter)
	def getCookie_dosth(B,co):
		A=co.strip().split('=',1)
		if not'%'in A[1]:A[1]=CK(A[1])
		return A
	def getCookie(A,_type=e):
		D=_type;G=CL
		if D==AF:G=CM
		G=A.userConfig.get(G);K=A.userConfig.get(j,{});C=K.get(D,{})
		if not G and not C:
			if D==e:A.getCookie_event.set()
			with A.con:A.con.notifyAll()
			return
		I=C.get(AE,{})
		if G:I=d(J(A.getCookie_dosth,G.split(';')))
		L=Bi.cookiejar_from_dict(I);N=CP;O=A.fetch(N,headers=A.header,cookies=L);H=Bg.loads(O.text);C[Bt]=0
		if H[M]==0:
			C[Bt]=1;C[Ar]=H[E][s];C[A5]=H[E][A5];C[A6]=H[E][A6];C[AE]=I;C[Bu]=F(H[E]['vipStatus'])
			if D==e:A.session_master.cookies=L;A.userid=C[Ar];A.csrf=I['bili_jct']
			if C[Bu]:A.session_vip.cookies=L
		else:A.userid=B
		K[D]=C
		with A.con:
			if U(C)>1:A.userConfig.update({j:K})
			if D==e:A.getCookie_event.set()
	getFakeCookie_event=x.Event()
	def getFakeCookie(A,fromSearch=BG):
		if A.session_fake.cookies:A.getFakeCookie_event.set()
		C={};C[AP]=A.header[AP];B=A.fetch('https://space.bilibili.com/2/video',headers=C);A.session_fake.cookies=B.cookies;A.getFakeCookie_event.set()
		with A.con:D=A.userConfig.get(j,{});D[Q]={AE:d(B.cookies)};A.userConfig.update({j:D})
		if not fromSearch:
			A.getCookie_event.wait()
			if not A.session_master.cookies:A.session_master.cookies=B.cookies
	add_fav_filter_event=x.Event()
	def add_fav_filter(B):
		N=B.userConfig.get(j,{})
		if N.get(e)and N[e].get(Ar):F=B.userConfig[j][e][Ar]
		else:B.getCookie_event.wait();F=B.userid
		I=[]
		if F:
			Q='https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid=%s&jsonp=jsonp'%A(F);L=B._get_sth(Q).json()
			if L[M]==0 and L.get(E):R=L[E].get(G);I=z(J(lambda x:{D:B.cleanCharacters(x[P].strip()),C:x[t]},R))
		S=[{D:'追番',C:V},{D:'追剧',C:A0}];O=B.config[l].get(Ae)
		if O:O.insert(0,{W:Af,H:'分区',K:S+I})
		B.add_fav_filter_event.set();B.userConfig[CQ]=I
	add_focus_on_up_filter_event=x.Event()
	def add_focus_on_up_filter(B):
		F=B.focus_on_up_list
		if not B.session_master.cookies:B.getCookie_event.wait()
		L=z(J(lambda x:x[C],F))
		if B.session_master.cookies:
			N='https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/all?timezone_offset=-480&type=video&page=1';G=B._get_sth(N).json()
			if G[M]==0 and G.get(E):
				O=G[E].get('items',[])
				for I in J(lambda x:{D:x[BI][Bv][H],C:A(x[BI][Bv][s])},O):
					if not I in F and not I[C]in L:F.append(I)
		P=[{D:'登录与设置',C:As}];F+=P;B.config[l][AN]=Q=[B.config[l].get(AN,[])[-1]];Q.insert(0,{W:s,H:BJ,K:F});B.add_focus_on_up_filter_event.set()
	def get_live_parent_area_list(O,parent_area):B=parent_area;E=B[H];id=A(B[t]);F=B[G];I=z(J(lambda area:{D:area[H],C:A(area['parent_id'])+N+A(area[t])},F));L={W:A1,H:E,K:I};M={t:id+'_0',K:L};return E,M
	def get_live_list(A):
		C='https://api.live.bilibili.com/xlive/web-interface/v1/index/getWebAreaList?source_id=2';B=A._get_sth(C,Q).json()
		if B[M]==0:D=B[E][E];A.userConfig[AO]=d(J(A.get_live_parent_area_list,D))
		return A.userConfig[AO]
	def set_default_cateManualLive(A):
		B=[{D:AM,C:AM}]
		for E in A.userConfig[AO]:F={D:E,C:A.userConfig[AO][E][t]};B.append(F)
		A.defaultConfig[r]=B;return B
	add_live_filter_event=x.Event()
	def add_live_filter(A):
		C=A.userConfig.get(AO,{});G=A.pool.submit(A.get_live_list)
		if not C:C=G.result()
		I=A.pool.submit(A.set_default_cateManualLive);A.config[l][Ad]=D=[];B=A.userConfig.get(r,[])
		if not B:B=I.result()
		if B:J={W:A1,H:'分区',K:B};D.append(J)
		if F(A.userConfig[Bp]):
			for E in C.values():
				if U(E[K][K])>1:D.append(E[K])
		A.add_live_filter_event.set()
	add_search_key_event=x.Event()
	def add_search_key(A):
		B=A.focus_on_search_key;L='https://api.bilibili.com/x/web-interface/search/square?limit=10&platform=web';F=A._get_sth(L,Q).json();P={}
		if F[M]==0:N=F[E]['trending'].get(G,[]);B+=z(J(lambda x:x[At],N))
		I={W:At,H:'搜索词',K:[]};I[K]=z(J(lambda i:{D:i,C:i},B));A.config[l][Aq]=O=A.config[l][Aq][-3:];O.insert(0,I);A.add_search_key_event.set()
	def get_tuijian_filter(E):
		I={'番剧时间表':'10001','国创时间表':'10004',Bq:L,'动画':V,'音乐':AL,'舞蹈':'129','游戏':AQ,'鬼畜':'119','知识':'36','科技':'188','运动':'234','生活':'160','美食':'211','动物':'217','汽车':'223','时尚':'155','娱乐':'5',Ac:'181','原创':'origin','新人':'rookie'};J=[{D:BC,C:'分区'},{D:BD,C:Bq}];E.config[l][AM]=M=[]
		for F in J:
			G={W:A1,H:F[C],K:[]};N=E.userConfig.get(F[D],[])
			for A in N:
				B=I.get(A)
				if not B:B=A
				O={D:A,C:B};G[K].append(O)
			M.append(G)
	def __init__(A):A.load_config();A.pool.submit(A.getCookie);A.pool.submit(A.getFakeCookie);A.pool.submit(A.getCookie,AF);B=AK(X.time());C=X.gmtime(B).tm_hour;A.pool.submit(A.get_wbiKey,C)
	def init(A,extend=B):print('============{0}============'.format(extend))
	def isVideoFormat(A,url):0
	def manualVideoCheck(A):0
	def destroy(A):0
	def format_img(B,img):
		A=img;A+='@672w_378h_1c.webp'
		if not A.startswith('http'):A=CR+A
		return A
	def pagination(A,array,pg):B=A.userConfig[Z]*F(pg);C=B-A.userConfig[Z];return array[C:B]
	def zh(D,num):
		C=num
		if F(C)>=100000000:B=AK(B9(C)/B9(100000000),1);B=A(B)+'亿'
		elif F(C)>=10000:B=AK(B9(C)/B9(10000),1);B=A(B)+'万'
		else:B=A(C)
		return B
	def second_to_time(D,a):
		a=F(a)
		if a<3600:C=X.strftime('%M:%S',X.gmtime(a))
		else:C=X.strftime(Bw,X.gmtime(a))
		if A(C).startswith(L):C=A(C).replace(L,B,1)
		return C
	def str2sec(E,x):
		x=A(x)
		try:D,B,C=x.strip().split(':');return F(D)*3600+F(B)*60+F(C)
		except:B,C=x.strip().split(':');return F(B)*60+F(C)
	def find_bangumi_id(C,url):
		B=A(url).split(AR)[-1]
		if not B:B=A(url).split(AR)[-2]
		B=B.split('?')[0];return B
	def get_Login_qrcode(H,pg):
		N='https://www.bilibili.com/favicon.ico';K='setting_login_';A={}
		if F(pg)!=1:return A
		D=[{R:'setting_tab&filter',O:'标签与筛选',S:N},{R:'setting_liveExtra',O:CS,S:N}];I='https://passport.bilibili.com/x/passport-login/web/qrcode/generate';J=H._get_sth(I,Q).json()
		if J[M]==0:
			id=J[E]['qrcode_key'];I=J[E][b];P={e:'主账号',AF:'副账号'};T={0:'未登录',1:'已登录'};U={0:B,1:'👑'};V=H.userConfig.get(j,{})
			for(W,X)in P.items():
				C=V.get(W)
				if C:D.append({R:K+id,O:C[A6],S:H.format_img(C[A5]),Y:U[C[Bu]]+X+A7+T[C[Bt]]})
			L={E:I,'quietzone':'208','codepage':'UTF8','quietunit':'px','errorcorrection':'M','size':'small'};D.append({R:K+id,S:'http://jm92swf.s1002.xrea.com/?'+Bk(L)});D.append({R:K+id,S:'https://bili.ming1992.xyz/API/QRCode?'+Bk(L)})
		A[G]=D;A[a]=1;A[f]=1;A[g]=1;A[c]=1;return A
	time_diff1={V:[0,300],A0:[300,900],AL:[900,1800],AQ:[1800,3600],'5':[3600,0x4ee2d6d415b85acef80ffffffff]};time_diff=L;dynamic_offset=B
	def get_dynamic(C,pg,mid,order):
		if mid==L:
			D={}
			if F(pg)==1:C.dynamic_offset=B
			Q='https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/all?timezone_offset=-480&type=video&offset=%s&page=%s'%(C.dynamic_offset,pg);J=C._get_sth(Q).json()
			if J[M]==0:
				C.dynamic_offset=J[E].get('offset');K=[];U=J[E]['items']
				for N in U:V=N[BI][Bv][H];I=N[BI]['module_dynamic']['major'][BK];W=A(I[T]).strip();X=C.cleanCharacters(I[P].strip());Z=I[h].strip();b=A(C.second_to_time(C.str2sec(I['duration_text']))).strip()+Ag+A(V).strip();K.append({R:m+W,O:X,S:C.format_img(Z),Y:b})
				D[G]=K;D[a]=pg;D[f]=9999;D[g]=99;D[c]=999999
			return D
		else:return C.get_up_videos(mid=mid,pg=pg,order=order)
	def get_found_vod(G,vod):
		C=vod;D=C.get(T,B)
		if not D:D=C.get(t,B)
		E=C.get('goto',B)
		if not E or E and E==m:D=m+A(D).strip()
		elif E=='ad':return[]
		N=C[P].strip();Q=C[Au].strip();U=C.get('is_followed')
		if E==AG:
			L=C['room_info'];I=B;V=L.get(CT,B)
			if V:I='直播中  '
			else:return[]
			I+='👁'+L[CU][CV]+Ag+C[Ah][H].strip()
		else:
			K=C.get('rcmd_reason',B)
			if K and Aa(K)==d and K.get(Av):
				F='  🔥'+K[Av].strip()
				if'人气飙升'in F:F='  🔥人气飙升'
			elif U:F='  已关注'
			else:F=Ag+C[Ah][H].strip()
			I=A(G.second_to_time(C[n])).strip()+BL+G.zh(C[BM][BN])+F
		M=[{R:D,O:N,S:G.format_img(Q),Y:I}]
		for W in J(G.get_found_vod,C.get('others',[])):M.extend(W)
		return M
	_popSeriesInit=0
	def get_found(A,tid,rid,pg):
		H=tid;C=pg;D={};K=1
		if H==AM:O=A.encrypt_wbi(fresh_type=4,feed_version='V8',brush=1,fresh_idx=C,fresh_idx_1h=C,ps=A.userConfig[Z])[0];B='https://api.bilibili.com/x/web-interface/wbi/index/top/feed/rcmd?'+O;K=99
		elif H==A3:B='https://api.bilibili.com/x/web-interface/popular?pn={0}&ps={1}'.format(C,A.userConfig[Z]);K=99
		elif H=='入站必刷':B='https://api.bilibili.com/x/web-interface/popular/precious'
		elif H=='每周必看':
			if F(C)==1:B='https://api.bilibili.com/x/web-interface/popular/series/list';I=A._get_sth(B,Q).json();A._popSeriesInit=F(I[E][G][0]['number'])
			P=A._popSeriesInit-F(C)+1;K=A._popSeriesInit;B=f"https://api.bilibili.com/x/web-interface/popular/series/one?number={P}"
		else:B='https://api.bilibili.com/x/web-interface/ranking/v2?rid={0}&type={1}'.format(rid,H)
		I=A._get_sth(B).json()
		if I[M]==0:
			N=[];L=I[E].get('item')
			if not L:L=I[E][G]
			for R in J(A.get_found_vod,L):N.extend(R)
			D[G]=N;D[a]=C;D[f]=K;D[g]=99;D[c]=999999
		return D
	def get_bangumi(D,tid,pg,order,season_status):
		X='first_ep';W='first_ep_info';T=order;I=tid;H={}
		if T=='追番剧':J='https://api.bilibili.com/x/space/bangumi/follow/list?type={0}&vmid={1}&pn={2}&ps={3}'.format(I,D.userid,pg,D.userConfig[Z]);K=D._get_sth(J).json()
		else:
			J='https://api.bilibili.com/pgc/season/index/result?type=1&season_type={0}&page={1}&order={2}&season_status={3}&pagesize={4}'.format(I,pg,T,season_status,D.userConfig[Z])
			if T==A3:
				if I==V:J='https://api.bilibili.com/pgc/web/rank/list?season_type={0}&day=3'.format(I)
				else:J='https://api.bilibili.com/pgc/season/rank/web/list?season_type={0}&day=3'.format(I)
			K=D._get_sth(J,Q).json()
		if K[M]==0:
			if E in K:L=K[E][G]
			else:L=K[u][G]
			if U(L)>D.userConfig[Z]:L=D.pagination(L,pg)
			b=[]
			for C in L:
				e=A(C[A8]).strip();i=C[P];N=C.get('ss_horizontal_cover')
				if not N:
					if C.get(W)and h in C[W]:N=C[W][h]
					elif C.get(X)and h in C[X]:N=C[X][h]
					else:N=C[h].strip()
				F=C.get(Aw,B)
				if not F and C.get(Ax)and C[Ax].get(Aw):F=C[Ax][Aw]
				F=F.replace('更新至','🆕');d=C.get(BM)
				if d:F='▶'+D.zh(d.get(BN))+'  '+F
				b.append({R:A9+e,O:i,S:D.format_img(N),Y:F})
			H[G]=b;H[a]=pg;H[f]=9999;H[g]=90;H[c]=999999
		return H
	def get_timeline(E,tid,pg):
		b='pub_index';Z='ep_cover';D={};d='https://api.bilibili.com/pgc/web/timeline/v2?season_type={0}&day_before=2&day_after=4'.format(tid);F=E._get_sth(d,Q).json()
		if F[M]==0:
			T=[];H=F[u]['latest']
			for C in H:I=A(C[A8]).strip();J=C[P].strip();K=C[Z].strip();N='🆕'+C[b]+'  ❤ '+C['follows'].replace('系列',B).replace('追番',B);T.append({R:A9+I,O:J,S:E.format_img(K),Y:N})
			V=[];W=F[u]['timeline']
			for e in range(U(W)):
				H=W[e][BO]
				for C in H:
					if A(C['published'])==L:I=A(C[A8]).strip();J=A(C[P]).strip();K=A(C[Z]).strip();h=A(X.strftime('%m-%d %H:%M',X.localtime(C['pub_ts'])));N=h+'   '+C[b];V.append({R:A9+I,O:J,S:E.format_img(K),Y:N})
			D[G]=V+T;D[a]=1;D[f]=1;D[g]=90;D[c]=999999
		return D
	def get_live(F,pg,parent_area_id,area_id):
		N='recommend_room_list';I=parent_area_id;C={}
		if I==AM:H='https://api.live.bilibili.com/xlive/web-interface/v1/webMain/getList?platform=web&page=%s'%pg;J=F._get_sth(H).json()
		else:
			H='https://api.live.bilibili.com/xlive/web-interface/v1/second/getList?platform=web&parent_area_id=%s&area_id=%s&sort_type=online&page=%s'%(I,area_id,pg)
			if I==A3:H='https://api.live.bilibili.com/room/v1/room/get_user_recommend?page=%s&page_size=%s'%(pg,F.userConfig[Z])
			J=F._get_sth(H,Q).json()
		if J[M]==0:
			L=[];B=J[E]
			if N in B:B=B[N]
			elif G in B:B=B[G]
			for D in B:
				T=A(D[CW]).strip();U=F.cleanCharacters(D[P]);K=D.get(CX)
				if not K:K=D.get(h)
				V='👁'+D[CU][CV].strip()+Ag+D[A6].strip();L.append({R:T,O:U,S:F.format_img(K),Y:V})
			C[G]=L;C[a]=pg;C[f]=9999;C[g]=99;C[c]=999999
		return C
	def get_up_series(I,mid,pg):
		C={};N='https://api.bilibili.com/x/polymer/web-space/seasons_series_list?mid=%s&page_num=%s&page_size=%s'%(mid,pg,I.userConfig[Z]);D=I._get_sth(N,Q).json()
		if D[M]==0:
			K=[];D=D[E]['items_lists'];P=D['seasons_list']+D['series_list']
			for L in P:
				F=L.get('meta');J=A(F.get(A8,B)).strip()
				if J:J=m+A(L['recent_aids'][0])
				else:J='list_'+A(mid)+'_series_'+A(F.get('series_id',B)).strip()
				T=I.cleanCharacters(F[H]);U=F.get(h);V=F.get(CY,B).strip();K.append({R:J,O:T,S:I.format_img(U),Y:V})
			C[G]=K;C[a]=pg;C[f]=9999;C[g]=99;C[c]=999999
		return C
	get_up_videos_result=d()
	def get_up_videos(C,mid,pg,order):
		L=order;K=pg;D=mid;I={}
		if not D in C.up_info or F(K)==1:C.get_up_info_event.clear();C.pool.submit(C.get_up_info,D)
		V=W=B
		if L==CZ:W=L;L=Ay
		elif L=='quicksearch':
			V='投稿: ';J=C.get_up_videos_result.get(D,[])
			if J:I[G]=J;return I
		elif L==Ca:return C.get_up_series(mid=D,pg=K)
		X=K
		if W:C.get_up_info_event.wait();X=C.up_info[D][Cb]-F(K)+1
		h=C.encrypt_wbi(mid=D,pn=X,ps=C.userConfig[Z],order=L)[0];i=f"https://api.bilibili.com/x/space/wbi/arc/search?{h}";b=C._get_sth(i,Q).json();J=[]
		if b[M]==0:
			j=b[E][G]['vlist']
			for N in j:
				k=A(N[T]).strip();l=C.cleanCharacters(N[P].strip());n=N[Au].strip();d=C.second_to_time(C.str2sec(A(N['length']).strip()))+BL+C.zh(N[Bx])
				if not V:d+='  💬'+C.zh(N['video_review'])
				J.append({R:m+k,O:V+l,S:C.format_img(n),Y:d})
			if W:J.reverse()
			if F(K)==1:
				C.get_up_info_event.wait();U=C.up_info[D];e=U[H]+Cc
				if V:e='UP: '+U[H]
				o={R:Ai+A(D),O:e,S:C.format_img(U[A5]),Y:U[AS]+'  👥'+U[Aj]+'  🎬'+A(U[BP])};J.insert(0,o)
			if V:C.get_up_videos_result[D]=J
			I[G]=J;I[a]=K;I[f]=99;I[g]=99;I[c]=999999
		return I
	history_view_at=0
	def get_history(D,type,pg):
		W='progress';H={}
		if F(pg)==1:D.history_view_at=0
		X='https://api.bilibili.com/x/web-interface/history/cursor?ps={0}&view_at={1}&type={2}'.format(D.userConfig[Z],D.history_view_at,type)
		if type==BQ:X='https://api.bilibili.com/x/v2/history/toview'
		U=D._get_sth(X).json()
		if U[M]==0:
			b=[];V=U[E].get(G,[])
			if type==BQ:V=D.pagination(V,pg)
			else:D.history_view_at=U[E]['cursor']['view_at']
			for C in V:
				I=C.get('history',B)
				if I:J=I['business'];K=A(I['oid']).strip();d=C[h].strip();Q=A(I[By]).strip()
				else:J=BK;K=A(C[T]).strip();d=C[Au].strip();Q=A(C[a][By]).strip()
				if J=='article':continue
				elif J=='pgc':K=AT+A(I[o]);e=C[c];Q=C.get('show_title')
				elif J==BK:K=m+K;e=C[Cd]
				i=D.cleanCharacters(C[P])
				if J==AG:j=C.get('badge',B);N=j+Ag+C['author_name'].strip()
				else:
					if A(C[W])=='-1':N='已看完'
					elif A(C[W])==L:N='刚开始看'
					else:k=A(D.second_to_time(C[W])).strip();N='看到  '+k
					if not e in[0,1]and Q:N+=' ('+A(Q)+')'
				b.append({R:K,O:i,S:D.format_img(d),Y:N})
			H[G]=b;H[a]=pg;H[f]=9999;H[g]=90;H[c]=999999
		return H
	def get_fav_detail(C,pg,mlid,order):
		I='cnt_info';D={};J='https://api.bilibili.com/x/v3/fav/resource/list?media_id=%s&order=%s&pn=%s&ps=10&platform=web&type=0'%(mlid,order,pg);F=C._get_sth(J).json()
		if F[M]==0:
			H=[];K=F[E].get('medias',[])
			for B in K:
				if B.get(k)in[2]and B.get(P)!='已失效视频':L=A(B[t]).strip();N=C.cleanCharacters(B[P]);Q=B[h].strip();T=A(C.second_to_time(B[n])).strip()+BL+C.zh(B[I][Bx])+'\u3000💬'+C.zh(B[I][BR]);H.append({R:m+L+'_mlid'+A(mlid),O:N,S:C.format_img(Q),Y:T})
			D[G]=H;D[a]=pg;D[f]=9999;D[g]=99;D[c]=999999
		return D
	def get_up_videoNum(B,mid):
		C={};I=f"http://api.bilibili.com/x/space/navnum?mid={mid}";D=B._get_sth(I,Q).json()
		if D[M]==0:
			C[BP]=A(D[E][p]).strip();G=divmod(F(C[BP]),B.userConfig[Z]);H=G[0]
			if G[1]!=0:H+=1
			C[Cb]=H
		B.up_info[mid].update(C);B.get_up_info_event.set()
	get_up_info_event=x.Event();up_info={}
	def get_up_info(B,mid,data={}):
		J='Official';D=data;C=mid;B.up_info[C]=A=B.up_info.get(C,{});B.pool.submit(B.get_up_videoNum,C)
		if not D:
			K=f"https://api.bilibili.com/x/web-interface/card?mid={C}";G=B._get_sth(K).json()
			if G[M]==0:D=G[E]
			else:return A
		F=D['card'];A[AS]='未关注'
		if D[AS]:A[AS]='已关注'
		A[H]=I=B.cleanCharacters(F[H]);A[Bz]=Ak+C+'_pubdate_getupvideos","name": "'+I.replace(AA,AH)+Az+I+A_;A[A5]=F[A5];A[Aj]=B.zh(F[Aj]);A[B_]=B.zh(D[B_]);A[Al]=F[J][Al]+AU+F[J][P];return A
	def get_vod_relation(F,query):
		G=f"https://api.bilibili.com/x/web-interface/archive/relation?{query}";A=F._get_sth(G).json();B=[]
		if A[M]==0:
			A=A[E]
			if A[Ce]:B.append('已关注')
			else:B.append('未关注')
			C=[]
			if A[Cf]:C.append('⭐')
			if A[Am]:C.append('👍')
			D=A.get(BS)
			if D:C.append('💰'*D)
			if U(C)==3:B.append('👍💰⭐')
			else:B.extend(C)
			if A['dislike']:B.append('👎')
			if A['season_fav']:B.append('已订阅合集')
		return B
	def get_follow(I,pg,sort):
		J=pg;D=sort;K={}
		if D==BT:L='https://api.bilibili.com/x/relation/followings?vmid={0}&pn={1}&ps=10&order=desc&order_type=attention'.format(I.userid,J)
		elif D==C0:L='https://api.bilibili.com/x/relation/followings?vmid={0}&pn={1}&ps=10&order=desc&order_type='.format(I.userid,J)
		elif D==B0:L='https://api.live.bilibili.com/xlive/web-ucenter/v1/xfetter/GetWebList?page={0}&page_size=10'.format(J)
		elif D==BU:L='https://api.bilibili.com/x/v2/history?pn={0}&ps=15'.format(J)
		elif D==B1:L='https://api.bilibili.com/x/relation/tag?mid={0}&tagid=-10&pn={1}&ps=10'.format(I.userid,J)
		elif D==C1:L='https://api.bilibili.com/x/relation/whispers?pn={0}&ps=10'.format(J)
		else:L='https://api.bilibili.com/x/relation/followers?vmid={0}&pn={1}&ps=10&order=desc&order_type=attention'.format(I.userid,J)
		Q=I._get_sth(L).json()
		if Q[M]!=0:return K
		if D==B1 or D==BU:T=Q[E]
		elif D==B0:T=Q[E]['rooms']
		else:T=Q[E][G]
		if F(J)==1:I.recently_up_list=[]
		X=[]
		for C in T:
			U=B
			if D==BU:
				N=Ai+A(C[Ah][s])
				if N in I.recently_up_list:continue
				I.recently_up_list.append(N);V=A(C[Ah][H]).strip();W=A(C[Ah][A5]).strip()
			elif D==B0:N=A(C[Cg]);V=I.cleanCharacters(C[P]);W=C['cover_from_user'].strip();U=C[A6].strip()
			else:N=Ai+A(C[s]);V=A(C[A6]).strip();W=A(C[A5]).strip()
			if C2 in C and C[C2]==1:U=B1
			X.append({R:N,O:V,S:I.format_img(W),Y:U})
		K[G]=X;K[a]=J;K[f]=9999;K[g]=99;K[c]=999999;return K
	def homeVideoContent(A):B=A.get_found(rid=L,tid=C3,pg=1)[G][:F(A.userConfig[Bl])];C={G:B};return C
	def categoryContent(I,tid,pg,filter,extend):
		u='_clicklink';O=pg;H=extend;D=tid;I.pool.submit(I.stop_heartbeat)
		if D==AM:
			if A1 in H:D=H[A1]
			if D.isdigit():
				D=F(D)
				if D>10000:D-=10000;return I.get_timeline(tid=D,pg=O)
				b=D;D=C3;return I.get_found(tid=D,rid=b,pg=O)
			b=L;return I.get_found(tid=D,rid=b,pg=O)
		elif D==Ac:
			D=V;P=A3;d='-1'
			if A1 in H:D=H[A1]
			if q in H:P=H[q]
			if C4 in H:
				if P==A3:P=A0
				d=H[C4]
			return I.get_bangumi(D,O,P,d)
		elif D==AN:
			R=L;P=Ay
			if s in H:R=H[s]
			if q in H:P=H[q]
			if R==L and not I.userid or R==As:return I.get_Login_qrcode(O)
			return I.get_dynamic(pg=O,mid=R,order=P)
		elif D==Ad:
			D=A3;h=L
			if A1 in H:D=H[A1]
			if N in D:i=D.split(N);D=i[0];h=i[1]
			return I.get_live(pg=O,parent_area_id=D,area_id=h)
		elif D==As:return I.get_Login_qrcode(O)
		elif D==BE:
			j=BT
			if C5 in H:j=H[C5]
			return I.get_follow(O,j)
		elif D==Ae:
			S=A(I.userConfig[Bm])
			if Af in H:S=H[Af]
			m=I.config[l].get(Ae)
			if S in[V,A0]:return I.get_bangumi(tid=S,pg=O,order='追番剧',season_status=B)
			elif S==L and m:
				for Q in m:
					if Q[W]==Af:
						if U(Q[K])>1:S=Q[K][2][C]
						break
			P='mtime'
			if q in H:P=H[q]
			return I.get_fav_detail(pg=O,mlid=S,order=P)
		elif D==BF:
			type=C3
			if k in H:type=H[k]
			if type==BJ:return I.get_follow(pg=O,sort=BU)
			return I.get_history(type=type,pg=O)
		elif D.endswith('_getbangumiseasons'):
			if F(O)==1:return{G:I.detailContent_args[D.split(N)[0]][C6]}
		elif D.endswith('_getupvideos'):R,P,v=D.split(N);return I.get_up_videos(pg=O,mid=R,order=P)
		elif D.endswith('_related'):
			w,v=D.split(N);x=f"https://api.bilibili.com/x/web-interface/archive/related?aid={w}";o=I._get_sth(x,e).json();T={}
			if o.get(M)==0:
				r=[]
				for y in J(I.get_found_vod,o[E]):r.extend(y)
				T[G]=r;T[a]=1;T[f]=1;T[g]=99;T[c]=40
			return T
		elif D.endswith(u):
			X=D.replace(u,B);Y=L
			if n in H:Y=H[n]
			return I.get_search_content(key=X,pg=O,duration_diff=Y,order=B,type=p,ps=I.userConfig[Z])
		else:
			Y=L
			if n in H:Y=H[n]
			type=p
			if k in H:type=H[k]
			P=Ch
			if q in H:P=H[q]
			X=A(I.search_key);t=I.config[l].get(Aq)
			if not X and t:
				for Q in t:
					if Q[W]==At:
						if U(Q[K])>0:X=Q[K][0][C]
						break
			if At in H:X=H[At]
			return I.get_search_content(key=X,pg=O,duration_diff=Y,order=P,type=type,ps=I.userConfig[Z])
	def get_search_content(D,key,pg,duration_diff,order,type,ps):
		I=pg;L=BG
		if not A(I).isdigit():L=I;I=1
		X=D.encrypt_wbi(keyword=key,page=I,duration=duration_diff,order=order,search_type=type,page_size=ps)[0];Z=f"https://api.bilibili.com/x/web-interface/wbi/search/type?{X}";V=D._get_sth(Z,Q).json();F={}
		if V.get(M)==0 and u in V[E]:
			W=[];J=V[E].get(u)
			if J and type==AG:J=J.get('live_room')
			if not J:return F
			for C in J:
				if type!=C[k]:continue
				H=B
				if type==C7:N=Ai+A(C[s]).strip();U=C['upic'].strip();K='👥'+D.zh(C[Aj])+'  🎬'+D.zh(C[Cd]);H=C[A6]
				elif type==AG:N=A(C[CW]).strip();U=C[h].strip();K='👁'+D.zh(C['online'])+Ag+C[A6]
				elif'media'in type:N=A9+A(C[A8]).strip();U=C[h].strip();K=A(C[Aw]).strip().replace('更新至','🆕')
				else:
					N=m+A(C[T]).strip();U=C[Au].strip();K=A(D.second_to_time(D.str2sec(C[n]))).strip()+BL+D.zh(C[Bx])
					if L==BG:K+='  💬'+D.zh(C[BR])
				if not H:H=D.cleanCharacters(C[P])
				if L:H=L+H
				W.append({R:N,O:H,S:D.format_img(U),Y:K})
			F[G]=W;F[a]=I;F[f]=9999;F[g]=99;F[c]=999999
		return F
	def cleanSpace(C,s):return A(s).replace(An,B).replace('\t',B).replace('\r',B).replace(A7,B)
	def cleanCharacters(C,s):return A(s).replace('<em class="keyword">',B).replace('</em>',B).replace('&quot;',AA).replace('&amp;','&')
	def get_normal_episodes(L,episode):
		D=episode;M=D.get(AI);C=L.detailContent_args
		if M:C=C[M]
		N=D.get(T,B)
		if not N:N=C[T]
		S=D.get(v,B);H=D.get(P,B)
		if not H:H=D.get(By,B)
		J=D.get(n,B)
		if not J:
			X=D.get(a,B)
			if X:J=X[n]
		E=G=Y=U=B;O=D.get('ep_id',B)
		if AV in D and C8 in D[AV]:O=L.find_bangumi_id(D[AV])
		if O:
			if J and A(J).endswith(BV):J=F(J/1000)
			if H.isdigit():H='第'+H+C[C9]
			E=D.get('badge',B)
			if not L.session_vip.cookies and E=='会员'and L.userConfig[CN]or E=='付费'and L.userConfig[CO]:C[B2]=U=V
			if L.session_vip.cookies:E=E.replace('会员',B)
			if E==BW:E=E.replace(BW,B);Y=V
			if E:E='【'+E+'】'
			G=D.get('long_title',B)
			if not E and G:G=A7+G
		Q=H+E+G;Q=Q.replace(I,A2).replace(w,AJ)
		if B3 in C:
			if Q in C[B3]:Q+=f"_av{N}"
			else:C[B3].append(Q)
		K=f"{Q}${N}_{S}_{O}_{J}_"
		if M:K+='@'+M
		if f"{N}_{S}"in C:W=C[B4];W[0]=K+BX;K=I.join(W);C[B4]=W
		Z=C.get(o,B)
		if Z==AT+A(O):C[BY]=K
		b=C.get(B5,B)
		if b:
			if Y:return K,B
			if U:
				if G:G='【解析】'+G
				H+=G;R=f"{H}${N}_{S}_{O}_{J}_{U}"
				if M:R+='@'+M
				if Z==AT+A(O):C[BY]=R+I+C[BY]
			else:R=K
			return K,R
		else:return K
	def get_ugc_season(D,section,season_title,sec_len,array):
		F=season_title;E=section
		if sec_len>1:A=F+A7+E[P]
		else:A=F
		A=A.replace(I,A2).replace(w,AJ);G=E.get(BO);C=I.join(J(D.get_normal_episodes,J(lambda e:D.add_this_array(e,array),G)))
		if BX in C:C=C.replace(BX,B);return A,C,0
		return A,C
	def get_vodReply(K,oid,pg=B):
		W='member';V='rpid';X=K.encrypt_wbi(type=1,ps=30,oid=A(oid))[0];Y=f"https://api.bilibili.com/x/v2/reply/wbi/main?{X}";L=K._get_sth(Y).json();O=B
		if L[M]==0:
			I=L[E].get('replies');Q=L[E].get('top_replies')
			if Q and I:I=Q+I
			if I:
				Z=L[E]['upper'][s];R=[]
				for F in I:
					a=F[V];J=F[W]['sex']
					if J and J=='女':J='👧'
					else:J='👦'
					S=F[s];H=F[W][A6]
					if S==Z:H='🆙'+H
					b='👍'+K.zh(F[Am]);H=Ak+f'{S}_pubdate_getupvideos","name": "'+H.replace(AA,AH)+Az+b+J+H+A_+'：';G=F[Av][Ci].strip()
					if'/note-app/'in G:continue
					if U(G)>400 or G.count(D)>24:G=K.cleanSpace(G)
					c=F[Av].get('jump_url',{})
					for(C,N)in c.items():
						d=C
						if not N.get('app_url_schema')and not N.get('pc_url'):
							if C.startswith('https://www.bilibili.com/')or C.startswith('https://b23.tv/'):
								C=A(C).split('?')[0].split(AR)
								while C[-1]==B:C.pop(-1)
								C=C[-1]
							if C.startswith(m)or C.startswith('BV')or C.startswith(AT)or C.startswith(A9):a=A(F[V]);T=N[P].replace(AA,AH);e=Ak+C+'_clicklink","name": "'+T+Az+'▶'+T+A_;G=G.replace(d,e)
					f=H+G;R.append(f)
				O=An.join(R)
		return O
	def add_this_array(A,e,array):e[AI]=array;return e
	detailContent_args={}
	def detailContent(H,array):
		A8='tag_name';A3='up_info';A1='relation';A0='vodReply';L=array;H.pool.submit(H.stop_heartbeat);L=L[0]
		if L.startswith(Cj):
			n=L.split(N)
			if n[1]=='tab&filter':return H.setting_tab_filter_detailContent()
			elif n[1]=='liveExtra':return H.setting_liveExtra_detailContent()
			elif n[1]=='login':return H.setting_login_detailContent(n[2])
		if L.startswith(G):return H.series_detailContent(L)
		if L.isdigit():return H.live_detailContent(L)
		if L.startswith(Ai):return H.up_detailContent(L)
		H.detailContent_args[L]=K={AI:L,**H.detailContent_args.get(L,{})};AO=K.get(B6)
		if AO:return H.interaction_detailContent(K)
		f=id=A4=p=B;V=K.get(T);AD=K.get(o)
		if V:
			L=f"av{V}"
			if AD:L=AD
			f=1
		K['_notfirst']=f
		if L.startswith(A9)or L.startswith(AT):return H.ysContent(K)
		for d in L.split(N):
			if d.startswith(m):id=d.replace(m,B);p=H.encrypt_wbi(aid=id)[0]
			elif d.startswith('BV'):id=d;p=H.encrypt_wbi(bvid=d)[0]
			elif d.startswith(Af):A4=d.replace(Af,B)
		if not A0 in K:K[A0]=H.pool.submit(H.get_vodReply,id)
		if not A1 in K:K[A1]=H.pool.submit(H.get_vod_relation,p)
		AP=f"https://api.bilibili.com/x/web-interface/wbi/view/detail?{p}";q=H._get_sth(AP,Q).json()
		if q[M]!=0:return{}
		W=q[E]['View'];AE=W.get(AV,B)
		if C8 in AE:K[o]=id=H.find_bangumi_id(AE);return H.ysContent(K)
		L=K[AI];Z=A(W[Ah][s]);K[T]=V=A(W.get(T));r=W.get(v)
		if not A3 in K:K[A3]=H.pool.submit(H.get_up_info,mid=Z,data=q[E].get('Card'))
		AF=H.cleanCharacters(W[P]);AQ=W[Au];j=W[Al].strip();AR=W['tname'];AS=X.strftime('%Y%m%d',X.localtime(W[Ay]));k=W[BM];t=W['rights'].get('is_stein_gate',0);g=[];g.append('▶'+H.zh(k[BN]));g.append('💬'+H.zh(k[BR]));g.append('👍'+H.zh(k[Am]));g.append('💰'+H.zh(k[BS]));g.append('⭐'+H.zh(k[Cf]));e={R:m+A(V),O:AF,S:AQ,BH:AR,CA:AS};e[Y]=AU.join(g)
		if f"{V}_{r}"in K:K.pop(f"{V}_{r}")
		A5=W[B4]
		if A5:K[B4]=z(J(H.get_normal_episodes,J(lambda e:H.add_this_array(e,L),A5)))
		a=[];c=[];u=[];A6=[];h=W.get(B3)
		if h:
			K[B3]=[];K[f"{V}_{r}"]=B;AG=h['sections']
			for AX in AG:b=H.pool.submit(H.get_ugc_season,AX,h[P],U(AG),L);A6.append(b)
			for b in Bj(A6):
				if b.result()[-1]==0:
					a.insert(0,b.result()[0]);c.insert(0,b.result()[1])
					if not I in b.result()[1]:f=1
				else:a.append(b.result()[0]);c.append(b.result()[1])
				A6.remove(b)
			u.append(T)
			if not f:u+=[A0,A1,A3,f"{V}_{r}"]
		else:
			a=['B站']
			if t:a[0]='互动视频'
		if not h or not f:
			if A5:a=[a[0]];AY=I.join(K[B4]).replace(BX,B);c=[AY]
		if H.userid:
			AZ=f"➕关注${V}_{Z}__1__notplay_follow";Aa=f"➖取关${V}_{Z}__2__notplay_follow";Ab=f"👍点赞${V}_{Z}__1__notplay_like";Ac=f"👍🏻取消点赞${V}_{Z}__2__notplay_like";Ad=f"👍💰投币${V}_{Z}__1__notplay_coin";Ae=f"👍💰💰${V}_{Z}__2__notplay_coin";Ag=f"👍💰⭐三连${V}_{Z}____notplay_triple";A7=[AZ,Ag,Ab,Ad,Ae,Aa,Ac]
			if A4:Ao=f"☆取消收藏${V}_{Z}__{A4}_del_notplay_fav";A7.append(Ao)
			for x in H.userConfig.get(CQ,[]):Ap=x[D].replace(I,A2).replace(w,AJ);Aq=x[C];x=f"⭐{Ap}${V}_{Z}__{Aq}_add_notplay_fav";A7.append(x)
			Ar=I.join(A7);a.insert(1,'做点什么');c.insert(1,Ar)
		if t:c[0]='片头$'+c[0].split(w)[1]
		e[AB]=i.join(a);e[AC]=i.join(c)
		if not h or f:
			y=[Ak+A(V)+'_related","name":"'+AF.replace(AA,AH)+'"}/]相关推荐[/a]']
			if U(j)<60 and j.count(D)<4:j+=An*F(3-U(j)/29)
			y.append(j);As='；'.join(sorted(J(lambda x:Ak+x[A8].replace(AA,AH)+'_clicklink","name":"'+x[A8].replace(AA,AH)+Az+A2+x[A8]+A2+A_,q[E].get('Tags',[])),key=U));y.append(As);l=K.get(A3);AK=K.get(A1)
			if l and AK:l=l.result();e[BZ]=Ba+l[Bz]+Ck+l[Aj]+AU+AU.join(AK.result())
			AL=K.get(A0)
			if AL:y.append(AL.result())
			e[AW]=An.join(y)
			if t:K[CB]=a.copy();K[Bb]=c.copy();K[CC]=e.copy();u+=[T,CB,Bb,CC]
		if not h and not t:H.detailContent_args.pop(L)
		else:
			AM={}
			for(AN,At)in K.items():
				if AN in u:AM[AN]=At
			H.detailContent_args[L]=AM.copy()
		Av={G:[e]};return Av
	def interaction_detailContent(V,array):
		C=array;M=C.get(AI);N=C.get(T);W=C.get(v,0);O=C.get(CD,0);X=C.get(B6);Y=f"https://api.bilibili.com/x/stein/edgeinfo_v2?aid={N}&graph_version={X}&edge_id={O}";F=V._get_sth(Y,Q).json().get(E);R={}
		if F:
			S=C.get(CB).copy();D=C.get(Bb).copy();H=C.get(CC)
			if O:J=A(F[P]).replace(I,A2).replace(w,AJ);D[0]+=f"#{J}${N}_{W}___@{M}"
			else:D[0]=D[0].split(I)[0]
			C[Bb]=D.copy();Z=F['edges'].get('questions',[]);K=[]
			for U in Z:
				a=U.get(P,B)
				for L in U.get('choices',[]):b=L[t];c=L[v];d=L.get('option',B);J=A7.join([a,d]).replace(I,A2).replace(w,AJ);K.append(f"{J}${b}_{c}_interaction@{M}")
			if K:S.insert(1,'选项');D.insert(1,I.join(K))
			else:C.pop(CD);C.pop(v)
			H[AB]=i.join(S);H[AC]=i.join(D);R[G]=[H]
		return R
	def series_detailContent(C,array):
		U='archives';K=array;L,type,V=K.replace('list_',B).split(N);D=1;M=99;A={R:K,AB:'B站'};S=[]
		while Ab:
			W='https://api.bilibili.com/x/series/archives?mid=%s&series_id=%s&pn=%s&ps=%s'%(L,V,D,M);X=C._get_sth(W,Q).json();F=X.get(E)
			if not A.get(O):A[O]=F[U][0][P]
			Y=I.join(J(C.get_normal_episodes,F.get(U)));S.append(Y);Z=F[a][c]
			if M*D>=Z:break
			D+=1
		A[AC]=I.join(S);T=C.up_info[L];A[BZ]=Ba+T[H]+AU+T[AS];b={G:[A]};return b
	def up_detailContent(L,array):
		F=array.replace(Ai,B);L.get_up_info_event.clear();L.pool.submit(L.get_up_info,F);Q=f"关注$_{F}__1__notplay_follow";R=f"取消关注$_{F}__2__notplay_follow";T=f"特别关注$_{F}__-10_special_notplay_follow";U=f"取消特别关注$_{F}__0_special_notplay_follow";P=[Q,T,R,U];P='做点什么$ $$$'+I.join(P);L.get_up_info_event.wait();E=L.up_info[F];M={O:E[H]+Cc,S:E[A5],BZ:Ba+E[H]+AU+E[AS]+'\u3000UID：'+A(F),Y:'👥 '+E[Aj]+'\u3000🎬 '+E[BP]+'\u3000👍 '+E[B_],AW:E[Al]}
		if L.userid:M[AB]='做点什么$$$关注TA';M[AC]=P
		V=L.config[l].get(AN);M[Cl]=A7.join(J(lambda x:Ak+A(F)+N+x[C]+'_getupvideos","name": "'+E[H].replace(AA,AH)+'  '+x[D]+Az+x[D]+A_,V[-1][K]));W={G:[M]};return W
	def setting_login_detailContent(J,key):
		M=key;E='f';D='d';C='c';W=J.cookie_dic_tmp.get(M,B);K=B
		if not W:K=J.get_cookies(M)
		if K:K=f"【{K}】通过手机客户端扫码确认登录后点击相应按钮设置账号"
		else:K='【已扫码并确认登录】请点击相应按钮设置当前获取的账号为：'
		Q={O:'登录与设置',AW:'通过手机客户端扫码并确认登录后，点击相应按钮设置cookie，设置后不需要管嗅探结果，直接返回二维码页面刷新，查看是否显示已登录，已登录即可重新打开APP以加载全部标签'};T=['登录$$$退出登录'];P=[];X=K+'$ ';Y='设置为主账号，动态收藏关注等内容源于此$'+A(M)+'_master_login_setting';Z='设置为备用的VIP账号，仅用于播放会员番剧$'+A(M)+'_vip_login_setting';P.append(I.join([X,Y,Z]));a='点击相应按钮退出账号>>>$ ';b='退出主账号$master_logout_setting';c='退出备用的VIP账号$vip_logout_setting';P.append(I.join([a,b,c]));d=[{E:'主页站点推荐栏',C:Bl,D:{AL:'3图',AQ:'4图','6':'6图','8':'8图','9':'9图'}},{E:'视频画质',C:Bn,D:J.vod_qn_id},{E:'视频编码',C:Bo,D:J.vod_codec_id},{E:'音频码率',C:Ap,D:J.vod_audio_id},{E:'收藏默认显示',C:Bm,D:{L:'默认收藏夹',V:'追番',A0:'追剧'}},{E:'上传播放进度',C:BA,D:{L:'关','15':'开'}},{E:'直播筛选细化',C:Bp,D:{L:'关',V:'开'}}]
		for H in d:
			T.append(H[E]);R=H[D][A(F(J.userConfig[H[C]]))]
			if Ap==H[C]:R=A(R).replace(BV,'k')
			U=['当前：'+R+'$ ']
			for(id,S)in H[D].items():
				if Ap==H[C]:S=A(S).replace(BV,'k')
				U.append(S+w+A(id)+N+H[C]+'_setting')
			P.append(I.join(U))
		Q[AB]=i.join(T);Q[AC]=i.join(P);e={G:[Q]};return e
	def setting_tab_filter_detailContent(K):
		L={O:'标签与筛选',AW:'依次点击各标签，同一标签第一次点击为添加，第二次删除，可以返回到二维码页后重进本页查看预览，最后点击保存，未选择的将追加到末尾，如果未保存就重启app，将丢失未保存的配置'};M=[];P=[];V=[{D:BB,C:'标签'},{D:BC,C:'推荐[分区]'},{D:BD,C:'推荐[排行榜]'},{D:r,C:Ad}]
		for Q in V:
			F=Q[D];M.append(Q[C]);E=K.userConfig.get(A(F)+AD,[]);R=B
			if E:R='【未保存】'
			else:E=K.userConfig.get(F,[])
			if not E:E=K.defaultConfig.get(F)
			if E and Aa(E[0])==d:E=z(J(lambda x:x[D],E))
			S=['当前: '+','.join(E)+'$ ',f"{R}点击这里保存$_{F}_save_setting",f"点击这里恢复默认并保存$_{F}_clear_setting"];T=K.defaultConfig[F].copy()
			if F==r:W=K.userConfig.get(A4,[]);T.extend(W.copy())
			for H in T:
				U=A(H)
				if Aa(H)==d:U=H[D]+Ao+H[C].replace(N,Ao);H=H[D]
				S.append(f"{H}${U}_{F}_setting")
			P.append(I.join(S))
		L[AB]=i.join(M);L[AC]=i.join(P);X={G:[L]};return X
	def setting_liveExtra_detailContent(H):
		Q='_liveFilter_setting';F={O:CS,AW:'点击想要添加的标签，同一标签第一次点击为添加，第二次删除，完成后在[标签与筛选]页继续操作，以添加到直播筛选分区列中'};J=['已添加'];R=H.userConfig.get(A4,[]);E=['点击相应标签(只)可以删除$ #清空$clear_liveFilter_setting']
		for B in R:S=B[C];B=B[D];E.append(B+w+'del_'+B+N+S+Q)
		E=[I.join(E)];T=H.userConfig.get(AO,{})
		for(V,W)in T.items():
			L=W[K][K]
			if U(L)==1:continue
			J.append(V);M=[]
			for P in L:B=A(P[D]).replace(N,'-').replace(I,A2).replace(w,AJ);id=A(P[C]).replace(N,Ao).replace(I,A2).replace(w,AJ);M.append(B+'$add_'+B+N+id+Q)
			E.append(I.join(M))
		F[AB]=i.join(J);F[AC]=i.join(E);X={G:[F]};return X
	def get_all_season(C,season):
		B=season;D=A(B[A8]);E=B[CE];F=C.detailContent_args[B[AI]]
		if D==F[B5]:F[B7]=E
		G=B[h];H=B[Ax][Aw];I={R:A9+D,O:E,S:C.format_img(G),Y:H};return I
	def get_bangumi_section(B,section,array):
		A=section;C=A[P].replace(I,A2).replace(w,AJ);D=A[k]
		if D in[1,2]and U(A['episode_ids'])==0:E=A[BO];F=z(J(lambda x:B.get_normal_episodes(x)[0],J(lambda e:B.add_this_array(e,array),E)));return C,F
	def ysContent(E,this_array):
		r='rating';C=this_array;F=C[AI];X=C.get(T);d=C.get(o)
		if d:F=d;C.pop(o)
		if AT in F:X='ep_id='+F.replace(AT,B);C[o]=F
		else:X='season_id='+F.replace(A9,B)
		F=C[AI];s='https://api.bilibili.com/pgc/view/web/season?{0}'.format(X);D=E._get_sth(s,Q).json().get(u,{});C[B5]=Z=A(D[A8]);e=D[P];C[B7]=D[CE];C[C9]='集'
		if D[k]in[1,4]:C[C9]='话'
		N=D[Ax][Al]
		if r in D:N=A(D[r]['score'])+'分  '+N
		M=D.get(C6)
		if U(M)==1:C[B7]=M[0][CE];M=0
		elif U(M)>1:C[C6]=z(J(E.get_all_season,J(lambda e:E.add_this_array(e,F),M)));N+='  [a=cr:{"id": "'+F+'_getbangumiseasons","name": "'+e.replace(AA,AH)+'"}/]更多系列[/a]'
		f=D.get(BO);g=[]
		for H in D.get('section',[]):
			if H:a=E.pool.submit(E.get_bangumi_section,H,F);g.append(a)
		t=D[h];v=D['share_sub_title'];w=D['publish']['pub_time'][0:4];x=D['evaluate'];j=D[BM];y='▶'+E.zh(j['views'])+'\u3000❤'+E.zh(j['favorites']);V={R:A9+Z,O:e,S:t,BH:v,CA:w,Cl:y,AW:x};V[Y]=N;W=[];K=[];L=[]
		if f:
			b=[];c=[]
			for(l,m)in J(E.get_normal_episodes,J(lambda e:E.add_this_array(e,F),f)):
				if m:b.append(l);c.append(m)
				else:W.append(l)
			if C.get(B2)and c:K.append(A(C[B7])+'【解析】');L.append(I.join(c))
			if b:K.append(A(C[B7]));L.append(I.join(b))
		n=[];p=[]
		for a in Bj(g):
			H=a.result()
			if H:
				if H[0]==BW:W+=H[1]
				else:n.append(H[0]);p.append(I.join(H[1]))
		if W:K.append(BW);L.append(I.join(W))
		K+=n;L+=p;q=C.get(BY)
		if q:K.insert(0,'B站');L.insert(0,q)
		if E.userid:A0='做点什么';A1=f"❤追番剧$__{Z}_add__notplay_zhui#💔取消追番剧$__{Z}_del__notplay_zhui";K.insert(1,A0);L.insert(1,A1)
		V[AB]=i.join(K);V[AC]=i.join(L);A2={G:[V]};return A2
	def get_live_api2_playurl(W,room_id):
		K=room_id;O=[];P=[];G='https://api.live.bilibili.com/xlive/web-room/v2/index/getRoomPlayInfo?room_id={0}&qn=0&platform=web&protocol=0,1&format=0,1,2&codec=0,1&dolby=5&panorama=1'.format(K);Q=W._get_sth(G,AF).json()
		if Q[M]==0:
			H=Q[E].get(Cm,B)
			if H:
				X=H[CF][Cn];C={Bc:{'avc':L,'hevc':V},AX:{'flv':L,'ts':V,'fmp4':A0}};C[AY]=d(J(lambda x:(x[AY],x[Al]),H[CF]['g_qn_desc']));R=[]
				for Y in X:R.extend(Y[AX])
				D={}
				for S in R:
					format=A(S.get('format_name'))
					for T in S[Bc]:
						U=A(T.get('codec_name'));Z=T.get('accept_qn')
						for F in Z:
							G=format+N+U+f"$live_{K}_"+A(F)+N+C[AX][format]+N+C[Bc][U]
							if not D.get(C[AY][F]):D[C[AY][F]]=[]
							D[C[AY][F]].append(G)
				for(a,b)in D.items():O.append(a);P.append(I.join(b))
		c=O,P;return c
	def live_detailContent(C,room_id):
		J=room_id;L=C.pool.submit(C.get_live_api2_playurl,J);W='https://api.live.bilibili.com/room/v1/Room/get_info?room_id='+A(J);N=C._get_sth(W,Q).json();T={}
		if N.get(M)==0:
			B=N[E];K=A(B['uid']);H=C.pool.submit(C.get_up_info,K);X=C.cleanCharacters(B[P]);Y=B.get(CX);Z=B.get(CY);a=B.get('parent_area_name')+'-'+B.get('area_name');D={R:J,O:X,S:Y,BH:a,AW:Z}
			if F(B.get(CT)):D[CA]=B.get('live_time').replace('-','.')
			U=L.result()[0];V=L.result()[1]
			if C.userid:b='关注TA';c='是否关注$ ';d=f"➕关注$_{K}__1__notplay_follow";e=f"➖取关$_{K}__2__notplay_follow";f=[c,d,e];g=I.join(f);U.insert(1,b);V.insert(1,g)
			D[AB]=i.join(U);D[AC]=i.join(V);H=H.result();D[BZ]=Ba+H[Bz]+Ck+C.zh(B.get(Ce))+AU+H[AS];T[G]=[D]
		return T
	search_key=B
	def searchContent(A,key,quick,pg=V):
		E=key
		if not A.session_fake.cookies:A.pool.submit(A.getFakeCookie,Ab)
		for C in A.task_pool:C.cancel()
		if F(pg)>1:return A.get_search_content(key=E,pg=pg,duration_diff=0,order=B,type=p,ps=A.userConfig[Z])
		A.task_pool=[];A.search_key=E;I={p:B,Co:'番剧: ',Cp:'影视: ',C7:'用户: ',AG:'直播: '}
		for(type,J)in I.items():C=A.pool.submit(A.get_search_content,key=E,pg=J,duration_diff=0,order=B,type=type,ps=A.userConfig[Z]);A.task_pool.append(C)
		D={};H=[]
		for C in Bj(A.task_pool):K=C.result().get(G,[]);H.extend(K);A.task_pool.remove(C)
		if U(H):D[G]=H;D[a]=pg;D[f]=9999;D[g]=99;D[c]=999999
		return D
	stop_heartbeat_event=x.Event()
	def stop_heartbeat(A):
		try:
			for B in A.task_pool:B.cancel()
		finally:A.stop_heartbeat_event.set()
	def start_heartbeat(B,aid,cid,ssid,epid,duration,played_time):
		E=played_time;G=F(B.userConfig[BA])
		if not B.userid or not G:return
		H=F((duration-E)/G)+1;I='https://api.bilibili.com/x/click-interface/web/heartbeat';C={T:A(aid),v:A(cid),Bd:A(B.csrf)}
		if ssid:C['sid']=A(ssid);C[o]=A(epid);C[k]=AQ
		D=0;B.stop_heartbeat_event.clear()
		while Ab:
			if D==G or B.stop_heartbeat_event.is_set():E+=D;D=0
			if not D:
				H-=1
				if not H:E=-1;B.stop_heartbeat_event.set()
				C['played_time']=A(E);C=B.encrypt_wbi(**C)[1];B.pool.submit(B._post_sth,url=I,data=C)
				if B.stop_heartbeat_event.is_set():break
			X.sleep(1);D+=1
	wbi_key={}
	def get_wbiKey(A,hour):D='wbi_img';C=A.fetch(CP,headers=A.header);F=C.json()[E][D]['img_url'];G=C.json()[E][D]['sub_url'];H=[46,47,18,2,53,8,23,32,15,50,10,31,58,3,45,35,27,43,5,49,33,9,42,19,29,28,14,39,12,38,41,13,37,48,7,16,24,55,40,61,26,17,0,1,60,51,30,4,22,25,54,21,56,59,6,63,57,62,11,36,20,34,44,52];I=F.split(AR)[-1].split('.')[0]+G.split(AR)[-1].split('.')[0];J=reduce(lambda s,i:s+I[i],H,B)[:32];A.wbi_key={W:J,'hour':hour}
	def encrypt_wbi(D,**C):
		E=AK(X.time());F=X.gmtime(E).tm_hour
		if not D.wbi_key or F!=D.wbi_key['hour']:D.get_wbiKey(F)
		C['wts']=E;G='ABCDEFGHIJK';C['dm_img_list']='[]';C['dm_img_str']=B.join(B8.sample(G,2));C['dm_cover_img_str']=B.join(B8.sample(G,2));C['dm_img_inter']='{"ds":[],"wh":[0,0,0],"of":[0,0,0]}';C=d(sorted(C.items()));C={C:B.join(filter(lambda chr:chr not in"!'()*",A(D)))for(C,D)in C.items()};H=Bk(C);I=hashlib.md5((H+D.wbi_key[W]).encode(encoding=Br)).hexdigest();C['w_rid']=I;return[H+'&w_rid='+I,C]
	def _get_sth(A,url,_type=e,**C):
		E=_type;B=url
		if E==AF and A.session_vip.cookies:D=A.session_vip.get(B,headers=A.header,**C)
		elif E==Q:
			if not A.session_fake.cookies:A.getFakeCookie_event.wait()
			D=A.session_fake.get(B,headers=A.header,**C)
		else:D=A.session_master.get(B,headers=A.header,**C)
		return D
	def _post_sth(A,url,data):return A.session_master.post(url,headers=A.header,data=data)
	def post_live_history(B,room_id):C={Cg:A(room_id),'platform':'pc',Bd:A(B.csrf)};D='https://api.live.bilibili.com/xlive/web-room/v1/index/roomEntryAction';B._post_sth(url=D,data=C)
	def do_notplay(E,ids):
		L='triple';K='fav';H,I,M,G,J,N,F=ids;C={Bd:A(E.csrf)};O=D=B
		if F=='follow':
			if J==C2:C.update({'fids':A(I),'tagids':A(G)});D='https://api.bilibili.com/x/relation/tags/addUsers'
			else:C.update({'fid':A(I),'act':A(G)});D='https://api.bilibili.com/x/relation/modify'
		elif F=='zhui':C.update({A8:A(M)});D='https://api.bilibili.com/pgc/web/follow/'+A(G)
		elif F==Am:C.update({T:A(H),Am:A(G)});D='https://api.bilibili.com/x/web-interface/archive/like'
		elif F==BS:C.update({T:A(H),'multiply':A(G),'select_like':V});D='https://api.bilibili.com/x/web-interface/coin/add'
		elif F==K:C.update({'rid':A(H),k:A0});C[J+'_media_ids']=A(G);D='https://api.bilibili.com/x/v3/fav/resource/deal'
		elif F==L:C.update({T:A(H)});D='https://api.bilibili.com/x/web-interface/archive/like/triple'
		E._post_sth(url=D,data=C)
		if F in[Am,BS,K,L]:C={T:A(H),Bd:A(E.csrf),'csrf_token':A(E.csrf)};D='https://api.bilibili.com/x/web-interface/share/add';E.pool.submit(E._post_sth,url=D,data=C)
		E._refreshDetail()
	def get_cid(D,aid,cid):
		C=cid;G=f"https://api.bilibili.com/x/web-interface/view?aid={aid}&cid={C}";A=D._get_sth(G).json().get(E,{})
		if not C:C=A[v]
		H=A[n];F=B
		if AV in A and C8 in A[AV]:F=D.find_bangumi_id(A[AV])
		return C,H,F
	cookie_dic_tmp={}
	def get_cookies(A,key):
		D='https://passport.bilibili.com/x/passport-login/web/qrcode/poll?qrcode_key='+key;B=A._get_sth(D,Q).json()
		if B[M]==0:
			C=B[E][Ci]
			if not C:A.cookie_dic_tmp[key]=d(A.session_fake.cookies);A.pool.submit(A.getFakeCookie)
			return C
		return'网络错误'
	def set_cookie(A,key,_type):
		D=_type;C=key;F=A.cookie_dic_tmp.get(C,B)
		if not F:
			G=A.get_cookies(C)
			if G:return
		E=A.userConfig.get(j,{});E[D]={AE:A.cookie_dic_tmp.get(C,{})};A.userConfig.update({j:E});A.getCookie(D);A.dump_config()
	def unset_cookie(A,_type):
		C=_type
		if C==AF:A.session_vip.cookies.clear()
		else:A.session_master.cookies=A.session_fake.cookies;A.userid=A.csrf=B
		if C in A.userConfig.get(j,{}):A.userConfig[j].pop(C);A.dump_config()
	def set_normal_default(B,id,type):B.userConfig[type]=A(id);B.dump_config()
	def set_normal_cateManual(B,name,_List,action):
		H=action;F=name;E=_List;G=B.userConfig.get(A(E)+AD)
		if not G:G=B.userConfig[A(E)+AD]=[]
		if H=='save':
			for I in B.defaultConfig[E]:
				if not I in G.copy():B.userConfig[A(E)+AD].append(I)
			B.userConfig[E]=B.userConfig[A(E)+AD].copy();B.userConfig.pop(E+AD);B.dump_config()
		elif H=='clear':B.userConfig[E]=B.defaultConfig[E].copy();B.userConfig.pop(A(E)+AD);B.dump_config()
		else:
			if E==r:
				F=F.split(Ao)
				if U(F)==3:F[1]+=N+A(F[2])
				F={D:F[0],C:A(F[1])}
			if F in G:B.userConfig[A(E)+AD].remove(F)
			else:B.userConfig[A(E)+AD].append(F)
	def add_cateManualLiveExtra(A,action,name,id):
		F='cateManualLive_tmp';G=A.userConfig.get(A4,[])
		if not G:G=A.userConfig[A4]=[]
		if action=='clear':
			for E in G:
				E[C]=E[C].replace(Ao,N)
				if E in A.userConfig.get(r,[]):A.userConfig[r].remove(E)
				if E in A.userConfig.get(F,[]):A.userConfig[F].remove(E)
			A.userConfig.pop(A4)
		elif id in z(J(lambda x:x[C],A.userConfig.get(A4,[]))):
			B={D:name,C:id};A.userConfig[A4].remove(B);B[C]=id.replace(Ao,N)
			if B in A.userConfig.get(r,[]):A.userConfig[r].remove(B)
			if B in A.userConfig.get(F,[]):A.userConfig[F].remove(B)
		else:B={D:name,C:id};A.userConfig[A4].append(B)
		A.dump_config()
	vod_qn_id={'127':'8K','126':'杜比视界','125':'HDR','120':'4K','116':'1080P60帧','112':'1080P+','80':'1080P','64':'720P'};vod_codec_id={'7':'avc','12':'hevc','13':'av1'};vod_audio_id={'30251':'Hi-Res无损','30250':'杜比全景声','30280':Cq,'30232':'132000','30216':'64000'}
	def get_dash_media(E,media,aid,cid,qn):
		I='SegmentBase';C=media;F=A(C.get(t));J=C.get(CG,B);K=C.get('codecs');L=C.get('bandwidth');M=C.get('startWithSap');H=C.get(Cr);O=C[I].get('indexRange');P=C[I].get('Initialization');D=H.split(AR)[0];G=B
		if D==p:Q=C.get('frameRate');R=C.get('sar');S=C.get('width');T=C.get('height');G=f"height='{T}' width='{S}' frameRate='{Q}' sar='{R}'"
		elif D==AZ:U=E.vod_audio_id.get(F,Cq);G=f"numChannels='2' sampleRate='{U}'"
		V=f"{E.localProxyUrl}{D}&aid={aid}&cid={cid}&qn={qn}".replace('&','&amp;');F+=N+A(J);W=f'''
      <Representation id="{F}" bandwidth="{L}" codecs="{K}" mimeType="{H}" {G} startWithSAP="{M}">
        <BaseURL>{V}</BaseURL>
        <SegmentBase indexRange="{O}">
          <Initialization range="{P}"/>
        </SegmentBase>
      </Representation>''';E.pC_urlDic[f"{aid}_{cid}"][D]=C;return W
	def get_dash_media_list(E,media_lis,aid,cid,qn):
		F=media_lis
		if not F:return B
		G=F[0][Cr].split(AR)[0]
		if G==p:I=A(qn);H=A(E.userConfig[Bo])
		else:I=A(E.userConfig[Ap]);H=L
		C={}
		for D in F:
			if G==AZ and not C:C=D
			if A(D[t])==I:
				if not C or A(D[CG])==H:
					C=D
					if A(D[CG])==H:break
		J=f'\n    <AdaptationSet>\n      <ContentComponent contentType="{G}"/>{E.get_dash_media(C,aid,cid,qn)}\n    </AdaptationSet>';return J
	def get_dash(B,ja,aid,cid,qn):
		A=ja;D=A.get(n);G=A.get('minBufferTime');H=B.pool.submit(B.get_dash_media_list,A.get(p),aid,cid,qn);C=A.get(AZ,[]);E=A.get('dolby',{}).get(AZ)
		if E:C=E+C
		F=A.get('flac')
		if Aa(F)==d:C.insert(0,F.get(AZ))
		I=B.pool.submit(B.get_dash_media_list,C,aid,cid,qn);J=f'<MPD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:mpeg:dash:schema:mpd:2011" xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd" type="static" mediaPresentationDuration="PT{D}S" minBufferTime="PT{G}S" profiles="urn:mpeg:dash:profile:isoff-on-demand:2011">\n  <Period duration="PT{D}S" start="PT0S">{H.result()}{I.result()}\n  </Period>\n</MPD>';return J
	def miao(B,m):
		m=A(m).partition('.')[2]
		if U(m)==0:m=BV
		if U(m)==1:m=m+'00'
		if U(m)==2:m=m+L
		return m
	def down_sub(C,url):
		I=C._get_sth(url,Q).json()['body'];E=B;F=1
		for D in I:G=AK(D['from'],3);H=AK(D['to'],3);J=D[Av];K=X.strftime(Bw,X.gmtime(G))+','+C.miao(G);L=X.strftime(Bw,X.gmtime(H))+','+C.miao(H);E+=A(F)+An+K+A7+'-->'+A7+L+An+J+'\n\n';F+=1
		return E
	localProxyUrl='http://127.0.0.1:9978/proxy?do=py&siteType=3&siteKey=py_bilibili&type='
	def get_subs(J,aid,cid):
		L='application/x-subrip';I=[];M=J.encrypt_wbi(aid=aid,cid=cid)[0];N=f"https://api.bilibili.com/x/player/wbi/v2?{M}";D=J._get_sth(N,e).json().get(E)
		if D:
			for K in D[Cs].get('subtitles',[]):
				O=A(K.get('lan_doc',B));C=K.get('subtitle_url')
				if C.startswith('//'):C=CR+C
				C=CK(C);I.append({b:f"{J.localProxyUrl}subtitle&url={C}",H:O,AX:L})
			if I:I.insert(0,{b:B,H:A7,AX:L})
		G=0
		if F(D.get('last_play_cid',0))==F(cid):
			G=F(D.get('last_play_time'))
			if G>0:G=F(G/1000)
		P=D.get(Ct,{}).get(B6,B);return I,G,P
	pC_urlDic={}
	def _get_playerContent(G,result,aid,cid,epid):
		e='durls';c='video_info';W='quality';P=epid;N=cid;L=aid;C=result;G.pC_urlDic[f"{L}_{N}"]=I={**G.pC_urlDic.get(f"{L}_{N}",{}),T:L,v:N,o:P};R=G.userConfig[Bn]
		if P:H='https://api.bilibili.com/pgc/player/web/v2/playurl?aid={}&cid={}&qn={}&fnval=4048&fnver=0&fourk=1&from_client=BROWSER'.format(L,N,R)
		else:
			X={'avid':L,v:N,AY:R,'fnval':4048,'fnver':0,'fourk':1,'from_client':'BROWSER'}
			if not G.session_vip.cookies:X['try_look']=1
			f=G.encrypt_wbi(**X)[0];H=f"https://api.bilibili.com/x/player/wbi/playurl?{f}"
		Q=G._get_sth(H,AF).json();S=B
		if Q[M]==0:
			if E in Q:D=Q[E]
			elif u in Q:
				D=Q[u]
				if c in D:Y=D['view_info']['report'];S=Y[A8];P=Y['ep_id'];D=D[c]
			else:return C
		else:return C
		I[B5]=S;I[o]=P;Z=d(J(lambda x:(x[W],x['new_description']),D['support_formats']));C[b]=[];U=D.get('dash');V=f"&aid={L}&cid={N}&qn="
		if U:
			I[CH]=U;C[AX]=Cu
			for g in U[p]:
				id=g[t];O=Z[id]
				if not O in C[b]:
					H=f"{G.localProxyUrl}dash{V}{id}"
					if id==F(R):C[b]=[O,H]+C[b]
					else:C[b].extend([O,H])
		elif e in D:
			for a in D[e]:
				K=a[W];O=Z[K];H=f"{G.localProxyUrl}durl{V}{K}"
				if K==F(R):C[b]=[O,H]+C[b]
				else:C[b].extend([O,H])
				I[A(K)]=a[Be][0]
		else:K=D[W];I[A(K)]=D[Be][0];C[b]=f"{G.localProxyUrl}durl{V}{K}"
		I[u]={**I.get(u,{}),**C};return C,S,P
	def _refreshDetail(A,t=0):X.sleep(F(t));A.fetch('http://127.0.0.1:9978/action?do=refresh&type=detail')
	def playerContent(C,flag,id,vipFlags):
		C.pool.submit(C.stop_heartbeat);D={};P=B
		if'@'in id:id,P=id.split('@')
		I=C.detailContent_args.get(P,C.detailContent_args);H=id.split(N)
		if U(H)<2:return D
		if AG==H[0]:return C.live_playerContent(id)
		G=H[0];E=H[1]
		if Cj in H:
			if'liveFilter'in H:id=H[2];C.add_cateManualLiveExtra(G,E,id)
			elif E in[BB,r,BC,BD]:S=H[2];C.set_normal_cateManual(G,E,S)
			elif'login'in H:C.set_cookie(G,E)
			elif'logout'in H:C.unset_cookie(G)
			else:C.set_normal_default(G,E)
			return D
		elif'notplay'in H:C.pool.submit(C.do_notplay,H);return D
		elif Ct in H:I[CD]=G;I[v]=E;C.pool.submit(C._refreshDetail);return D
		G,E,J,M,W=id.split(N)
		if not E or not M:E,M,J=C.get_cid(G,E)
		D[BR]='https://api.bilibili.com/x/v1/dm/list.so?oid='+A(E)
		if W:X='https://www.bilibili.com/bangumi/play/ep'+A(J);D[b]=X;D['flag']='bilibili';D[B2]=V;D['jx']=V;D[CI]={AP:C.header[AP]};return D
		Y=C.pool.submit(C.get_subs,G,E);K=C.pC_urlDic.get(f"{G}_{E}")
		if K:D,Q,J=K[u],K[B5],K[o]
		else:D[B2]=L;D[CJ]=B;D[CI]=C.header;D,Q,J=C._get_playerContent(D,G,E,J)
		D['subs'],Z,O=Y.result();a=I.get(B6,B);R=I.get(T)
		if R and G!=R or f"{G}_{E}"in I:I[T]=G;C.pool.submit(C._refreshDetail,2)
		elif O and a!=O:I[B6]=O;C.pool.submit(C._refreshDetail)
		else:c=C.pool.submit(C.start_heartbeat,G,E,Q,J,F(M),Z);C.task_pool.append(c)
		return D
	def live_playerContent(D,id):
		K='url_info';T,I,O,format,G=id.split(N)
		if D.userid and F(D.userConfig[BA])>0:D.pool.submit(D.post_live_history,I)
		P='https://api.live.bilibili.com/xlive/web-room/v2/index/getRoomPlayInfo?room_id={0}&protocol=0,1&format={1}&codec={2}&qn={3}&ptype=8&platform=web&dolby=5&panorama=1'.format(I,format,G,O);J=D._get_sth(P,AF).json();C={}
		if J[M]==0:
			try:H=J[E][Cm].get(CF);G=H[Cn][0][AX][0][Bc][0]
			except:return C
			Q=A(G['base_url']);R=A(G[K][0]['host']);S=A(G[K][0]['extra']);H=R+Q+S;C[b]=H;C[CJ]=B
			if'.flv'in H:C[CJ]='video/x-flv'
		else:return C
		C[B2]=L;C[CI]={Cv:'https://live.bilibili.com',AP:D.header[AP]};return C
	def _testUrl(A,url,id,mediaType):
		B=head(url,headers=A.header,timeout=5).status_code
		if B!=200:A.pC_urlDic[id][mediaType].pop(url)
	def get_fastesUrl(C,ja,id,mediaType):
		E=mediaType;A=ja;D=A
		if Aa(A)==d:C.pC_urlDic[id][E]=D=[A.get('baseUrl',A.get(b,B))];D.extend(A.get('backup_url',[]));C.pC_urlDic[id][Bf]=F(d(J(lambda x:x.split('=')[:2],D[0].split('?')[1].split('&'))).get(Bf,0))
		for G in D:C.pool.submit(C._testUrl,G,id,E)
	def localProxy(D,param):
		N='range';M='application/octet-stream';E=param;A=E.get(k)
		if A==Cs:O=D.down_sub(E[b]);return[200,M,O]
		F=E.get(T);G=E.get(v);H=E.get(AY);C=D.pC_urlDic[f"{F}_{G}"]
		if A=='dash':P=D.get_dash(C[CH],F,G,H);return[200,Cu,P]
		if A in[Be,p,AZ]:
			if A==Be:A=H
			K=AK(X.time());I=C.get(Bf)
			if Aa(C[A])==d or(I-K)%10==0:D.get_fastesUrl(C[A],f"{F}_{G}",A);I=C.get(Bf)
			J=B8.choice(C[A])
			if not J or A!=AZ and I-K<1800:
				D._get_playerContent({},F,G,C[o]);C=D.pC_urlDic[f"{F}_{G}"]
				if A==p:D.get_dash(C[CH],F,G,H)
				D.get_fastesUrl(C[A],f"{F}_{G}",A);J=B8.choice(C[A])
			L=D.header.copy()
			if N in E:L['Range']=E[N]
			Q=D.fetch(J,headers=L,stream=Ab);return[206,M,Q.content]
		return[404,'text/plain',B]
	config={'player':{},l:{BE:[{W:C5,H:'分类',K:[{D:B0,C:B0},{D:BT,C:BT},{D:C0,C:C0},{D:B1,C:B1},{D:C1,C:C1},{D:'我的粉丝',C:'我的粉丝'}]}],AN:[{W:q,H:'别人投稿排序',K:[{D:'最新发布',C:Ay},{D:'最多播放',C:'click'},{D:'最多收藏',C:'stow'},{D:'最早发布',C:CZ},{D:'合集和列表',C:Ca}]}],Ac:[{W:A1,H:'分类',K:[{D:'番剧',C:V},{D:'国创',C:AQ},{D:'电影',C:A0},{D:'电视剧',C:'5'},{D:'纪录片',C:AL},{D:'综艺',C:'7'}]},{W:q,H:'排序',K:[{D:A3,C:A3},{D:'播放数量',C:A0},{D:'更新时间',C:L},{D:'最高评分',C:AQ},{D:'弹幕数量',C:V},{D:'追看人数',C:AL},{D:'开播时间',C:'5'},{D:'上映时间',C:'6'}]},{W:C4,H:'付费',K:[{D:'全部',C:'-1'},{D:'免费',C:V},{D:'付费',C:'2%2C6'},{D:'大会员',C:'4%2C6'}]}],Ae:[{W:q,H:'排序',K:[{D:'收藏时间',C:'mtime'},{D:'播放量',C:BN},{D:'投稿时间',C:'pubtime'}]}],BF:[{W:k,H:'分类',K:[{D:'视频',C:BK},{D:Ad,C:AG},{D:BJ,C:BJ},{D:BQ,C:BQ}]}],Aq:[{W:k,H:'类型',K:[{D:'视频',C:p},{D:'番剧',C:Co},{D:Ac,C:Cp},{D:Ad,C:AG},{D:'用户',C:C7}]},{W:q,H:'视频排序',K:[{D:'综合排序',C:Ch},{D:'最多点击',C:'click'},{D:'最新发布',C:Ay},{D:'最多收藏',C:'stow'},{D:'最多弹幕',C:'dm'}]},{W:n,H:'视频时长',K:[{D:'全部',C:L},{D:'60分钟以上',C:AQ},{D:'30~60分钟',C:AL},{D:'5~30分钟',C:A0},{D:'5分钟以下',C:V}]}]}};header={'Origin':'https://www.bilibili.com',Cv:'https://space.bilibili.com',AP:'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'}