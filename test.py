# from bs4 import BeautifulSoup 
# import requests


# html = requests.get('https://quotes.toscrape.com/')
# data = BeautifulSoup(html.text ,'html.parser').findAll('span' , attrs={"class" : 'text'})
# print(html.text)
# for i in data :     
#     print(i.text)




# driver.get("https://fr.aliexpress.com/?src=bing&albch=search&acnt=1603219&isdl=y&aff_short_key=UneMJZVf&albcp=554819710&albag=1304021917290456&slnk=&trgt=kwd-81501613456833&plac=&crea=81501424002086&netw=o&device=c&mtctp=e&utm_source=Bing&utm_medium=ppc&utm_campaign=FR-Search-Bing-Trademark-20240117&utm_content=e-Aliexpress-20170106&utm_term=aliexpress%5C-aliexpress&msclkid=b6384767fd561964005422ae8c69f928")
from selenium import webdriver

# button_input = driver.find_element(By.CLASS_NAME, "search-button")
# input = driver.find_element(By.ID, "search-key")
# input.send_keys("airpods")
# button_input.click()
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)


driver.get("https://fr.aliexpress.com/w/wholesale-airpods.html?spm=a2g0o.productlist.search.0")



# wait = WebDriverWait(driver, 10)
# wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "images--imageWindow--1Z-J9gn")))
img_element = driver.find_element(By.CLASS_NAME, "images--item--3XZa6xf")
print(new_element)

driver.quit()



