import datetime
from eol_spider.datafilter import DataFilter
import re


def mysql_datetime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def parse_text_by_multi_content(content, delimiter):
    text = ''
    for c in content:
        text = "%s%s%s" % (text, DataFilter.simple_format(c.xpath('.').extract()), delimiter)
    text = text[:-len(delimiter)]
    return text


def get_google_spider_url(origin_url):
    google_spider_url = "https://ipv4.google.com/sorry/index?continue=%s" \
                        "&hl=zh-CN&q=EgSAx54QGIrXgsMFIhkA8aeDS5qZGSfjywVPCg6UscyzSOslsXzgMgFj" % origin_url
    #return google_spider_url
    return origin_url


def get_chinese_by_fullname(fullname, surname_list):
    for name in re.split(",|\s+", fullname):
        name = name.strip()
        if not name:
            continue
        if name in surname_list:
            return "China"
    return ""


