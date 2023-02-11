# import random
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

"""Данный модуль используется для создания базовых методов"""

# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def go_to_page(self, url):
#         return self.driver.get(url)
#
#     def find_element(self, locator, time=10):
#         return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
#
#     def find_elements(self, locator, time=10):
#         return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))
#
#     def _blank_to_self(self, locator):
#         element = self.find_element(locator)
#         self.driver.execute_script("arguments[0].setAttribute('target', arguments[1]);", element, "_self")
#
#     def click_on(self, locator):
#         self.find_element(locator).click()
#
#     @staticmethod
#     def gen_cyrillic_string(length):
#         cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#         cyrillic_letters = cyrillic_lower_letters + cyrillic_lower_letters.upper()
#         rand_string = ''.join(random.choice(cyrillic_letters) for i in range(length))
#         return rand_string

