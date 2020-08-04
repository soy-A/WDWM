from selenium import webdriver
import json
import threading

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

data_dict = []
cpp_dict = []
creative_dict = []
electrical_dict = []
global_dict = []

def lms():
    driver = webdriver.Chrome(executable_path = '/workspace/chromedriver', options = options)
    driver.get('https://ieilms.jbnu.ac.kr/login.php')

    id = '201819186'
    pw = 'jsallyb8246!'
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
        if courseName[i] == '자료구조':
            print(courseName[i])
            driver.get(courseURL[i])
            assigns = driver.find_element_by_id('section-1').find_elements_by_class_name('modtype_assign')
            assignURL = []
            if not assigns:
                print("과제가 없습니다.\n")
                data_dict.append({'title' : '과제가 없습니다.', 'date' : ' '})
                continue
            for j in assigns:
                assignURL.append(j.find_element_by_tag_name('a').get_attribute('href'))
            for k in assignURL:
                driver.get(k)
                assign = driver.find_element_by_xpath('//*[@id="region-main"]/div/h2')
                deadline = driver.find_element_by_class_name('submissionstatustable').find_elements_by_class_name('lastcol')[2]
                print("과제명 : " + assign.text)
                print("과제 제출 마감일 : " + deadline.text + "\n")
                data_dict.append({'title': assign.text, 'date': deadline.text})
        elif courseName[i] == 'C++프로그래밍':
            print(courseName[i])
            driver.get(courseURL[i])
            assigns = driver.find_element_by_id('section-1').find_elements_by_class_name('modtype_assign')
            assignURL = []
            if not assigns:
                print("과제가 없습니다.\n")
                cpp_dict.append({'title' : '과제가 없습니다.', 'date' : ' '})
                continue
            for j in assigns:
                assignURL.append(j.find_element_by_tag_name('a').get_attribute('href'))
            for k in assignURL:
                driver.get(k)
                assign = driver.find_element_by_xpath('//*[@id="region-main"]/div/h2')
                deadline = driver.find_element_by_class_name('submissionstatustable').find_elements_by_class_name('lastcol')[2]
                print("과제명 : " + assign.text)
                print("과제 제출 마감일 : " + deadline.text + "\n")
                cpp_dict.append({'title': assign.text, 'date': deadline.text})
        elif courseName[i] == '창의적IT공학설계입문':
            print(courseName[i])
            driver.get(courseURL[i])
            assigns = driver.find_element_by_id('section-1').find_elements_by_class_name('modtype_assign')
            assignURL = []
            if not assigns:
                print("과제가 없습니다.\n")
                creative_dict.append({'title' : '과제가 없습니다.', 'date' : ' '})
                continue
            for j in assigns:
                assignURL.append(j.find_element_by_tag_name('a').get_attribute('href'))
            for k in assignURL:
                driver.get(k)
                assign = driver.find_element_by_xpath('//*[@id="region-main"]/div/h2')
                deadline = driver.find_element_by_class_name('submissionstatustable').find_elements_by_class_name('lastcol')[2]
                print("과제명 : " + assign.text)
                print("과제 제출 마감일 : " + deadline.text + "\n")
                creative_dict.append({'title': assign.text, 'date': deadline.text})
        elif courseName[i] == '글로벌공학윤리':
            print(courseName[i])
            driver.get(courseURL[i])
            assigns = driver.find_element_by_id('section-1').find_elements_by_class_name('modtype_assign')
            assignURL = []
            if not assigns:
                print("과제가 없습니다.\n")
                global_dict.append({'title' : '과제가 없습니다.', 'date' : ' '})
                continue
            for j in assigns:
                assignURL.append(j.find_element_by_tag_name('a').get_attribute('href'))
            for k in assignURL:
                driver.get(k)
                assign = driver.find_element_by_xpath('//*[@id="region-main"]/div/h2')
                deadline = driver.find_element_by_class_name('submissionstatustable').find_elements_by_class_name('lastcol')[2]
                print("과제명 : " + assign.text)
                print("과제 제출 마감일 : " + deadline.text + "\n")
                global_dict.append({'title': assign.text, 'date': deadline.text})
        elif courseName[i] == '전기전자기초실험':
            print(courseName[i])
            driver.get(courseURL[i])
            assigns = driver.find_element_by_id('section-1').find_elements_by_class_name('modtype_assign')
            assignURL = []
            if not assigns:
                print("과제가 없습니다.\n")
                electrical_dict.append({'title' : '과제가 없습니다.', 'date' : ' '})
                continue
            for j in assigns:
                assignURL.append(j.find_element_by_tag_name('a').get_attribute('href'))
            for k in assignURL:
                driver.get(k)
                assign = driver.find_element_by_xpath('//*[@id="region-main"]/div/h2')
                deadline = driver.find_element_by_class_name('submissionstatustable').find_elements_by_class_name('lastcol')[2]
                print("과제명 : " + assign.text)
                print("과제 제출 마감일 : " + deadline.text + "\n")
                electrical_dict.append({'title': assign.text, 'date': deadline.text})
    driver.quit()


def DatatoJson(data_json):
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data_json, file, ensure_ascii=False, indent='\t')

def CpptoJson(cpp_json):
    with open('cpp.json', 'w', encoding='utf-8') as file:
        json.dump(cpp_json, file, ensure_ascii=False, indent='\t')

def CreativetoJson(creative_json):
    with open('creative.json', 'w', encoding='utf-8') as file:
        json.dump(creative_json, file, ensure_ascii=False, indent='\t')

def ElectricaltoJson(electrical_json):
    with open('electrical.json', 'w', encoding='utf-8') as file:
        json.dump(electrical_json, file, ensure_ascii=False, indent='\t')

def GlobaltoJson(global_json):
    with open('global.json', 'w', encoding='utf-8') as file:
        json.dump(global_json, file, ensure_ascii=False, indent='\t')

class Repeat:

    def __init__(self):
        pass

    def Relms(self):
        global data_dict,cpp_dict,creative_dict,electrical_dict,global_dict
        data_dict.clear()
        cpp_dict.clear()
        creative_dict.clear()
        electrical_dict.clear()
        global_dict.clear()
        lms()
        DatatoJson(data_dict)
        CpptoJson(cpp_dict)
        CreativetoJson(creative_dict)
        ElectricaltoJson(electrical_dict)
        GlobaltoJson(global_dict)
        threading.Timer(3600, self.Relms).start()

re = Repeat()
re.Relms()
