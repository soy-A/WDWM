from selenium import webdriver
import getpass

driver = webdriver.Chrome('C:\chromedriver.exe')
driver.get('https://ieilms.jbnu.ac.kr/login.php')

id = input("학번을 입력하세요 : ")
pw = getpass.getpass("비밀번호를 입력하세요 : ")
driver.find_element_by_name('username').send_keys(id)
driver.find_element_by_name('password').send_keys(pw)
driver.find_element_by_xpath('//*[@id="region-main"]/div/div/div/div[1]/div[1]/div[2]/form/div[2]/input').click()
courseList = driver.find_element_by_class_name('course_lists').find_elements_by_tag_name('li')
courseName = []
courseURL = []
for i in courseList:
    courseName.append(i.find_element_by_class_name('course-title').text.split(' ')[0])
    courseURL.append(i.find_element_by_tag_name('a').get_attribute('href'))

for i in range(len(courseList)):
    if courseName[i] == '[혁신교육개발원]':
        continue
    print(courseName[i])
    driver.get(courseURL[i])
    assigns = driver.find_element_by_class_name('course_box_current').find_elements_by_class_name('modtype_assign')
    assignURL = []
    if not assigns:
        print("과제가 없습니다.\n")
        continue
    for j in assigns:
        assignURL.append(j.find_element_by_tag_name('a').get_attribute('href'))
    for k in assignURL:
        driver.get(k)
        assign = driver.find_element_by_xpath('//*[@id="region-main"]/div/h2')
        deadline = driver.find_element_by_class_name('submissionstatustable').find_elements_by_class_name('lastcol')[2]
        print("과제명 : " + assign.text)
        print("과제 제출 마감일 : " + deadline.text + "\n")
            
