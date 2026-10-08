import pytest
from selenium import webdriver
from urls import URLs


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def main_page(driver):
    driver.get(URLs.HOME_PAGE_URL)
    return driver
