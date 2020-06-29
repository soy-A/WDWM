import json
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path = '/workspace/chromedriver',options = options)


def output():
     for i in range(len(subjectName)): 
        print(subjectName[i])  
        driver.execute_script(subjectURL[i])
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="center2"]/div/div[2]/div/div[5]/div[2]/table/thead/tr/th[1]/a').send_keys('\n')
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
                    print('\n')
            n += 1
        driver.back()
        driver.back()
        time.sleep(3)


def subject():
     subjects = driver.find_elements_by_class_name("leftGroupMenu_div")
     subjectName = []
     subjectURL = [] 
     for i in subjects:
        name = i.get_attribute('title') 
        url = i.get_attribute('onclick')
        if name.split(' ')[0] == '2020-1': 
            subjectName.append(name.split(' ')[1])
            subjectURL.append(url)


def khubhome():
    url = "https://jbnu.khub.kr/"
    driver.get(url)
    driver.find_element_by_name('login').send_keys(id)
	driver.find_element_by_name('passwd').send_keys(pw)
	driver.find_element_by_xpath('//*[@id="loginform"]/table/tbody/tr[1]/td[2]/input').click()
	time.sleep(3)
