from html.parser import HTMLParser


class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]


if __name__ == '__main__':
    html = '\n'.join([input() for _ in range(int(input()))])
    parser = MyHtmlParser()
    parser.feed(html)
    parser.close()
