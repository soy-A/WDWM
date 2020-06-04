
from selenium import webdriver


driver = webdriver.Chrome('C:/Users/김자연/Desktop/setups/chromedriver_win32/chromedriver.exe')


def output(postnum):
    text = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(postnum)).text
    print("제목 :",text)
    date = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[5]'%(postnum)).text
    print("게시일 :",date)
    link = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(postnum)).get_attribute("href")
    print(link)



def newpost(pagenum,postnum):
    print("newpost in")
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
    print("lastpost in")
    url="http://www.jbnu.ac.kr/kor/?menuID=452&pno={pagenum}"
    driver.get(url)
    nextpagepost=0
    print("nextpagepost =",nextpagepost)
    if postnum>4:
        nextpagepost = 5-(9-postnum)
        for i in range(postnum+1,10):
            output(postnum+1)
            postnum+=1
        driver.find_element_by_xpath('//*[@id="print_area"]/div[2]/a[%d]'%(pagenum+1)).click()
        postnum=0
        for i in range(postnum,nextpagepost):
            output(postnum+1)
            postnum+=1
    else:
        for i in range(5):
            output(postnum)
            postnum+=1


def notice(pagenum):
    print("notice in")
    postnum=1
    url="http://www.jbnu.ac.kr/kor/?menuID=452&pno={pagenum}"
    driver.get(url)
    th = driver.find_element_by_class_name('page_list').find_elements_by_tag_name('img')
    for i in th:
        notice = i.get_attribute('alt')
        if notice=='공지글' and postnum<len(th):
            output(postnum)
    newpost(pagenum,postnum)

notice(1)