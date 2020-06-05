from selenium import webdriver
driver = webdriver.Chrome("C:/Users/민소연/Downloads/chromedriver_win32_1/chromedriver.exe") #본인의 chrome driver 주소

def notice():
	driver.get('https://it.jbnu.ac.kr/it/index.do')

	print('<학과공지>\n')

	for i in range(5):
		# xpath '//*[@id="recentBbsArtclObj_681_1050"]/li[%d]/a'안의 %d값을 1씩 올려 순차적으로 공지를 가져온다.
		text = driver.find_element_by_xpath('//*[@id="recentBbsArtclObj_681_1050"]/li[%d]/a'%(i+1)).text
		title = text[:-6]
		date = text[-5:]
		url = driver.find_element_by_xpath('//*[@id="recentBbsArtclObj_681_1050"]/li[%d]/a'%(i+1)).get_attribute("href")
		print(title)
		print('게시일:', date)
		print('바로가기:', url)
		print('\n')

notice()
