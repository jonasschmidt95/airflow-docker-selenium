from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from bs4 import BeautifulSoup

default_args = {
    'owner': 'your-name',
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}

def get_driver():
    # selenium firefox browser options
    options = FirefoxOptions()
    options.add_argument("-headless")
    options.add_argument('--disable-dev-shm-usage')
    # Initialize a remote WebDriver
    driver = webdriver.Remote(
        command_executor="http://selenium:4444/wd/hub",
        options=options
    )
    return driver

def scrape_product_links():
    links = []
    driver = get_driver()
    # Iterate over product pages
    for page_number in range(1, 6):
        page_link = f"https://web-scraping.dev/products?page={page_number}"
        # Go to the page link
        driver.get(page_link)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        # Iterate over product boxes
        for product_box in soup.select("div.row.product"):
            # Get the link of each product
            link = product_box.select_one("a").attrs["href"]
            links.append(link)
    return links

def scrape_web():
    links = scrape_product_links()
    print(links)

# DAG setup
with DAG(
    dag_id="get_product_links",
    default_args=default_args,
    description='Simulate a RPA bot that scrapes web content',
    start_date=datetime(2025, 5, 24),
    schedule='@daily',
    catchup=False,
) as dag:
    task_generate = PythonOperator(
        task_id='scrape_web',
        python_callable=scrape_web
    )
    # Task flow
    task_generate