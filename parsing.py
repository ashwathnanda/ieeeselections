import xml.etree.ElementTree as ET
import urllib
from HTMLParser import HTMLParser
a=input("enter Url ")
tag=input("enter tag to be displayed")
s=urllib.urlopen(a)
h=s.read()
parser.feed(h)

ans=h.getElementsByTagName(tag)
print ans

#http://www.diveintopython.net/html_processing/extracting_data.html
#https://docs.python.org/2/library/htmlparser.html
