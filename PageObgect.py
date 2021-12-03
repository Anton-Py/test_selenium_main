from BaseApp import BasePage
from constants import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class MovaviLocators:
    LOCATOR_HAD_SEARCH = header_search
    LOCATOR_ENTR_FIRLD = entry_field
    LOCATOR_SEARCH = search
    LOCATOR_MN_PAGE = main_text


class MainPage(BasePage):
    # Проверяем ссылки в хедере, кроме поиска
    def test_main_page(self):
        main_page = self.wait_of_element_located(MovaviLocators.LOCATOR_MN_PAGE)
        assert main_page.text == title_txt

        for dict_window_key in dict_windows:
            action = ActionChains(self.chrome)
            tag_name = dict_windows[dict_window_key]
            element = self.chrome.find_element(By.TAG_NAME, tag_name)
            time.sleep(1)
            action \
                .move_to_element(element) \
                .key_down(Keys.CONTROL) \
                .click(element) \
                .key_up(Keys.CONTROL) \
                .perform()
            time.sleep(1)
            default_handle = self.chrome.window_handles
            self.chrome.switch_to.window(default_handle[1])  # Преключаемся на вторую вкладку
            time.sleep(1)
            url = self.chrome.current_url
            assert (asrt[0] in url) or (asrt[1] in url) or (asrt[2] in url) or (asrt[3] in url) or (asrt[4] in url)
            # assert chrome.current_url in asserts
            time.sleep(1)
            self.chrome.switch_to.window(default_handle[0])
            time.sleep(1)

            default_handle = self.chrome.current_window_handle
            handles = list(self.chrome.window_handles)
            assert len(handles) > 1
            time.sleep(1)
            handles.remove(default_handle)
            assert len(handles) > 0
            time.sleep(1)
            self.chrome.switch_to_window(handles[0])
            self.chrome.close()
            self.chrome.switch_to_window(default_handle)
            time.sleep(1)

    # Проверяем кнопку поиска в хедере
    def sait_search(self):
        element = self.wait_of_element_located(MovaviLocators.LOCATOR_HAD_SEARCH)
        element.click()
        time.sleep(2)
        entry = self.wait_of_element_located(MovaviLocators.LOCATOR_ENTR_FIRLD)
        entry.send_keys(text_search)
        time.sleep(2)
        action = ActionChains(self.chrome)
        element = self.wait_of_element_located(MovaviLocators.LOCATOR_SEARCH)
        time.sleep(1)
        action \
            .move_to_element(element) \
            .key_down(Keys.CONTROL) \
            .click(element) \
            .key_up(Keys.CONTROL) \
            .perform()
        time.sleep(1)
        default_handle = self.chrome.window_handles
        self.chrome.switch_to.window(default_handle[1])
        time.sleep(3)
        body_text = self.chrome.find_element_by_tag_name('body').text
        assert (page_source_one and page_source_two) in body_text, "страница не соответствует запросу"
        time.sleep(2)
        self.chrome.switch_to.window(default_handle[0])
        time.sleep(1)

        default_handle = self.chrome.current_window_handle
        handles = list(self.chrome.window_handles)
        assert len(handles) > 1
        time.sleep(1)
        handles.remove(default_handle)
        assert len(handles) > 0
        time.sleep(1)
        self.chrome.switch_to_window(handles[0])
        self.chrome.close()
        self.chrome.switch_to_window(default_handle)
        time.sleep(1)