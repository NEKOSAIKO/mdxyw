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
           
        }
        #提交的信息
        payload={
       
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
