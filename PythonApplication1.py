from selenium import webdriver
from bs4 import BeautifulSoup
import requests

url="http://www.jbnu.ac.kr/kor/?menuID=452"
r = requests.get(url)
bs=BeautifulSoup(r.content,"lxml")


driver = webdriver.Chrome('C:/Users/김자연/Desktop/setups/chromedriver_win32/chromedriver.exe')

driver.get(url)

#divs = bs.select("th")
#divs = divs[-9:]
#print(divs)

img=driver.find_elements_by_tag_name("img")
print(img)
    



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


