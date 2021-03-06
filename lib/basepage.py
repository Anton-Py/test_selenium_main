# import telebot
# from telebot.types import Message
from lib.constants import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, chrome):
        # self.instance = telebot.TeleBot(TOKEN)
        # self.id_channel = ID_CHANNEL
        self.chrome = chrome
        self.base_url = Locators.SITE

    def wait_of_element_located(self, css_selector, time=10):
        return WebDriverWait(self.chrome, time).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)),
            message=f"Can't find element by locator {css_selector}")

    def wait_of_element_located_tag_name(self, css_selector, time=10):
        return WebDriverWait(self.chrome, time).until(
            EC.visibility_of_any_elements_located((By.TAG_NAME, css_selector)),
            message=f"Can't find element by locator {css_selector}")

    def wait_of_element_click(self, css_selector, time=10):
        return WebDriverWait(self.chrome, time).until(
            EC.element_to_be_clickable((By.LINK_TEXT, css_selector)),
            message=f"Can't find element by locator {css_selector}")

    def wait_of_elements_located_css(self, css_selector, time=10):
        return WebDriverWait(self.chrome, time).until(
            EC.visibility_of_any_elements_located((By.CLASS_NAME, css_selector)),
            message=f"Can't find element by locator {css_selector}")

    def wait_of_element_located_text(self, css_selector, time=10):
        return WebDriverWait(self.chrome, time).until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, css_selector)),
            message=f"Can't find element by locator {css_selector}")

    def go_to_site(self):
        return self.chrome.get(self.base_url)
