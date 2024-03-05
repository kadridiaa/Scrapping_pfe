from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


def scrape_data():
    driver.get(
        "https://fr.aliexpress.com/w/wholesale-airopds.html?spm=a2g0o.productlist.search.0"
    )

    # Attendre jusqu'à ce que l'élément contenant les produits soit présent
    product_container = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "list--galleryWrapper--29HRJT4"))
    )

    # Récupérer tous les éléments div à l'intérieur de l'élément parent
    product_divs = product_container.find_elements(By.TAG_NAME, "a")
    
    # product = product_divs.find_elements(By.CLASS_NAME, "multi--container--1UZxxHY cards--card--3PJxwBm search-card-item")

    # Afficher le nombre d'éléments div récupérés
    print("Nombre d'éléments div trouvés :", len(product_divs))

    # Parcourir et imprimer le contenu de chaque élément div
    for div in product_divs:
        product_img = div.find_elements(
            By.CLASS_NAME,
            "images--item--3XZa6xf",
        )
    
        product_name = div.find_elements(
            By.TAG_NAME,
            "h3",
        )
        price_div = div.find_element(By.CLASS_NAME, "multi--price--1okBCly")
        price_spans = price_div.find_elements(By.TAG_NAME, "span")
        product_price = "".join([span.text for span in price_spans])
        product_sales = div.find_elements(
            By.CLASS_NAME,
            "multi--trade--Ktbl2jB",
        )
        


# Appeler la fonction pour l'exécuter
scrape_data()

# Fermer le navigateur à la fin
driver.quit()

