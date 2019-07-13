class Taobao:

    def __init__(self):
        # 登录的URL，获取token
        self.request_url = 'https://login.taobao.com/member/login.jhtml'
        # 通过st实现登录的URL
        self.st_url = 'https://login.taobao.com/member/vst.htm?st={st}'
        #  用户中心地址
        self.user_url = 'https://i.taobao.com/my_taobao.htm'
        #  代理IP地址，防止自己的IP被封禁
        self.proxy_ip = 'http://120.193.146.97:843'
        #  登录POST数据时发送的头部信息
        self.request_headers = {'Host': 'login.taobao.com',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
                                'Referer': 'https://login.taobao.com/member/login.jhtml',
                                'Content-Type': 'application/x-www-form-urlencoded', 'Connection': 'Keep-Alive'}

        # 用户名
        self.username = 'xxx@xxx.com'
        # ua字符串，经过淘宝ua算法计算得出，包含了时间戳,浏览器,屏幕分辨率,随机数,鼠标移动,鼠标点击,其实还有键盘输入记录,鼠标移动的记录、点击的记录等等的信息
        self.ua = '089#6o5vOJvX+p/vyJ+evvvvv964Zx59o/eBpRDo3gsRlVypemTq+lp56psnhm5sL5/TvRMoZ//llHppexSA/99V6N9d3uCs5+K+v+7akvvvyFmNxoT5G0y/ZdMM6m0mGJlo3kJi5J5vR/EKvvvwb9ghRluiJwlHYHN43dhi+x5rYx0kvlvesIJvvxprxNge+hXxpxKzcV8iKq05ZuT03LK+v+7akvvvyFbFxoT5G0y/ZdMM6m0mGJlo3kJi5J5vR/EKvvvwDhjhRluiJwlHYHN43dhi+x5rYx0Vvlv5CtGNMx8+v+uMO/p9uE2COPovypleYeYY+8KOYBJ+v+24FVhTZxriDpLjmSNDWm8AHc7PEBUsV+QPdu8+v+uMX/p9kLpCOPovZ5ZhYK7goZKOYoK+v+paZNvvy/oCxoT5GXSR6V0wYV/zGJkDvlv62X0xkt96vJ3GZv5vaVNMkud3Breg/VynptGv2p22kFpOhIxbKNMiEpJVvlv5CtGNMYv+vvLasgQ1nG7xyYN+vveBZ6C4Q7NTvlv0vvVKd+kpyxlvvKgK96/PiJvvmNJ/7uLMvvVhV+kp35lvvKgK96/jscv+v1pFSd/wMWE5lVlbVHkBypEe3sElZuQA/pUrRTM49uspFuplpn4BypEe3sE36zDIFvg7l5v2Sm+usv6lO9QoSIsv6v5QKoDb9l6d/R6a7LJVEmjl/x5wz791bs2c6LVQ+lKs19IVSHr1/meeV4YPy+/V879d5W/I9l6d/Qv+7LDvln7KVmI87NJ68wDFK6lQaJ5spRJlXLvV+Qpusk5SZ7lpepvF/oVQ+l6Lv5TQZXgpv46s85QQRvKRy97t5XglvJpTKv5BR68Rlx27ukTl7J/x5HKsKsOpvNenposw7eeu+ula5HvOM/s56wlbZsQBFwDG/v2Gcmpk/uJQsHJI9pwp37L+ZoQBFwDjup+GMz95FuM5pHDIa95+csIQ3+O/+NpmQoI27oDaa4+3875oKPSxDsDeWuQw97gdpL7SSmLp9dpvlV4fZ9y5v7+0pWRPs5vTvs8m9ojpv46l8TbQRv6fhL+lZuQA/pUrRTM45689vL9gFlYPc7Uky7TY8zDI9l6d/QKsSulpv46s8vRQ9N+Vb/JYhsdFVv7mpoDJ7+8bvs9/O+VX5vK9epy9KkIHp+p7/+Eu5689v45vks8Hzo/V879Jse88vJ8IQFMkzovV+QlJvuZ87Jev34pyYsVQ+lZuKL5L92/x+4EF9aQp77Z9yvDuK+X0vlvclvVxCdouvJKEQnkGvlvRrGGorJLYnJ5v+RyBvlQDvlv62X09kjS6vJhSnv5vVOOXa5AOklKxxeN+vv44XdwY8TTVvHfDvlv62X04kTL6vJyy3v5vR4eEVSHChn2oQ9qrPv6LYNu+ABESRI0W+DRtvJ5v+cGqMcvfvlv/tY79sQf7WfSglx+xxHd61ZuVRdMVvlv5CtGNMx8+v+uMO/p9es6COPovZ5ZhYK7goZKOYNK+vvkqCtVNyJ5v93o2s/pYv4Uz15vNlNg0dFB5NL0zyJ5v93H2s/pYvRUz15vwp+T2T009JL0z3v5vR4eDRGljhn2oQK32P+oAydtKAFEPhw5K9Wb6vJ5v+cGqMcvkvlvesIJvvxpBWNge+hXxpxKzcV8iKq05ZuT03JK+vvkqCtVN5J5vR/EKvvvwDtghRluiJwlHYHN43dhi+x5rYx0kvlvesIJvvxpIZlge+hXxpxKzcV8iKq05ZuT03LK+v+7akvvvyFEPxoT5G0y/ZdMM6m0mGJlo3kJi5J5vR/EKvvvwEdghRluiJwlHYHN43dhi+x5rYx0kvlvesIJvvxpt8vge+hXxpxKzcV8iKq05ZuT03mJ+v+24FWuTUBriDpdpXUNV8kT5AM/n1oSYRNF+AN=='
        # 密码，在这里不能输入真实密码，淘宝对此密码进行了加密处理，256位，此处为加密后的密码
        self.password2 = '98d8979ad859f27838ba5aa299217fb4edf7b46f052c1330bf9fe57d594a09e5ee9402fc9bb86d83d9c0d5b50b13e93a8679e2699a17a87993d435e25ac81b01c74d68a3eb6460b0a1e05068d337567be980911e0dcaa6ef2b8141aeb21cf547c8a77c2aa9ff6ea724e6f2df838c3680cf56ba8e0484da15051bdd27eaee5a20'
        self.post = {
            ‘TPL_username’: ‘asi1225’
‘TPL_password’:
ncoSig:
ncoSessionid:
ncoToken: 568a4c01590f5471ba7fb82f469daf0463650d7a
slideCodeShow: false
useMobile: false
lang: zh_CN
loginsite: 0
newlogin: 0
TPL_redirect_url: https://www.taobao.com/
from: tb
fc: default
style: default
css_style:
keyLogin: false
qrLogin: true
newMini: false
newMini2: false
tid:
loginType: 3
minititle:
minipara:
pstrong:
sign:
need_sign:
isIgnore:
full_redirect:
sub_jump:
popid:
callback:
guf:
not_duplite_str:
need_user_id:
poy:
gvfdcname: 10
gvfdcre: 68747470733A2F2F6C6F67696E2E74616F62616F2E636F6D2F6D656D6265722F6C6F676F75742E6A68746D6C3F73706D3D61323177752E3234313034362D676C6F62616C2E373630373037343436332E31372E343163613535653548376668473626663D746F70266F75743D7472756526726564697265637455524C3D68747470732533412532462532467777772E74616F62616F2E636F6D253246
from_encoding:
sub:
TPL_password_2: 1b1376fa2d0ed0e5f6dd3b5f7e69e890bab2de70802ffeb8f61c77bff8eee439b3f3fd171b87600173109109399a451f15a34cf38e3221297c543a405ef4028bfcd82bccbea32e3df1d69a5e17f5456f075fd217674c016fd24d58520a118409ef3a3fb57d3faf4ecac52226777d05fa782c63f1fabb494642ea7678fab3bfab
loginASR: 1
loginASRSuc: 1
allp:
oslanguage: zh-CN
sr: 1920*1080
osVer:
naviVer: chrome|70.0353867
osACN: Mozilla
osAV: 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36
osPF: Win32
miserHardInfo:
appkey: 00000000
nickLoginLink:
mobileLoginLink: https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/&useMobile=true
showAssistantLink:
um_token: HV02PAAZ0b017d587760bce05bea3b5507430b02999999
ua: 113#I3SjUffFfepKpf4AGkFRzXbxbsk0S3Qo+6f6bFbOdPuPV+V/kgi5on47BIPXjWRD1PF6HWiYyKE1DNDok0MaGuix6R6YkFRo1PFYfW44dKuqoyFNJI/no7okbYomk0+1wKkWbD44sPkAWsSDf9NboYbxYkHFSCu+OsvRGp7NdokXDXk6xWRSCGJeG74OkWRD1PfW1FJLsPDZDdp1nYPwoswQbYxYk05DbKf680i4eK1Z4yFIk0nwWX1xnX5Yk0I/fbfA9Hr/0ypG6s4r+QdoAlyR2Mav8iQcz9kNFerJrs3G2NB7CGSOHWgA9WddOyCxDSwLkqpNuYqzNeOxmtaYDgJfxFAWyhns3BaGALTLp+MnFiGGt52olW7p3gO0BnBfCxOEbM+em7TbywsbvX8g0pYnylK31kvvO8qRYl/gnLh1UlJekWt7L4NWFZighCXcyfpWCkCNuZy5Zjm9WyxkBZsyDzeVNFPDFfLKeqry6pZP9pZOY/B6NDmRS2nYQZ8vrJAaWXFozz7iRu3LYfkDg4rAf8+IWijsmKca42IIfxfQeZqaBCQYEAc/AqAYd4JSMjdf7I6qLcTAUFtxCACMoVYRiad7G6EOeXRYLKvbHev4fA308mNZ1gs1HSQP6Hl2kcvs/B2lCtM+aeNy6NNesCq/cib/KQkQnjxZ6J4QNF9P4IivQyB4kcSoBVqNVSkTnT7DOzvKgEBEBRJZ5KT2UiIsyUBex4kI5otjz6XerlUGbcN1wJNbyZaQF6WtDhrdWOfXvj7eKbybQlJwHVSHtOQ7HdC2Co5wAz/nedUoeOu+P2SjL+5m3jmMZGgRe0ufLP8oKbPKwPO37AaiV9LuThp+Mack0hZigCC/tVmwTlDtErt2jmqF1qWs10AlgrjlMBqDDZlE4J4O661x/WB9sQFoRx4PurawL+GaO/UIcGYoL+7Z7Sr6vSrQcCngcQ0b31RB+iIbW+RJ2sApJIgsxNvxcEOovAf8mNLuuxaPoW24L3126OCm}
