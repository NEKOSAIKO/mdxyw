#-*- coding:utf-8 -*-
__author__ = 'Zach_z'

import time
import requests
import re
class Login:

    #初始化
    def __init__(self):
        #检测间隔时间，单位为秒
        self.every = 15

    #模拟登录
    def login(self, print_self=None):
        print (self.getCurrentTime(), "拼命连网中...")

        url="http://211.138.135.94/a70.htm"
        #消息头
        headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'max-age=0',
            'Content-Length': '145',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'program=lymx; vlan=0; getUserName=2021509; ISP_select=3; md5_login2=2021509%7C2021509; save_DDDDD=2021509; save_upass=2021509; ip=172.16.26.65; userIp=172.16.26.65; PHPSESSID=2pk01rqsm37i6tbeujpjnb3l20',
            'Host': '211.138.135.94',
            'Origin': 'http://211.138.135.94',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://211.138.135.94/a70.htm',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31',
        }
        #提交的信息
        payload={
            'DDDDD': '2021509',
            'upass': '2021509',
            'R1': '0',
            'R2': '',
            'R3': '3',
            'R6': '0',
            'para': '00',
            '0MKKey': '123456',
            'bttonClicked': '',
            'redirect_url': '',
            'err_flag': '',
            'username': '',
            'password': '',
            'user': '',
            'cmd': '',
            'Login': ''

        }
        try:
            requests.post(url,headers=headers,data=payload)
            print_self.getCurrentTime(),u'连上了...现在开始看连接是否正常'
        except:
            print("error")
    #判断当前是否可以连网
    def canConnect(self):
        try:
            q=requests.get("http://www.baidu.com",timeout=5)
            m=re.search(r'STATUS OK',q.text)
            print(m)
            if m:
                return True
            else:
                return False
        except:
            print ('error')
            return False

    #获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

    #主函数
    def main(self):
        print (self.getCurrentTime(), u"Hi，欢迎使用自动登陆系统")
        while True:
            self.login()
            while True:
                can_connect = self.canConnect()
                if not can_connect:
                    print (self.getCurrentTime(),u"断网了...")
                    self.login()
                else:
                    print (self.getCurrentTime(), u"一切正常...")
                time.sleep(self.every)
            time.sleep(self.every)


login = Login()

login.main()
