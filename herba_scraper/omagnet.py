
import re
from datetime import datetime
import requests
from bs4 import BeautifulSoup

from herba_scraper.utils import Utils


class Omagnet:
    def __init__(self):
        pass

    def fetch(self, omagnet_url):
        response = requests.get(omagnet_url)
        return self.parse(response.content)

    def parse(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        data = {}
        data['link'] = self.parse_magnet_link(soup)
        data['info_hash'] = Utils.get_magnet_info_hash(data['link'])
        data['filesize'], data['date'] = self.parse_magnet_info(soup)
        data['files'] = self.parse_files(soup)
        return data

    def parse_magnet_link(self, soup):
        input = soup.find(
            'input', {'id': 'input-magnet', 'class': 'form-control'})
        if input:
            return input['value']
        else:
            return None

    def parse_magnet_info(self, soup):
        dds = soup.select('dl.dl-horizontal.torrent-info dd')
        if len(dds) < 3:
            return 0, None

        size = Utils.convert_size(dds[1].text.strip())
        if re.match(r"(\d{4})-(\d{2})-(\d{2})", dds[2].text.strip()):
            date =  datetime.strptime(dds[2].text.strip(), "%Y-%m-%d %H:%M:%S")
            return size, date
        else:
            return size, None

    def parse_files(self, soup):
        files = []
        for tr in soup.select('table.table.table-hover.file-list tbody tr'):
            file = {}
            td = tr.select('td')
            if len(td) < 2:
                continue
            file['name'] = td[0].text.strip()
            file['size'] = Utils.convert_size(td[1].text.strip())
            files.append(file)
        return files
