![header](https://raw.githubusercontent.com/Sushchyk/DBLabs/master/img/kpi.png)
<h1 align="center">Лабораторна робота №1
<h2 align="center">Вивчення базових операцій обробки XML-документів </h2>
<p align="right">Виконав студент групи КП-42 Сущик Андрій</p>
<p align="right">Варіант 19</p>

## Вміст XSL-файлу
```
<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>Catalog</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
        <th>Title</th>
        <th>Description</th>
        <th>Image</th>
        <th>Price </th>
    </tr>
    <xsl:for-each select="data/product">
    <tr>
        <td><xsl:value-of select="title"/></td>
        <td><xsl:value-of select="description"/></td>
        <td>
            <img>
                <xsl:attribute name="src">
                    <xsl:value-of select="image"/>
                </xsl:attribute>
            </img>
        </td>
        <td><xsl:value-of select="price"/></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>
</xsl:stylesheet>
```
## Текст програми
task1.py
```
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

```
task2.py
```
from lxml import etree
tree = etree.parse('task1.xml')
for item in tree.xpath('//page'):
    fragments = item.getchildren()
    count = 0
    for fragment in fragments:
        if fragment.get("type") == "text":
            count += 1
    print item.get("adress") + " : " +  str(count)
```
task3.py
```
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
```
## Копії екранних форм 
![Screenshot 1](https://raw.githubusercontent.com/Sushchyk/DBLabs/master/lab1/screenshots/1.png)
![Screenshot 1](https://raw.githubusercontent.com/Sushchyk/DBLabs/master/lab1/screenshots/2.png)
## Вміст XHTML-файлу

```
<?xml version='1.0' encoding='UTF-8'?>
<?xml-stylesheet type="text/xsl" href="catalog.xsl"?>
<data><product><title>Rich Sport Fishing Hunter...</title><description> новый модельный ряд карбоновых спиннингов, предназначенных для джиговой ловли.</description><image>http://www.fishing-mart.com.ua/746-6133-home/rich-sport-fishing-hunter-hi-modulus.jpg</image><price>$624.00</price></product><product><title>Panacea Marauder Fat</title><description>семейство троллинговых глубоководных воблеров крупного размера.</description><image>http://www.fishing-mart.com.ua/56-6175-home/panacea-marauder-fat.jpg</image><price>$260.00</price></product><product><title>Mikado Mind 100</title><description>азка-спрей для технического поддержания эксплуатационных характеристик безынерционных катушек.</description><image>http://www.fishing-mart.com.ua/137-6188-home/mikado-mind-100.jpg</image><price>$144.56</price></product><product><title>Tica Reel Grease</title><description> смазка для катушек.</description><image>http://www.fishing-mart.com.ua/1276-4885-home/tica-reel-grease-smazka-dlya-katushek.jpg</image><price>$39.00</price></product><product><title>Fanatik Boxer</title><description> съедобный силиконовый виброхвост от украинского производителя. Изготовляется из мягкого силикона с добавлением ароматических солей, которые при проводке создают ароматический шлейф позади приманки, тем самым привлекая хищника и принуждая его атаковать приманку.</description><image>http://www.fishing-mart.com.ua/753-6230-home/fanatik-boxer.jpg</image><price>$28.60</price></product><product><title>Fanatik Viper</title><description> съедобный силиконовый твистер с массивным аппетитным телом.</description><image>http://www.fishing-mart.com.ua/1372-6244-home/fanatik-viper.jpg</image><price>$28.60</price></product><product><title>Fanatik Lobster</title><description> съедобная силиконовая приманка, чем-то похожая на рака.</description><image>http://www.fishing-mart.com.ua/1373-6256-home/fanatik-lobster.jpg</image><price>$28.60</price></product><product><title>Fanatik Larva</title><description> съедобная силиконовая приманка в форме личинки стрекозы.</description><image>http://www.fishing-mart.com.ua/1374-6268-home/fanatik-larva.jpg</image><price>$28.60</price></product><product><title>Fanatik Raider</title><description> съедобная силиконовая приманка в форме рака.</description><image>http://www.fishing-mart.com.ua/1375-6280-home/fanatik-raider.jpg</image><price>$28.60</price></product><product><title>Fanatik Dagger</title><description> съедобная силиконовая приманка в форме небольшого червяка.</description><image>http://www.fishing-mart.com.ua/1376-6289-home/fanatik-dagger.jpg</image><price>$28.60</price></product><product><title>Бахилы ОЗК (БЦК)</title><description> военные средства химзащиты активно применяются в рыбалке. Данные бахилы популярны у зимних рыбаков. Одеваются поверх зимних сапог для предотвращения намокания последних. </description><image>http://www.fishing-mart.com.ua/522-5891-home/bahily-ozk-bck.jpg</image><price>$72.80</price></product><product><title>Fanatik Goby</title><description> силиконовая приманка, по форме напоминающая бычка.</description><image>http://www.fishing-mart.com.ua/1384-6335-home/fanatik-goby.jpg</image><price>$35.10</price></product><product><title>Fanatik FO-3315 офсетный крючок</title><description> офсетные крючки корейского произодства от ТМ FANATIK.</description><image>http://www.fishing-mart.com.ua/1388-6373-home/fanatik-fo-3315-ofsetnyy-kryuchok.jpg</image><price>$15.60</price></product><product><title>Fanatik FD-1140 двойной крючок</title><description> двойные крючки для силиконовых приманок, изготовленные в Корее. С виду очень похожие на Kumho.</description><image>http://www.fishing-mart.com.ua/1389-6374-home/fanatik-fd-1140-dvoynoy-kryuchok.jpg</image><price>$22.88</price></product><product><title>Ryobi Ecusima Vi</title><description> бюджетная спиннинговая катушка. Хотя, понятие "бюджетная" у Ryobi достаточное относительное. Потому что </description><image>http://www.fishing-mart.com.ua/898-3332-home/ryobi-ecusima-vi.jpg</image><price>$915.20</price></product><product><title>Condor липгрип (челюстной захват)</title><description> липгрип, челюстной захват рыбы. </description><image>http://www.fishing-mart.com.ua/1391-6376-home/condor-lipgrip-chelyustnoy-zahvat.jpg</image><price>$130.00</price></product><product><title>Mistrall поводки спиннинговые 7x7</title><description>strall спиннинговые поводки на щуку - продукция от польской фирмы Mistrall.</description><image>http://www.fishing-mart.com.ua/1398-6392-home/mistrall-povodki-spinningovye.jpg</image><price>$8.32</price></product><product><title>Rubicon стальные поводки 7x7</title><description> поводки на щуку из 49 микронитей в нейлоновой оболочке.</description><image>http://www.fishing-mart.com.ua/1399-6393-home/rubicon-stalnye-povodki-7x7.jpg</image><price>$7.28</price></product><product><title>Winner поводки на щуку 1x7 с...</title><description> металлические поводки из семи нитей, покрытые нейлоновой оболочкой.</description><image>http://www.fishing-mart.com.ua/1400-6394-home/winner-povodki-na-shuku-1x7-s-amerikankoy.jpg</image><price>$6.24</price></product><product><title>Winner поводки на щуку 1x7 с...</title><description> металлические поводки с нейлоновой оболочкой.</description><image>http://www.fishing-mart.com.ua/1401-6395-home/winner-povodki-na-shuku-1x7-s-plastinchatym-karabinom.jpg</image><price>$5.20</price></product></data>
```
