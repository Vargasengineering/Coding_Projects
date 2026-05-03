
### 04/28/2026
### Samuel Vargas
### This is a program that grabs the text from the Analogman King of Tone Waitlist website and outputs info as to who gets to place an order for a KoT based on the date they got on the waitlist
### The current wait time to order a KoT is about 5-6 years now

### Libraries

from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen



def main():

    ### This section grabs the text from the Analogman KoT page and turns it into data

    url = "https://www.analogman.com/kotdelay.htm"
    page = urlopen(url)

    html_bytes = page.read()
    web_page = html_bytes.decode("utf-8")
    web_page = BeautifulSoup(web_page, 'html.parser')

    ### Turns processed web page data into a string
    text = web_page.find('p')
    text = text.get_text()

    ### Truncates text string and gives final output
    start_index = text.find('K')
    end_index = 135 + 1
    print(text[start_index: end_index])




main()
