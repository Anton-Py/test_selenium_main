# import telebot
# from telebot.types import Message
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from lib.constants import Locators
import urllib.request
import os.path
import time


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

    def wait_of_element_located_button(self, css_selector, time=10):
        return WebDriverWait(self.chrome, time).until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, css_selector)),
            message=f"Can't find element by locator {css_selector}")

    def wait_of_elements_located_css_selector(self, css_selector, time=10):
        return WebDriverWait(self.chrome, time).until(
            EC.visibility_of_any_elements_located((By.CSS_SELECTOR, css_selector)),
            message=f"Can't find element by locator {css_selector}")

    def wait_of_element_located_tag_name(self, css_selector, time=10):
        return WebDriverWait(self.chrome, time).until(
            EC.visibility_of_element_located((By.TAG_NAME, css_selector)),
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

    def switch_to_second_tab(self):
        default_handle = self.chrome.window_handles
        self.chrome.switch_to.window(default_handle[1])
        return default_handle

    def switch_to(self):
        self.chrome.switch_to.window(self.switch_to_second_tab()[0])
        default_handle = self.chrome.current_window_handle
        handles = list(self.chrome.window_handles)
        assert len(handles) > 1
        handles.remove(default_handle)
        assert len(handles) > 0
        self.chrome.switch_to.window(handles[0])
        self.chrome.close()
        self.chrome.switch_to.window(default_handle)

    def close_last_tab(self):
        if len(self.chrome.window_handles) == 2:
            self.chrome.switch_to.window(window_name=self.chrome.window_handles[1])
            time.sleep(2)
            self.chrome.close()
            self.chrome.switch_to.window(window_name=self.chrome.window_handles[0])
            self.chrome.execute_script('el = document.elementFromPoint(100, 200); el.click();')

    def check_downloaded_distributiv(self, element):
        while not os.path.exists('D:\\Main_test_one_file\\test_main\\First\\download_files\\'):
            time.sleep(2)
        # check distributiv
        if os.path.isfile(f'D:\\Main_test_one_file\\test_main\\First\\download_files\\{element}'):
            print(f"File download: {element} is completed")
        else:
            print(f"File download: {element} is not completed")
        time.sleep(3)
        # delete distributiv
        os.remove(f'D:\\Main_test_one_file\\test_main\\First\\download_files\\{element}')
