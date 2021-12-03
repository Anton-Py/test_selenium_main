import telebot
from telebot.types import Message
from constants import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, chrome):
        self.instance = telebot.TeleBot(token)
        self.id_channel = id_channel
        self.chrome = chrome
        self.base_url = site

    def wait_of_element_located(self, css_selector, time=10):
        return WebDriverWait(self.chrome, time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)),
            message=f"Can't find element by locator {css_selector}")

    def go_to_site(self):
        return self.chrome.get(self.base_url)