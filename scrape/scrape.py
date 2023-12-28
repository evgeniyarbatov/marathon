import csv
import os
import re

import requests 
from bs4 import BeautifulSoup

OUTPUT_DIR = './data'

configs = [
    {
        'url': 'https://www.alltime-athletics.com/mmaraok.htm',
        'extra': ['Men']
    },
    {
        'url': 'https://www.alltime-athletics.com/wmaraok.htm',
        'extra': ['Women']
    },
]

if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

outfile = open(
    OUTPUT_DIR + "/marathon.csv", 
    "w",
)
writer = csv.writer(outfile)

for config in configs:
    r = requests.get(config['url'])
    soup = BeautifulSoup(r.content, 'html.parser')

    contents = soup.find_all('pre')
    for content in contents:
        for line in content.text.splitlines():
            entry = line.strip()
            if entry:
                row = re.split(r" {2,}", entry)
                row += config['extra']
                writer.writerow(row)