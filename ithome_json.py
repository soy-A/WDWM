from selenium import webdriver
import json
import threading

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path = '/workspace/chromedriver', options = options)

from collections import OrderedDict

file_data = OrderedDict()

def notice():
	driver.get('https://it.jbnu.ac.kr/it/index.do')

	data = {}
	for i in range(5):
		text = driver.find_element_by_xpath('//*[@id="recentBbsArtclObj_681_1050"]/li[%d]/a'%(i+1)).text
		title = text[:-6]
		date = text[-5:]
		url = driver.find_element_by_xpath('//*[@id="recentBbsArtclObj_681_1050"]/li[%d]/a'%(i+1)).get_attribute("href")
		file_data["title"] = title
		file_data["date"] = date
		file_data["url"] = url
		data[i]=file_data
	with open('ithome.json', 'w', encoding = "utf-8") as make_file:
		json.dump(data, make_file, ensure_ascii=False, indent="\t")

class Repeat:

	def __init__(self):
		pass

	def Reithome(self):
		notice()
		threading.Timer(3600,self.Reithome).start()

re = Repeat()
re.Reithome()
