from selenium import webdriver
import getpass
#일단 이산수학만 지정해놓고 실행
driver = webdriver.Chrome('C:/chromedriver_win32 (4)/chromedriver.exe')
driver.get('https://jbnu.khub.kr/')

id = input("학번을 입력하세요 : ")
pw = getpass.getpass("비밀번호를 입력하세요 : ")
driver.find_element_by_name('login').send_keys(id)
driver.find_element_by_name('passwd').send_keys(pw)
driver.find_element_by_xpath('//*[@id="loginform"]/table/tbody/tr[1]/td[2]/input').click()
subject_list = driver.find_element_by_xpath('//*[@id="boardAbox"]/form/table/tbody').find_elements_by_class_name('leftGroupMenu_div')
print(len(subject_list))
#del subject_list[0]
#subject = []
#url = []
#for i in subject_list:
#    subject = i.find_element_by_tag_name('tbody').find_element_by_tag_name('div').get_attribute('title')
#    print(subject)

#name = input("원하는 과목의 이름을 입력하시오: ")

##for i in subject_list:
# #  if subject == name:
#         #driver.get(i.find_element_by_xpath("font-size:14px;font-family:Malgun Gothic, gulim, dotum;font-weight:bold;padding:0 5px;")) 수정 
#         driver.get(i.find_element_by_xpath('//*[@id="center2"]/div/div[2]/div/div[5]/div[2]/table/thead/tr/th[1]/a'))
#         driver.get(i.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[4]/td[2]/a'))
#         body_element = driver.find_element_by_tag_name("body")
#         break
#print("[과제 정보]")
#print(body_element[1].text)





