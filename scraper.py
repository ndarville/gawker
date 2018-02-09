"""
NUM_PAGES:
    Number of Gawker pages, 1 to 9469.

    Configure manually from shell with argument;
    eg: `python scraper.py 10` scrapes first 10 pages.

    This simplifies performance testing;
    eg: `time python scraper.py 10` on UNIX with `time`.

scrape_links():
    Iterates through pages and saves JSON object of Gawker article links.

Todo:
    * scrape_articles() using the JSON object
    * scrape_images()
    * Performance optimizations
    * Save progress; resume feature
    * Validation and tests

Use:
    `python scraper.py`
"""
import errno
import json
import os
import sys

from pyquery import PyQuery
import requests


NUM_PAGES = int(sys.argv[1]) if len(sys.argv) == 2 else 9469
HAS_LINKS = NUM_PAGES == 9469
OUTPUT_DIR = "output"
LINKS_FILE = "links.json"

site = "http://gawker.com"
urls = ["http://gawker.com/page_%d" % (page) for page in xrange(1, NUM_PAGES+1, 1)]

def buildLinks(urls):
    "Get article permalinks from web document. Add to list `links`."

    links = []
    pattern = "section.main article header h1 a"

    for url in urls:
        anchors = PyQuery(url, site)(pattern).make_links_absolute()
        links += [{"url": a.attrib["href"]} for a in anchors] # List of dicts
        # links += [a.attrib["href"] for a in anchors] # List of strings

    return links

def saveJson(data, file):
    "Save JSON object to .json."

    try:
        os.makedirs(OUTPUT_DIR)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    print "Saving to " + file + " ..."
    with open(OUTPUT_DIR + "/" + file, "w") as out_f:
        json.dump(data, out_f)

def scrape_links():
    "Scrape link data from web documents and save as JSON."

    if not HAS_LINKS:
        print "Building list of links ..."
        links = buildLinks(urls)
        print "Finished building list."
        saveJson(links, LINKS_FILE)
    else:
        print "List of links already exists; loading links."
        links = json.load(open(OUTPUT_DIR + "/" + LINKS_FILE))

def main():
    return scrape_links()

if __name__ == "__main__":
    main()
