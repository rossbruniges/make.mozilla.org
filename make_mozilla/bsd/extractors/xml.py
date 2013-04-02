from lxml import etree
parser = etree.XMLParser(recover=True)


def constituent_email(xml):
    print '### XML ###'
    print xml
    print '###'
    doc = etree.fromstring(xml, parser)
    return doc.xpath('/api/cons/cons_email/email')[0].text
