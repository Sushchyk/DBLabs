from lxml import html
from lxml import etree
import requests
import sys

rootUrl = 'http://www.shkola.ua'


def getTextOrImage(urls):

    root = etree.Element('data')
    doc = etree.ElementTree(root)

    text = []
    images = []

    for item in urls:
        page = requests.get(item)
        tree = html.fromstring(page.content)
        pageElement = etree.SubElement(root, 'page', adress=item)
        text = tree.xpath('//*[text() and not(self::script)]')
        images = tree.xpath('//img')

        for item in images:
            imageFragment = etree.SubElement(pageElement, 'fragment', type = 'image')
            imageFragment.text = item.get("src")

        for item in text:
            if item.text != None:
                textFragment = etree.SubElement(pageElement, 'fragment', type='text')
                textFragment.text = item.text

        doc.write('task1.xml', xml_declaration=True, encoding='utf-8')

def parsePage():
    page = requests.get(rootUrl)
    tree = html.fromstring(page.content)
    links = tree.xpath('//a[@href]')
    i = 0
    count = 0
    length = len(links)
    urls = []
    while (count != 20 and i < length):
        hrefValue = links[i].get("href")
        if hrefValue[0] == '/':
            urls.append(rootUrl + hrefValue)
            print urls[len(urls) - 1]
            count += 1
        i += 1
    getTextOrImage(urls)

parsePage()





