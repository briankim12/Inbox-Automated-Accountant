#!/usr/bin/env python
# coding=utf-8
import lxml.html
from demo_data import HTML


def lxml_handler(event, context):
    print event, context
    try:
        etree = lxml.html.document_fromstring(HTML)
        links = etree.xpath('//a')
        print 'Test Succeeded: found {} links with xpath'.format(len(links))
        return True
    except Exception, e:
        print 'Test Failed: {}'.format(e)
        return False
