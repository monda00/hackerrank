'''
HTML Parser - Part 1
'''

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        for e in attrs:
            print('->', e[0], '>', e[1])

    def handle_endtag(self, tag):
        print('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for e in attrs:
            print('->', e[0], '>', e[1])

if __name__ == '__main__':
    MyParser = MyHTMLParser()
    MyParser.feed(''.join([input().strip() for _ in range(int(input()))]))

