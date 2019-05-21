'''
Detect HTML Tags, Attributes and Attribute Values
'''

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for e in attrs:
            print('->', e[0], '>', e[1])

if __name__ == '__main__':
    MyParser = MyHTMLParser()
    MyParser.feed(''.join([input().strip() for _ in range(int(input()))]))

