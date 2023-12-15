import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestMakeMyTrip:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.makemytrip.com/")
        yield
        self.driver.quit()

    def test_search_cheapest_departure(self, setup):
        # Input your departure and destination details here
        departure_city = "Bengaluru"
        destination_city = "Mumbai"

        #  departure city input field
        departure_input = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/label/input")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/label/input"))
        )
        departure_input.send_keys(Keys.BACKSPACE * len(departure_input.get_attribute("value")))
        #departure_input.clear()
        departure_input.send_keys(departure_city)
        time.sleep(2)
        departure_input.send_keys(Keys.ARROW_DOWN, Keys.RETURN)

        # destination city input field
        destination_input = self.driver.find_element(By.ID, "toCity")

        destination_input.clear()
        destination_input.send_keys(destination_city)
        time.sleep(2)
        destination_input.send_keys(Keys.ARROW_DOWN, Keys.RETURN)

        # Find and click on the date input field to open the calendar
        date_input = self.driver.find_element(By.XPATH, "//span[normalize-space()='22']")
        date_input.click()

        #  date within the specified month range
        date_range = self.driver.find_element(By.XPATH, "//div[@aria-label='Fri Dec 22 2023']")
        date_range.click()

        # click on the "Search" button
        search_button = self.driver.find_element(By.XPATH, "//a[normalize-space()='Search']")
        search_button.click()

        # Wait for the search results to load
        time.sleep(5)

        #click on the "Sort by" dropdown to select "Cheapest"
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//p[contains(text(),'₹ 3,763')]")
        sort_by_dropdown.click()

        # Wait for the sorting to take effect
        time.sleep(5)

        # Verify that the first result is the cheapest departure rate
        result_prices = self.driver.find_elements(By.XPATH, "//div[@class='DayPicker-Months']")
        assert result_prices, "No search results found."
        cheapest_price = result_prices[39].text
        print(f"The cheapest departure rate for the specified month range is: {cheapest_price}")

        # Additional assertions or actions can be added as needed

if __name__ == "__main__":
    pytest.main(["-v", "test_makemytrip.py"])
