from xml.dom import minidom
import xml.etree.ElementTree as et
import json

Minidom     = False
ElementTree = False
JSON = True

if Minidom:
    # Recupere le fichier et le traite comme un XML
    mydoc = minidom.parse("/Users/floriandelrieu/OneDrive/Cours/Python/Tutos/TEST_xml/items.xml")
    # Recupere les items du ficher XML
    items = mydoc.getElementsByTagName('item')

if ElementTree:
    mydoc2 = et.parse("/Users/floriandelrieu/OneDrive/Cours/Python/Tutos/TEST_xml/items.xml")

if JSON:
    data = {'a':(10, 20, 'blah'), 'b':(20, 70, 'blah2')}
    with open("/Users/floriandelrieu/OneDrive/Cours/Python/Tutos/TEST_xml/data.xml","w") as fp:
        json.dump(data,fp)