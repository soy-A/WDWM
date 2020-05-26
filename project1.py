from selenium import webdriver
import getpass

driver = webdriver.Chrome('C:\chromedriver.exe')
driver.get('https://ieilms.jbnu.ac.kr/login.php')
#delay = 10
#driver.implicitly_wait(delay)

id = input("학번을 입력하세요 : ")
pw = getpass.getpass("비밀번호를 입력하세요 : ")
driver.find_element_by_name('username').send_keys(id)
driver.find_element_by_name('password').send_keys(pw)
driver.find_element_by_xpath('//*[@id="region-main"]/div/div/div/div[1]/div[1]/div[2]/form/div[2]/input').click()
courseList = driver.find_element_by_class_name('course_lists').find_elements_by_tag_name('li')
for i in courseList:
    course = i.find_element_by_class_name('course-title').text.split(' ')[0]
    print(course)

name = input("수업명을 입력하시오 : ")
for i in courseList:
    course = i.find_element_by_class_name('course-title').text.split(' ')[0]
    if course == name:
        driver.get(i.find_element_by_tag_name('a').get_attribute('href'))
        assigns = driver.find_element_by_class_name('course_box_current').find_elements_by_class_name('modtype_assign')
        url = []
        for j in assigns:
            url.append(j.find_element_by_tag_name('a').get_attribute('href'))
        for k in url:
            driver.get(k)
            report = driver.find_element_by_xpath('//*[@id="region-main"]/div/h2')
            deadline = driver.find_element_by_class_name('submissionstatustable').find_elements_by_class_name('lastcol')[2]
            print(report.text)
            print("과제 제출 마감일 : " + deadline.text)
            
        break