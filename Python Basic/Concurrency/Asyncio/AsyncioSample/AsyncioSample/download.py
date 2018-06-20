import json
import logging
import os
from pathlib import Path
from urllib.request import urlopen, Request

logger = logging.getLogger(__name__)
#imgur_url = 'https://api.imgur.com/3/gallery'
imgur_url = 'https://api.imgur.com/3/gallery/random/random/2'

def get_image_links(all_links):
    for x in ['.jpg,', '.gif', '.png']:
        if x in all_links:
            return x

def get_links(client_id):
   headers = {'Authorization': 'Client-ID {}'.format(client_id)}
   req = Request(imgur_url, headers=headers, method='GET')

   with urlopen(req) as resp:
       data = json.loads(resp.read().decode('utf-8'))

   all_links = list(map(lambda item: item['link'], data['data']))
   img_links = filter(get_image_links, all_links)
   return img_links

def download_link(directory, link):
   logger.info('Downloading %s', link)
   download_path = directory / os.path.basename(link)

   with urlopen(link) as image, download_path.open('wb') as f:
       f.write(image.readall())

def setup_download_dir():
   download_dir = Path('images')

   if not download_dir.exists():
       download_dir.mkdir()

   return download_dir
