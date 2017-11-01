import re
import urllib
from urllib.parse import urlparse,urljoin,unquote

__author__ = 'dusc'
from bs4 import BeautifulSoup

class HtmlParser(object):
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is  None:
            return

        soup = BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r'/item'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return  new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = unquote(page_url)
        title_node = soup.find("dd",class_='lemmaWgt-lemmaTitle-title').find("h1")

        res_data['title'] = unquote(title_node.get_text());
        print(res_data)
        return res_data