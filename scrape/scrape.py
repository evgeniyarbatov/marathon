import csv
import os
import re

import requests 
from bs4 import BeautifulSoup

OUTPUT_DIR = '../data'

urls = [
    'https://www.alltime-athletics.com/mmaraok.htm',
    'https://www.alltime-athletics.com/wmaraok.htm',
]

if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

outfile = open(
    OUTPUT_DIR + "/marathon.csv", 
    "w",
)
writer = csv.writer(outfile)

for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    contents = soup.find_all('pre')
    for content in contents:
        for line in content.text.splitlines():
            entry = line.strip()
            if entry:
                row = re.split(r" {2,}", entry)
                writer.writerow(row)