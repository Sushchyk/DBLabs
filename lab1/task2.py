from lxml import etree
tree = etree.parse('task1.xml')
for item in tree.xpath('//page'):
    fragments = item.getchildren()
    count = 0
    for fragment in fragments:
        if fragment.get("type") == "text":
            count += 1
    print item.get("adress") + " : " +  str(count)