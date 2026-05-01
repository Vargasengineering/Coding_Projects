
### 04/28/2026
### Samuel Vargas
### This is a program that grabs the text from the Analogman King of Tone Waitlist website and outputs info as to who gets to place an order for a KoT based on the date they got on the waitlist
### The current wait time to order a KoT is about 5-6 years now

### Libraries

from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen



def main():

    url = "https://www.analogman.com/kotdelay.htm"
    page = urlopen(url)
    print(page) ## for debugging

    intel_bytes = page.read()
    web_page = intel_bytes.decode("utf-8")
    print(web_page) ## for debugging

    ## Test Line
    ## Test Line 2


main
