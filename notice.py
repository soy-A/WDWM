from selenium import webdriver
#from beautifulsoup4 import BeautifulSoup	
driver = webdriver.Chrome("C:/Users/민소연/Downloads/chromedriver_win32/chromedriver.exe")

def notice():
	driver.get('https://it.jbnu.ac.kr/it/index.do')

	for i in range(5):
		text = driver.find_element_by_xpath('//*[@id="recentBbsArtclObj_681_1050"]/li[%d]/a'%(i+1)).text
		title = text[:-5]
		date = text[-5:]
		url = driver.find_element_by_xpath('//*[@id="recentBbsArtclObj_681_1050"]/li[%d]/a'%(i+1)).get_attribute("href")
		print(title, url, date)

notice()