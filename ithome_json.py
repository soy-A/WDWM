from selenium import webdriver
import json
import threading

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

it_dict = []

def notice():
	driver = webdriver.Chrome(executable_path = '/workspace/chromedriver', options = options)

	driver.get('https://it.jbnu.ac.kr/it/index.do')

	for i in range(5):
		text = driver.find_element_by_xpath('//*[@id="recentBbsArtclObj_681_1050"]/li[%d]/a'%(i+1)).text
		title = text[:-6]
		date = text[-5:]
		url = driver.find_element_by_xpath('//*[@id="recentBbsArtclObj_681_1050"]/li[%d]/a'%(i+1)).get_attribute("href")
		it_dict.append({'title':title, 'date':date, 'url':url})
		print(title,date,url)
	driver.quit()

def toJson(it_json):
    with open('ithome.json','w',encoding='utf-8') as file:
        json.dump( it_json,file,ensure_ascii=False,indent='\t')

class Repeat:

	def __init__(self):
		pass

	def Reithome(self):
		notice()
		toJson(it_dict)
		threading.Timer(3600,self.Reithome).start()

re = Repeat()
re.Reithome()
