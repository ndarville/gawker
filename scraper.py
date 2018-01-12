"""
NUM_PAGES: Number of Gawker pages, 1 to 9469.

scrape_links():
    Iterates through pages and saves JSON object of Gawker article links.

Todo:
    * scrape_articles() using the JSON object
    * scrape_images()
    * Performance optimizations
    * Validation and tests

Use:
    `python scraper.py`
"""
import errno
import json
import os

from pyquery import PyQuery as pq
import requests


NUM_PAGES = 9469
OUTPUT_DIR = "output"
SITE = "http://gawker.com"

urls = ["http://gawker.com/page_%d" % (page) for page in xrange(1, NUM_PAGES+1, 1)]

def fetchDoc(url):
    "Fetch requested document from URL."
    response = requests.get(url)

    return pq(response.content)

def scrape_links():
    "Scrape link data from documents and save to JSON object."
    links = []
    for url in urls:
        doc = fetchDoc(url)
        links += [{"url": a.attrib["href"]} for a in doc("section.main article header h1 a")]

    try:
        os.makedirs(OUTPUT_DIR)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    with open(OUTPUT_DIR + "/links.json", "w") as out_f:
        json.dump(links, out_f)

def main():
    return scrape_links()

if __name__ == "__main__":
    main()
