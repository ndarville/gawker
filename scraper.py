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


NUM_PAGES = 1
OUTPUT_DIR = "output"
LINKS_FILE = "links.json"

urls = ["http://gawker.com/page_%d" % (page) for page in xrange(1, NUM_PAGES+1, 1)]

def fetchDoc(url):
    "Fetch requested document from URL."

    response = requests.get(url)

    return pq(response.content)

def buildLinks(urls):
    "Get article permalinks from web documents."

    links = []
    for url in urls:
        doc = fetchDoc(url)
        links += [{"url": a.attrib["href"]} for a in doc("section.main article header h1 a")]

    return links

def saveJson(data, file):
    "Save JSON object to .json."

    try:
        os.makedirs(OUTPUT_DIR)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    with open(OUTPUT_DIR + "/" + file, "w") as out_f:
        json.dump(data, out_f)

def scrape_links():
    "Scrape link data from web documents and save as JSON."

    links = buildLinks(urls)
    saveJson(links, LINKS_FILE)

def main():
    return scrape_links()

if __name__ == "__main__":
    main()
