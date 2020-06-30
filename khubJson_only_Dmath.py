from selenium import webdriver
import getpass
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path = '/workspace/chromedriver', options = options)
driver = webdriver.Chrome('C:/Users/이미르/Downloads/chromedriver_win32_1/chromedriver.exe') #본인 chrome driver 주소
driver.get('https://jbnu.khub.kr/')

khub_dict = []
def toJson(khub_dict):
    with open('khub_DMath.json','w',encoding = 'utf-8') as file:
        json.dump( khub_dict,file,ensure_ascii=False,indent='\t')

id = #학번
pw = #비번
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
    if subjectName[i] == "이산수학":
        driver.execute_script(subjectURL[i])
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="center2"]/div/div[2]/div/div[5]/div[2]/table/thead/tr/th[1]/a').send_keys('\n') #레포트에 들어감
        time.sleep(2)
        workclass = driver.find_elements_by_class_name('btr')
        n = 1
        for j in workclass:
            line = ((n-1)//5)+2
            worktitle = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[%d]/td[2]'%line).text
            deadline = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[%d]/td[3]'%line).text
            submit = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[%d]/td[4]'%line).text
            print(worktitle, deadline, submit)
            n += 5
        
        driver.back()
        driver.back()
        time.sleep(3)
