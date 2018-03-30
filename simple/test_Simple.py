# -*- coding: iso-8859-15 -*-
"""Simple FunkLoad test

$Id$
"""
import unittest
import random
import string

import time
from funkload.FunkLoadTestCase import FunkLoadTestCase

class Simple(FunkLoadTestCase):
    """This test use a configuration file Simple.conf."""

    def setUp(self):
        """Setting up test."""
        counturl = 6
        randnum = random.randint(0,counturl-1)
        urlname = "url" + str(randnum)
        self.server_url = self.conf_get('main', urlname)

    def randomnumlist(self):
        charstore = string.ascii_lowercase + string.digits
        numlist= ""
        for x in range(31):
            a = random.randint(0, 35)
            numlist = numlist + charstore[a]
        return numlist

    def randid(self):
        randid=self.randomnumlist()
        return randid

    def ransign(self):
        ransign=self.randomnumlist()
        return ransign

    def test_simple(self):
        # The description should be set in the configuration file
        server_url = self.server_url
        # begin test ---------------------------------------------
        ret = self.get(server_url, description='Get URL')
        self.assert_(ret.code in [200, 301, 302], "expecting a 200 or 301 or 302")
        # print ret
        # end test -----------------------------------------------

    def test_simple_2(self):
        server_url = "http://106.14.13.223:8081/callback/weimo"
        body = {
            "id":self.randid(),
            "topic":"o2o_meal_order",
            "event":"add",
            "version":1,
            "sign":self.ransign(),
            "test":"false",
            "business_id":"57208957",
            "public_account_id":"55983882",
            "msg_body":"{\"merchantId\":55983882,\"orderId\":125192,\"orderNo\":\"68821705240000076589\",\"orderStatus\":0,\"storeId\":15334}"
        }
        ret = self.post(url=server_url, params=body, description="POST URL")
        print 1111111,self.getBody()


if __name__ in ('main', '__main__'):
    unittest.main()