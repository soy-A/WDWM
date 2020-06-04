from selenium import webdriver
import getpass
import time

driver = webdriver.Chrome('C:/Users/민소연/Downloads/chromedriver_win32_1/chromedriver.exe') #본인 chrome driver 주소
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
    driver.execute_script(subjectURL[i])
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="center2"]/div/div[2]/div/div[5]/div[2]/table/thead/tr/th[1]/a').send_keys('\n') #레포트에 들어감
    time.sleep(2)
    workclass = driver.find_elements_by_class_name('b02')
    n = 1
    for j in workclass:
        line = ((n-1)//5)+2
        font = j.find_elements_by_tag_name('font')
        for a in font:
            progress = a.get_attribute('color')
            if progress == '#517DE0':
                worktitle = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[%d]/td[2]'%line).text
                deadline = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[%d]/td[3]/font/b'%line).text
                submit = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[%d]/td[4]'%line).text
                print(worktitle, deadline, submit)
        n += 1
    driver.back()
    time.sleep(3)
