from selenium import webdriver
from bs4 import BeautifulSoup
import requests


url="http://www.jbnu.ac.kr/kor/?menuID=452&pno={page}"
r = requests.get(url)
bs=BeautifulSoup(r.content,"lxml")


driver = webdriver.Chrome('C:/Users/김자연/Desktop/setups/chromedriver_win32/chromedriver.exe')

driver.get(url)

#divs = bs.select("th")
#divs = divs[-9:]
#print(divs)

#th = driver.find_element_by_class_name('page_list').find_elements_by_tag_name('img')
#Len=0

#함수
#newpost : 새 글 아이콘 공지 출력
#lastpost : 최신 공지 5개 출력
#notice : 고정공지 출력
#변수
#pagenum : 현재 페이지 숫자
#postnum : 현재 페이지에서 게시글 순서
#순서
#고정공지→새 글 아이콘 공지 or 최신공지 출력



def newpost(pagenum,postnum):
    print("newpost in")
    url="http://www.jbnu.ac.kr/kor/?menuID=452&pno={pagenum}"
    driver.get(url)
    th = driver.find_element_by_class_name('page_list').find_elements_by_tag_name('img')
    for i in th:
        img = i.get_attribute('alt')
        if img=='새글' and postnum<len(th):
            text = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(postnum)).text
            print("제목 :",text)
            date = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[5]'%(postnum)).text
            print("게시일 :",date)
            link = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(postnum)).get_attribute("href")
            print(link)
            print("postnum =",postnum)
            print("pagenum =",pagenum)
            postnum+=1
        elif img=='새글' and postnum>9:
            driver.find_element_by_xpath('//*[@id="print_area"]/div[2]/a[%d]'%(pagenum+1)).click()
            newpost(pagenum+1)
            postnum=0
    lastpost(pagenum,postnum)

def lastpost(pagenum,postnum):
    print("lastpost in")
    url="http://www.jbnu.ac.kr/kor/?menuID=452&pno={pagenum}"
    driver.get(url)
    nextpagepost=5-postnum
    print("nextpagenum =",nextpagepost)
    if postnum<4:
        for i in range(postnum+1,9):
            text = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(postnum)).text
            print("제목 :",text)
            date = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[5]'%(postnum)).text
            print("게시일 :",date)
            link = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(postnum)).get_attribute("href")
            print(link)
            print("postnum =",postnum)
            print("pagenum =",pagenum)
            postnum+=1
        driver.find_element_by_xpath('//*[@id="print_area"]/div[2]/a[%d]'%(pagenum+1)).click()
        postnum=1
        for i in range(postnum,nextpagepost):
            text = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(postnum)).text
            print("제목 :",text)
            date = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[5]'%(postnum)).text
            print("게시일 :",date)
            link = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(postnum)).get_attribute("href")
            print(link)
            print("postnum =",postnum)
            print("pagenum =",pagenum)
            postnum+=1
    else:
        for i in range(5):
            text = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(postnum)).text
            print("제목 :",text)
            date = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[5]'%(postnum)).text
            print("게시일 :",date)
            link = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(postnum)).get_attribute("href")
            print(link)
            print("postnum =",postnum)
            print("pagenum =",pagenum)
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
            text = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(postnum)).text
            print("제목 :",text)
            date = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[5]'%(postnum)).text
            print("게시일 :",date)
            link = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(postnum)).get_attribute("href")
            print(link)
            print("postnum =",postnum)
            print("pagenum =",pagenum)
            postnum+=1
        elif notice=='공지글' and postnum>9:
            driver.find_element_by_xpath('//*[@id="print_area"]/div[2]/a[%d]'%(pagenum+1)).click()
            notice(pagenum+1)
            postnum=0
    newpost(pagenum,postnum)

        

notice(1)




#for d in range(9):
#    icon = len(divs[d].select("img"))
#    if icon:
#        text = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(d+1)).text
#        print("제목 :",text)
#        date = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[5]'%(d+1)).text
#        print("게시일 :",date)
#        link = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(d+1)).get_attribute("href")
#        print(link)
#    else:
#        break

#print("\n")
#for d in range(d,d+5):
#    if not icon:
#        text = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(d+1)).text
#        print("제목 :",text)
#        date = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[5]'%(d+1)).text
#        print("게시일 :" ,date)
#        link = driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[%d]/td[2]/span/a'%(d+1)).get_attribute("href")
#        print(link)
#    else:
#        break


    

#order=driver.find_element_by_xpath('//*[@id="print_area"]/div[1]/table/tbody/tr[1]/th/img').text
#print(order)
#print(len(order))

#if order==False:
#    print("empty")

#image = driver.find_elements_by_tag_name('th')
#print(image)

# //*[@id="print_area"]/div[1]/table/tbody/tr[1]/td[2]/span/a
# //*[@id="print_area"]/div[1]/table/tbody/tr[2]/td[2]/span/a
# //*[@id="print_area"]/div[1]/table/tbody/tr[3]/td[2]/span/a
# //*[@id="print_area"]/div[1]/table/tbody/tr[9]/td[2]/span/a