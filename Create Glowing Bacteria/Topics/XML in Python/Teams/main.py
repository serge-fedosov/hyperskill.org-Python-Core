from lxml import etree

xml_file = "xml_file1.xml"
root = etree.parse(xml_file).getroot()
etree.dump(root)

