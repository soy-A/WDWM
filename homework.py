
from selenium import webdriver
driver = webdriver.Chrome("C:/Users/민소연/Downloads/chromedriver_win32/chromedriver.exe")

def HW():
	driver.get('https://ieilms.jbnu.ac.kr/login.php?errorcode=4')

	id = '201812755'
	pw = 'dkssud99!!'

	driver.find_element_by_xpath('//*[@id="input-username"]').send_keys(id)
	driver.find_element_by_xpath('//*[@id="input-password"]').send_keys(pw)
	driver.find_element_by_xpath('//*[@id="region-main"]/div/div/div/div[1]/div[1]/div[2]/form/div[2]/input').click()

	driver.find_element_by_xpath('//*[@id="yui_3_17_2_1_1590469146124_129"]').click()
	driver.find_element_by_xpath('//*[@id="yui_3_17_2_1_1590469146124_207"]').click()

	courses = driver.find_elements_by_class_name("coursefullname")

	list = ['레포트', '과제']
	for course in courses:
		course.click()
		current = driver.find_element_by_class_name("section main clearfix current")
		activesections = current.find_element_by_class_name("activityinstance")
		for activesection in activesections:
			for text in list:
				if text in activesection.text:
					target = activesection

		target.click()

HW()