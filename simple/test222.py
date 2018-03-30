# coding=utf-8

import commands
import re
import time
import unittest

class test222(unittest.TestCase):
    def md5(self,str):
        import hashlib
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()

    def timenow(self):
        timenow=str(time.time())
        return timenow

    def auth(self,body,passwd,timenow):
        str=body+passwd+timenow
        auth= self.md5(str)
        return auth

    def request(self,body):
        geturl = "http://106.14.13.223:8084"
        url = geturl + '/api/transferinfo'
        ContentType = 'Content-Type:application/xml'
        CurlCmd = 'curl -v -d ' + '%r' % body + ' -H ' + '%r' % ContentType  + " " + url
        return CurlCmd

    def request_login(self,body,Timestamp,Authorization):
        geturl = "http://106.14.13.223:8084"
        url = geturl + '/api/transferinfo'
        ContentType = 'Content-Type:application/xml'
        CurlCmd='curl -v -d ' + '%r' % body + ' -H ' + '%r' % ContentType + ' -H' + '%r' % Timestamp + ' -H' '%r' % Authorization + " " + url
        return CurlCmd

    def test_login(self):
        timenow=self.timenow()
        body="<?xml version=\'1.0\' encoding=\'utf-8\'?><business id=\'LOGIN\'><body><input><username>test1</username><deviceno>P101173T00149</deviceno></input></body></business>"
        passwd=self.md5("123456")
        auth= self.auth(body,passwd,timenow)
        Timestamp = 'Timestamp:'+timenow
        Authorization = 'Authorization:'+auth

        request_login=self.request_login(body,Timestamp,Authorization)
        (status, output) = commands.getstatusoutput(request_login)
        # print output
        pattern = re.compile("<returnmsg>\S+</returnmsg>")
        match = pattern.findall(output)


        if match[0]=='<returnmsg>\xe7\x99\xbb\xe5\xbd\x95\xe6\x88\x90\xe5\x8a\x9f</returnmsg>':
            print "登录成功"
        else:
            raise Exception('登录失败')


    def test_loginout(self):
        body='<?xml version="1.0" encoding="utf-8"?><business id="LOGINOUT"><body><input><token>bf03f76efc1ad68e46fcc500fafa</token></input></body></business>'
        request_loginout = self.request(body)
        print request_loginout
        (status, output) = commands.getstatusoutput(request_loginout)
        pattern = re.compile("<returnmsg>\S+</returnmsg>")
        match = pattern.findall(output)

        if match[0]=='<returnmsg>\xe9\x80\x80\xe5\x87\xba\xe6\x88\x90\xe5\x8a\x9f\xef\xbc\x81</returnmsg>':
            print "\n退出成功"
        else:
            raise Exception("退出失败")

    def test_Rolesearch(self):
        body='<?xml version="1.0" encoding="utf-8"?><business id="ROLESEARCH"><body><input><appcode></appcode><token>29ea0056c557c25e0684aac4b4cc03a0</token></input></body></business>'
        request_rolesearch = self.request(body)
        print request_rolesearch

    def test_StoreSearch(self):
        body='<?xml version="1.0" encoding="utf-8"?><business id="STORESEARCH"><body><input><type>0</type><merchantid>249</merchantid><storeid></storeid></input></body></business>'
        request_StoreSearch = self.request(body)
        print request_StoreSearch

    def test_MerchantSearch(self):
        body='<?xml version="1.0" encoding="utf-8"?><business id="MERCHANTSEARCH"><body><input><type>0</type><nsrsbh>110101201601010014</nsrsbh><merchantid>1</merchantid></input></body></business>'
        request_MerchantSearch = self.request(body)
        print request_MerchantSearch

    def test_DeviceSearch(self):
        body='<?xml version="1.0" encoding="utf-8"?><business id="DEVICESEARCH"><body><input><type>3</type><searchid>P101173T00149</searchid></input></body></business>'
        request_DeviceSearch = self.request(body)
        print request_DeviceSearch

    def test_UpdatePassword(self):
        body='<?xml version="1.0" encoding="utf-8"?><business id="UPDATEPASSWORD"><body><input><username>test1</username><password>fcea920f7412b5da7be0cf42b8c93759</password></input></body></business>'
        timenow = "1496303816"
        passwd = self.md5("123456")
        auth = self.auth(body, passwd, timenow)
        print 11111111
        print timenow
        print 22222222
        print auth

        request_UpdataPassword = self.request(body)
        print request_UpdataPassword



if __name__ in ('main', '__main__'):
    unittest.main()

