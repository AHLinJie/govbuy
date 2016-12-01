# -*- coding: utf-8 -*-
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
# scrapy crawl dmoz -o items.json -t json 写数据到json文件
import scrapy

from scrapy_djangoitem import DjangoItem
import pdb

# pdb.set_trace()
from nimei.models import HostInfo


def serialize_test(value):
    return 'test-%s' % value


class GovbuyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(scrapy.Item):
    title = scrapy.Field(serializer=serialize_test)


class HostInfoItem(DjangoItem):
    django_model = HostInfo