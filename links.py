from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


def read_links(path):
    file1 = open(path, 'r')
    links = file1.readlines()
    tmp = list()
    for x in links:
        if re.search('^#', x) is None:  # Use '#' at the beginning of a line for line comment in links.txt
            tmp.append(x)
    return tmp


def get_links():
    links = read_links('links.txt')
    for x in links:
        try:
            url_proto_domain = re.search('(http[s]?://)?([^/\s]+)', x).group(0)
            req = Request(x)
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "html.parser")

            links = []
            for link in soup.findAll('a'):
                url_path = str(link.get('href'))
                if re.search('^(http|https)://', url_path) is not None:
                    links.append(url_path)
                if re.search('^/', url_path) is not None:
                    links.append(url_proto_domain + url_path)

            print(x)
            print(links)
            print(len(links))
            print()
        except:
            print("An exception occurred for website: {}".format(x))
            print()
