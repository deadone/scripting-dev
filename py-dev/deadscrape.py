#!/bin/python
# deadscrape.py
# author: dead1
# Scrape Emails From Webpages
import re
import sys
from requests_html import HTMLSession

# add ability to crawl full webpage
# multi threaded
print("[*] Dead1's Webpage Email Scraper v1.1")
if len(sys.argv) > 1:
	url = sys.argv[1]
	print("[*] Scraping Webpage: " + url)
else:
	print("[X] Usage: dscraper.py http://google.ca")
	
# the credit for this regex:
# https://stackoverflow.com/questions/62141910/accelerate-2-loops-with-regex-to-find-email-address-on-website
EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

# initiate an HTTP session
session = HTMLSession()
r = session.get(url)

# add detection functionality
# uncomment next (3) lines to use
# "[*] JavaScript Enabled."
# for JAVA-Script driven websites
# r.html.render()

print("[*] Discovered Emails:")
for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
    print(re_match.group())
