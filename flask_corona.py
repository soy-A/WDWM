from flask import Flask, jsonify
import json
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path='/workspace/chromedriver',options = options)

corona_dict = {}
i = 0

def output(postnum):
    text = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(postnum)).text
    print("제목 :",text)
    date = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[5]'%(postnum)).text
    print("게시일 :",date)
    link = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(postnum)).get_attribute("href")
    print(link)
    global corona_dict
    global i
    corona_dict[i] = {'text':text, 'date':date, 'link':link}    
    i = i+1



def newpost(pagenum,postnum):
    url="http://www.jbnu.ac.kr/kor/?menuID=452&pno={pagenum}"
    driver.get(url)
    th = driver.find_element_by_class_name('page_list').find_elements_by_tag_name('img')
    new = 0
    for i in th:
        img = i.get_attribute('alt')
        if img=='새글' and postnum<len(th): 
            output(postnum)
            postnum+=1
            new+=1
    if new==0:
        lastpost(pagenum,postnum)

def lastpost(pagenum,postnum):
    url="http://www.jbnu.ac.kr/kor/?menuID=452&pno={pagenum}"
    driver.get(url)
    nextpagepost=0
    if postnum>5:
        nextpagepost = 5-(9-postnum-1)
        for i in range(postnum,10):
            output(postnum)
            postnum+=1
        driver.find_element_by_xpath('//*[@id="print_area"]/div[2]/a[%d]'%(pagenum+1)).click()
        postnum=0
        for i in range(postnum,nextpagepost):
            output(postnum+1)
            postnum+=1
    else:
        for i in range(5):
            output(postnum+i)



def notice(pagenum):
    postnum=1
    url="http://www.jbnu.ac.kr/kor/?menuID=452&pno={pagenum}"
    driver.get(url)
    th = driver.find_element_by_class_name('page_list').find_elements_by_tag_name('img')
    for i in th:
        notice = i.get_attribute('alt')
        if notice=='공지글' and postnum<len(th):
            output(postnum)
            postnum+=1
    newpost(pagenum,postnum)

def toJson(corona_dict):
    with open('corona.json','w',encoding='utf-8') as file:
        json.dump( corona_dict,file,ensure_ascii=False,indent='\t')

def loadJson():
    with open('corona.json','r',encoding='utf-8') as file:
        return json.load(file)

notice(1)
#toJson(corona_dict)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/corona')
def hello_json():
    #data = loadJson()
    return jsonify(corona_dict)

if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="8080",debug=True)
