from lxml import etree

xml_string = input()

root = etree.fromstring(xml_string)
print(len(root.getchildren()), len(root.keys()))
