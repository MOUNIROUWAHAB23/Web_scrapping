import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

rows = []

def scrapping():
    for page in range(1, 4, 1):  
        print(page)
        page_url = "https://store.fifa.com/fr-fr/football-shirts/" + str(page) 

        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver.get(page_url)
        
        # Trouver tous les éléments <img> contenant les images
        all_images = driver.find_elements(By.XPATH, '//div[@class="col-span-7"]//img')

        for image in all_images:
            try:
                # Obtenir l'URL de l'image
                image_url = image.get_attribute("src")

                # Ajouter l'URL de l'image à la liste
                rows.append((image_url))
                print(rows)
            except:
                print("Image non trouvée")

        driver.close()

    # Créer un DataFrame Pandas et l'écrire dans un fichier CSV
    df = pd.DataFrame(rows, columns=["image_url"])
    df.to_csv(f"test1.csv", index=False)

scrapping()
