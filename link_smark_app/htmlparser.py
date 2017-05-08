from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.a=[]
        self.n=[]
        self.x=0
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0]=='href':
                if (attr[1][:3] == 'htt' or attr[1][:3] == 'www'):
                    self.a.append(attr[1])
                    self.x=1
    def handle_data(self, data):
        if self.x==1:
            self.n.append(data)
            self.x=0
    def namez(self):
        return self.n
    def attrits(self):
        return self.a
