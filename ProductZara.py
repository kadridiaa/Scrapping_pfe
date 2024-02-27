from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


def scrape_data():
    driver.get(
        "https://www.zara.com/dz/fr/search?searchTerm=t%20shirt&section=WOMAN"
    )
    
    # product_div = driver.find_elements(By.CLASS_NAME , 'product-grid__product-list')
    list_products = driver.find_elements(By.TAG_NAME  , 'li')
    imgs_product = driver.find_elements(By.TAG_NAME , 'img')
    product_names  = driver.find_elements(By.TAG_NAME  , 'h2')
    price_spans = driver.find_elements(By.CLASS_NAME, 'price__amount')

    for price_span in price_spans:
        price_value_span = price_span.find_element(By.CLASS_NAME, 'money-amount__main')
        price_text = price_value_span.text
        print(price_text)
    
    
    
    # print(product_prices)
    
    
    
    for name in product_names:
        prd_name = name.text
        print(prd_name)
    
    for img in imgs_product:
            img_src = img.get_attribute('src')
            print(img_src)

    
    
    
    
    
    
    
    # for prd in list_products :
    #     #  product_img = prd.find_elements(By.CLASS_NAME  ,'media__wrapper media__wrapper--fill')
    #     #  print(product_img)
    #      product_data = prd.find_elements(By.CLASS_NAME ,'product-grid-product-info')
    #      print(product_data)
    #      product_name = prd.find_elements(By.TAG_NAME ,'h2') ##product-link _item product-grid-product-info__name link
    #      print(product_name)
    #      product_price = prd.find_elements(By.CLASS_NAME , 'money-amount__main')
    #      print(product_price)
         
         
         
    # print(len(list_products))
    
    
scrape_data()    