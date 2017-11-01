import urllib.request

__author__ = 'dusc'


class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        response = urllib.request.urlopen(url,timeout=2)
        if response.getcode() != 200:
            return None

        return response.read()
