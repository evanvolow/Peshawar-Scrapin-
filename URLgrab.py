import requests, re
from bs4 import BeautifulSoup

searchURL="https://www.cia.gov/library/readingroom/advanced-search-view?keyword=afghanistan&ds_field_pub_date_op=between&ds_field_pub_date[min]=1979&ds_field_pub_date[max]=1989"
searchResults=requests.get(searchURL, verify=False)
