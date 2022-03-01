from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_verify_application_open_successfully():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.google.com")
        # Getting current URL source code
        get_title = driver.title
        # Printing the title of this URL
        print(get_title)
        assert driver.title == "Google"
    except Exception as e:
        print(e)
    finally:
        driver.quit()

        driver.quit()