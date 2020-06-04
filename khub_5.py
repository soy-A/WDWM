from selenium import webdriver
import getpass
import time

driver = webdriver.Chrome('C:/chromedriver_win32 (4)/chromedriver.exe')
driver.get('https://jbnu.khub.kr/')


id = input("학번을 입력하세요 : ")
pw = getpass.getpass("비밀번호를 입력하세요 : ")
driver.find_element_by_name('login').send_keys(id)
driver.find_element_by_name('passwd').send_keys(pw)
driver.find_element_by_xpath('//*[@id="loginform"]/table/tbody/tr[1]/td[2]/input').click()
time.sleep(3)   #3초 기다리기

subjects = driver.find_elements_by_class_name("leftGroupMenu_div")  #khub에 있는 사용자가 수강중 or 수강완료한 과목들 모두 찾아와서 리스트로 만듦
subjectName = []    #과목명을 가지는 리스트 생성
subjectURL = [] #과목 url을 가지는 리스트 생성
for i in subjects:  #subjects리스트를 for문으로 돌면서 과목명과 과목 url을 가져옴
    name = i.get_attribute('title') 
    url = i.get_attribute('onclick')
    if name.split(' ')[0] == '2020-1':  #이번학기 과목만 subjectName과 subjectURL에 추가하기 위한 조건문
        subjectName.append(name.split(' ')[1])
        subjectURL.append(url)

for i in range(len(subjectName)):   #subjectName리스트의 크기만큼 for문을 돌려서 각 과목의 페이지 들어가서 과제 정보를 가져옴
    print(subjectName[i])   #과목명 출력
 
need = input('과목명을 입력하세요: ')
for i in range(len(subjectName)):
    if need == subjectName[i]:
        driver.execute_script(subjectURL[i])
        for j in range(5): #레포트에서 진행중 색을 통해 구별하는 것은 마지막에 추가 예정, 임시로 5개까지 돌려보았으나.......왜 안될까요
            driver.find_element_by_xpath('//*[@id="center2"]/div/div[2]/div/div[5]/div[2]/table/thead/tr/th[1]/a').click() #여기서 오류예상!
            driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[%d]/td[2]/a'%(j+2)).click()
            title = driver.find_element_by_tag_name('b').text
	          date =  driver.find_element_by_class_name("viewi01").text
	          info = driver.find_element_by_xpath('//*[@id="center"]/div/div[2]/div/div[7]/div').text
            print(title)
            print(date)
	          print(info)
            print('\n')
            driver.back()
        driver.back()
        
