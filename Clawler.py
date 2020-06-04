from bs4 import BeautifulSoup
import requests
import random
import time
from tqdm import tqdm, trange
import re

base_url = 'http://www.jbnu.ac.kr/kor/?menuID=452'
response = requests.get(base_url)

if response.status_code == 200:
    html = BeautifulSoup(response.text,'html.parser')
    #menu9841_obj223 > div._fnctWrap._articleTable > form:nth-child(2) > table > tbody > tr:nth-child(1) > td._artclTdTitle > a > strong
    print("[상단 고정 공지]")
    title = html.select('#print_area > div.page_list > table > tbody > tr:nth-child(1) > td.left > span > a')[0].get_text(strip=True)
    print(title)
    print("\n")
    title=html.select('#print_area > div.page_list > table > tbody > tr:nth-child(2) > td.left > span > a')[0].get_text(strip=True)
    print(title)
    date=html.select('#print_area > div.page_list > table > tbody > tr:nth-child(2) > td:nth-child(6)')[0].get_text(strip=True)
    print(date)
    title=html.select('#print_area > div.page_list > table > tbody > tr:nth-child(3) > td.left > span > a')[0].get_text(strip=True)
    print(title)
    date=html.select('#print_area > div.page_list > table > tbody > tr:nth-child(3) > td:nth-child(6)')[0].get_text(strip=True)
    print(date)