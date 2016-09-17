from lxml import etree
from lxml import html
import  requests

def getDescription(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    #print url;
    return tree.xpath('//div[@id="more_info_sheets"]/div[@id = "idTab1"]/p/span/text()')[0]

page = requests.get('http://www.fishing-mart.com.ua/2-fishing-mart-spinningovaya-ribalka?n=20&id_category=2')
tree = html.fromstring(page.content)
productImages = tree.xpath('//ul[@id = "product_list"]/li/div[@class="center_block"]/a/img/@src')
productNames = tree.xpath('//ul[@id = "product_list"]/li/div[@class="center_block"]/h3/a/text()')
productPrices = tree.xpath('//ul[@id = "product_list"]/li/div[@class="right_block"]/div/span[@class = "price"]/text()')
productLinks = tree.xpath('//ul[@id = "product_list"]/li/div[@class="center_block"]/h3/a/@href')
productDescriptions = map(lambda link: getDescription(link), productLinks)

root = etree.Element('data')
doc = etree.ElementTree(root)
for i in range (0,20):
    productElement = etree.SubElement(root, 'product')
    productTitle = etree.SubElement(productElement, 'title')
    productTitle.text = productNames[i]
    productDesc = etree.SubElement(productElement, 'description')
    productDesc.text = productDescriptions[i][2:]
    productImg = etree.SubElement(productElement, 'image')
    productImg.text = productImages[i]
    productPrice = etree.SubElement(productElement, 'price')
    productPrice.text = productPrices[i]
    i +=1
doc.write('task3.xml', xml_declaration=True, encoding='utf-8')