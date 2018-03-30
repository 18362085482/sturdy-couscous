# -*- coding: UTF-8 -*-
"""Simple FunkLoad test

$Id$
"""
import unittest
from random import random
from funkload.FunkLoadTestCase import FunkLoadTestCase
import pprint
import time
from funkload.utils import Data
try:
    # For c speedups
    from simplejson import loads, dumps
except ImportError:
    from json import loads, dumps


class Invoice(FunkLoadTestCase):
    """This test uses the configuration file Simple.conf."""


    def setUp(self):
        """Setting up test."""
        self.server_url = self.conf_get('main', 'invoice_url')


    def assertIssue(self,url,data):
        response = self.post(url,
                             params= Data('application/json', dumps(data)),
                             description="Issue " + data['fplxdm'] + "")
        self.assert_(response.code in [200],"Http request code")
        json_data = loads(self.getBody());
        self.assert_(json_data.has_key("code"), "code exist")
        self.assert_(json_data['code'] == 0 ,"success issue")
        self.assert_(json_data.has_key("fpqqlsh") ,"fpqqlsh exist")
        self.assert_(len(json_data['fpqqlsh']) > 0 ,"fpqqlsh correct")
        return json_data['fpqqlsh']

    def assertQuery(self,url,data):
        response = self.post(url,
                             params= Data('application/json', dumps(data)),
                             description="query " + data['fpqqlsh'] + "")
        self.assert_(response.code in [200],"Http request code")
        json_data = loads(self.getBody());
        self.assert_(json_data.has_key("code"), "code exist")
        self.assert_(json_data.has_key("data"), "data exist")
        self.assert_(json_data['code'] == 0 ,"success query")

        return json_data['data']

    def assertPrint(self,url,data):
        response = self.post(url,
                             params= Data('application/json', dumps(data)),
                             description="Issue " + data['fpqqlsh'] + "")
        self.assert_(response.code in [200],"Http request code")
        json_data = loads(self.getBody());
        self.assert_(json_data.has_key("code"), "code exist")
        self.assert_(json_data['code'] == 0 ,"success print")


    def wtest_issue_025_invoice(self):
        url = self.server_url + '/api/invoice/issue'
        data = {
            'token' : '2cc5e62a58754cf8aae654dfd15a3cbb',
            'operatorId' : 152,
            'unionMerchantId' : '249',
            'device_id' : 'P101173T00099',
            'unionStoreId' : '54',
            'id' : 'FPKJ',
            'fplxdm' : '025',
            'kplx' : 0,
            'yhlx' : 0,
            'ghdwsbh' : '',
            'ghdwmc' : '南京阿有料网络科技有限公司',
            'groups' : [
                {
                    'fphxz' : 0,
                    'spmc' : '汽水',
                    'spsl' : 1,
                    'hsdj' : 103,
                    'hsje' : 103,
                    'sl' : 0.03,
                    'se' : 3
                }
            ],
            'bz' :'备注',
            'skr' :'张收款',
            'fhr' :'张复核',
            'kpr' :'张开票',
            'yfpdm' :'',
            'yfphm' :'',
            'sprsjh' :'13512535412',
        };
        fpqqlsh = self.assertIssue(url,data)
        url = self.server_url + '/api/invoice/detail'
        data = {
            'token': '2cc5e62a58754cf8aae654dfd15a3cbb',
            'fpqqlsh':fpqqlsh
        }
        i = 10
        while(i > 0):
            query_result = self.assertQuery(url,data);
            if(query_result != None and query_result['status'] == 0):
                i = 0
                self.assert_(len(query_result['fphm']) > 0, 'fphm correct')
                self.assert_(len(query_result['fpdm']) > 0, 'fpdm correct')
            elif(query_result != None):
                i = 0
                self.assert_(len(query_result['errmsg']) > 0, 'errmsg correct')
            else:
                i = i - 1
                time.sleep(2)

        # The description should be set in the configuration file

    def wtest_issue_026_invoice(self):
        url = self.server_url + '/api/invoice/issue'
        data = {
            'token' : '2cc5e62a58754cf8aae654dfd15a3cbb',
            'operatorId' : 152,
            'unionMerchantId' : '249',
            'device_id' : 'P101173T00099',
            'unionStoreId' : '54',
            'id' : 'FPKJ',
            'fplxdm' : '026',
            'kplx' : 0,
            'yhlx' : 0,
            'ghdwsbh' : '',
            'ghdwmc' : '南京阿有料网络科技有限公司',
            'ghdwdzdh' : '测试地址',
            'ghdwyhzh' : '6222024301036123261',
            'groups' : [
                {
                    'fphxz' : 0,
                    'spmc' : '汽水',
                    'ggxh' : '测试',
                    'dw' : '个',
                    'spsl' : 2,
                    'dj' : 13.5,
                    'je' : 27,
                    'sl' : 0.03,
                    'se' : 0.81
                }
            ],
            'bz' :'备注',
            'skr' :'张收款',
            'fhr' :'张复核',
            'kpr' :'张开票',
            'yfpdm' :'',
            'yfphm' :'',
            'sprsjh' :'13512535412',
        };
        fpqqlsh = self.assertIssue(url,data)
        url = self.server_url + '/api/invoice/detail'
        data = {
            'token': '2cc5e62a58754cf8aae654dfd15a3cbb',
            'fpqqlsh':fpqqlsh
        }
        i = 10
        while(i > 0):
            query_result = self.assertQuery(url,data);
            if(query_result != None and query_result['status'] == 0):
                i = 0
                self.assert_(len(query_result['fphm']) > 0, 'fphm correct')
                self.assert_(len(query_result['fpdm']) > 0, 'fpdm correct')
            elif(query_result != None):
                i = 0
                self.assert_(len(query_result['errmsg']) > 0, 'errmsg correct')
            else:
                i = i - 1
                time.sleep(2)

        # The description should be set in the configuration file

    def test_issue_007_invoice(self):
        url = self.server_url + '/api/invoice/issue'
        data = {
            'token' : '2cc5e62a58754cf8aae654dfd15a3cbb',
            'operatorId' : 152,
            'unionMerchantId' : '249',
            'device_id' : 'P101173T00128',
            'unionStoreId' : '54',
            'id' : 'FPKJ',
            'fplxdm' : '007',
            'kplx' : 0,
            'yhlx' : 0,
            'ghdwsbh' : '',
            'ghdwmc' : '南京阿有料网络科技有限公司',
            'ghdwdzdh' : '测试地址',
            'ghdwyhzh' : '6222024301036123261',
            'qdbz' : 1,
            'groups' : [
                {
                    'fphxz' : 0,
                    'spmc' : '餐饮服务',
                    'ggxh' : '测试',
                    'dw' : '个',
                    'spsm': '',
                    'spsl' : 2,
                    'dj' : 13.5,
                    'je' : 27,
                    'sl' : 0.03,
                    'se' : 0.81
                }
            ],
            'bz' :'备注',
            'skr' :'张收款',
            'fhr' :'张复核',
            'kpr' :'张开票',
            'yfpdm' :'',
            'yfphm' :'',
            'sprsjh' :'13512535412',
        };
        fpqqlsh = self.assertIssue(url,data)
        url = self.server_url + '/api/invoice/detail'
        data = {
            'token': '2cc5e62a58754cf8aae654dfd15a3cbb',
            'fpqqlsh':fpqqlsh
        }
        i = 10
        while(i > 0):
            query_result = self.assertQuery(url,data)
            if(query_result != None and query_result['status'] == 0):
                i = 0
                self.assert_(len(query_result['fphm']) > 0, 'fphm correct')
                self.assert_(len(query_result['fpdm']) > 0, 'fpdm correct')
                url = self.server_url + '/api/invoice/print'
                self.assertPrint(url,data)
            elif(query_result != None):
                i = 0
                self.assert_(len(query_result['errmsg']) > 0, 'errmsg correct')
            else:
                i = i - 1
                time.sleep(2)

        # The description should be set in the configuration file


if __name__ in ('main', '__main__'):
    unittest.main()
