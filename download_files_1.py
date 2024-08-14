import requests
import os

#wanted to write a script instead of downloading manually cause why not haha

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

# Download KANJIDIC2
kanjidic2_url = "https://www.edrdg.org/kanjidic/kanjidic2.xml.gz"
download_file(kanjidic2_url, "kanjidic2.xml.gz")

# Download SVG files (example, actual process might differ)
svg_url = "https://github.com/KanjiVG/kanjivg/releases/download/r20220427/kanjivg-20220427-main.zip"
download_file(svg_url, "kanjivg.zip")

# Unzip files
import gzip
import shutil
with gzip.open('kanjidic2.xml.gz', 'rb') as f_in:
    with open('kanjidic2.xml', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

import zipfile
with zipfile.ZipFile('kanjivg.zip', 'r') as zip_ref:
    zip_ref.extractall('kanjivg')