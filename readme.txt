Le but de ce projet récupérer les informations du site "http://books.toscrape.com/"
à l'aide python et de ses bibliothèques (soit selenium ou beautifulsoup) puis y accéder avec MongoDb.
Dans mon cas j'ai utilisé selenium

Dans les grandes lignes le projet consistait à 
-récupérer les informations en se rendant sur le site   "http://books.toscrape.com"
et repérant les balises Html nécessaires grâce au script "scrap.py":une fois ce script lancer on obtient un fichier".csv"contenant les informations récupérer.
-ouvrir ou exporter les informations récupérer dans sa base de données MongoDb: avec le script"main.py"

prérequis
installation de python(version 3.11.6 ou supérieure)
installation de pandas : pip install pandas 
installation de selenium: pip install selenium