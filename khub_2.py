from selenium import webdriver
import getpass
#일단 이산수학만 지정해놓고 실행
driver = webdriver.Chrome('C:\chromedriver.exe')
driver.get('https://jbnu.khub.kr/')

id = input("학번을 입력하세요 : ")
pw = getpass.getpass("비밀번호를 입력하세요 : ")
driver.find_element_by_name('login').send_keys(id)
driver.find_element_by_name('password').send_keys(pw)
driver.find_element_by_xpath('//*[@id="loginform"]/table/tbody/tr[1]/td[2]/input').click()
#driver.find_element_by_xpath('//*[@id="boardAbox"]/form/table/tbody/tr[1]/td[2]/div/table/tbody/tr/td[2]/div[2]/a/div[1]/b').click()
driver.find_element_by_class_name("font-size:14px;font-family:Malgun Gothic, gulim, dotum;font-weight:bold;padding:0 5px;")
driver.find_element_by_xpath('//*[@id="center2"]/div/div[2]/div/div[5]/div[2]/table/thead/tr/th[1]/a').click()
driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[4]/td[2]/a').click()

body_element = driver.find_element_by_tag_name("body")
print("[과제 정보]")
print(body_element[1].text)
