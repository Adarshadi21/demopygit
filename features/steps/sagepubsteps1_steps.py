from behave import*
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@given('I access "{url}"')
def step_access_website(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)


@when('I click on the "{title}" title')
def step_click_tile(context, title,):
    WebDriverWait(context.driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "cookieconsent:desc"))
    )

    title_locator = (By.XPATH, "//a[@data-id='/-Our collections-Academic Books']")
    context.driver.find_element(*title_locator).click()


@when('I click on {count} titles under "{discipline}"')
def step_click_discipline_tiles(context, count, discipline):
    discipline_locator = (By.XPATH, f"//span[text()='Browser By']//following-sibling::span[text()='{discipline}']")
    context.driver.find_element(*discipline_locator).click()

    for _ in range(int(count)):
        tile_locator = (By.CSS_SELECTOR, '.product-list .product-tile a')
        tile = context.driver.find_element(*tile_locator)
        tile_name = tile.text
        unique_integer = extract_unique_integer(tile.get_attribute("href"))
        print(f"Clicked Tile: {tile_name}, Unique Integer: {unique_integer}")
        tile.click()


def extract_unique_integer(url):
    match = re.search(r'\b(\d+)\b', url)
    return match.group(1) if match else None


@then('I print the unique integer along with the clicked title name')
def step_print_unique_integer(context):
    pass
