from selenium import webdriver
import getpass
import time

driver = webdriver.Chrome('C:/chromedriver.exe')
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
    driver.execute_script(subjectURL[i])    #해당 과목 페이지로 이동 ※ driver.execute_script("javascript문")는 자바스크립트로 작성된 코드 실행하는 함수 
    #과제 가지고 오는 코드 써야함!!
    driver.back()   #뒤로가기 subjectURL[i]는 url이 아니라 클릭 명령을 수행하는 자바스크립트 문법이므로 
                        #driver.back()을 통해 뒤로가기를 해서 내 강의 페이지로 가야함


