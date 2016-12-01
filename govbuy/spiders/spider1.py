# coding=utf-8
from __future__ import unicode_literals, absolute_import
import logging
import scrapy

logger = logging.getLogger(__name__)
from ..items import HostInfoItem
from ..items import HostInfo


def test_info():
    print '=-' * 100
    print HostInfo.objects.all()


class GovBuySpider(scrapy.Spider):
    name = 'govbuy'
    host = 'http://www.shucheng.gov.cn'

    def start_requests(self):
        urls = [
            '{0}/tmp/xxgklist2.shtml?unitsId=1&action=list&types=2&SS_Path=/-012-148-052&SSIDS=2012',
        ]
        for url in urls:
            yield scrapy.Request(url=url.format(self.host), callback=self.prase)

    def prase(self, response):
        # filename = 'test.html'
        test_info()
        links = response.xpath('//li[re:test(@class, "mc$")]//a')
        for index, link in enumerate(links):
            shref = link.xpath('@href').extract()
            sname = link.xpath('text()').extract()

            href = shref[0] if shref else None
            name = sname[0].strip() if sname else None
            print u'name: %s \n url: %s ' % (name, href)
            # x = HostInfoItem()
            # x['name'] = name
            # x.save()

            # with open(filename, 'wb') as f:
            # f.write(response.body)
            # self.log('save file %s' % filename)
