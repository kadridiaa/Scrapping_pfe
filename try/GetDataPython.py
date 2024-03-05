# from flask import Flask, jsonify
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service 
# from selenium.webdriver.common.by import By
# import json

# # Set up Selenium WebDriver
# service = Service(executable_path='chromedriver.exe')
# driver = webdriver.Chrome(service=service)

# def scrape_data():
#     driver.get("https://fr.aliexpress.com/w/wholesale-airpods.html?spm=a2g0o.productlist.search.0")
#     imgs_element = driver.find_element(By.CLASS_NAME, "images--imageWindow--1Z-J9gn")
#     outer_html = driver.execute_script("return arguments[0].outerHTML;", imgs_element)
#     return outer_html

# # Execute the scrape_data function to get the image source
# element = scrape_data()
# print (element)

# driver.quit()

from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
import json

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

def scrape_data():
    driver.get("https://fr.aliexpress.com/w/wholesale-airpods.html?spm=a2g0o.productlist.search.0")
    parent_element = driver.find_element(By.CLASS_NAME, "multi--content--11nFIBL")
        
    parent_outer_html = driver.execute_script("return arguments[0].outerHTML;", parent_element)
    
    child_elements = parent_element.find_elements(By.XPATH, "./*")
    
    child_elements_list = []
    for child in child_elements:
        tag_name = child.tag_name
        attributes = child.get_attribute("outerHTML")
        
        child_element_details = {
            "tag_name": tag_name,
            "attributes": attributes
        }
        child_elements_list.append(child_element_details)
    
    # Construct the JSON object
    json_data = {
        "parent_outer_html": parent_outer_html,
        "child_elements": child_elements_list
    }
    
    return json_data

json_data = scrape_data()

json_file_path = 'ProductSearchedData.json'

with open(json_file_path, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print("Data has been written to {json_file_path}")

driver.quit()
