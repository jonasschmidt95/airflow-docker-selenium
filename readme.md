# Airflow Docker mit Selenium

## 1. Installation

### 1.1 Image erstellen

Mit dem folgenden Befehl wird das AirflowImage erweitert. Es werden die zusätzlichen Packages für Selenium und BeautifulSoup installiert.

`docker-compose build`

### 1.2 Datenbank initialisieren

Mit dem Befehl wird die Datenbank von Airflow initialisert.

`docker compose up airflow-init`

### 1.3 Starten von Airflow

Mit dem folgenden Befehl werden die Container gestartet.

`docker compose up -d`

Man kann Airflow nun unter `http://localhost:8080/` aufrufen.

## Quellen

- https://www.dataquest.io/blog/setting-up-apache-airflow-with-docker-locally-part-i/
- https://scrapfly.io/blog/posts/intro-to-web-scraping-using-selenium-grid