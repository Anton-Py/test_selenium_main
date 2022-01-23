from lib.core import BasePage
from lib.constants import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class MovaviLocators:
    LOCATOR_HAD_SEARCH = HEADER_SEARCH
    LOCATOR_ENTR_FIRLD = ENTRY_FIELD
    LOCATOR_SEARCH = SEARCH
    LOCATOR_MN_PAGE = MAIN_TEXT
    LOCATOR_UI = LOC_UI


class MainPage(BasePage):

    def act_first(self, tag_name):
        element = self.wait_of_element_located(tag_name)
        ActionChains(self.chrome) \
            .move_to_element(element) \
            .key_down(Keys.CONTROL) \
            .click(element) \
            .key_up(Keys.CONTROL) \
            .perform()
    def act_first_for_links(self, tag_name):
        element = self.wait_of_element_click(tag_name)
        ActionChains(self.chrome) \
            .move_to_element(element) \
            .key_down(Keys.CONTROL) \
            .click(element) \
            .key_up(Keys.CONTROL) \
            .perform()

    def act_second(self):
        element = self.wait_of_element_located(MovaviLocators.LOCATOR_SEARCH)
        ActionChains(self.chrome) \
            .move_to_element(element) \
            .key_down(Keys.CONTROL) \
            .click(element) \
            .key_up(Keys.CONTROL) \
            .perform()

    def act_ui(self, tag_name):
        element = self.chrome.find_element_by_partial_link_text(tag_name)
        ActionChains(self.chrome) \
            .move_to_element(element) \
            .key_down(Keys.CONTROL) \
            .click(element) \
            .key_up(Keys.CONTROL) \
            .perform()

    def handle(self):
        default_handle = self.chrome.window_handles
        self.chrome.switch_to.window(default_handle[1])
        return default_handle

    def switch_to(self):
        self.chrome.switch_to.window(self.handle()[0])
        default_handle = self.chrome.current_window_handle
        handles = list(self.chrome.window_handles)
        assert len(handles) > 1
        handles.remove(default_handle)
        assert len(handles) > 0
        self.chrome.switch_to_window(handles[0])
        self.chrome.close()
        self.chrome.switch_to_window(default_handle)

    # Проверяем ссылки в хедере, кроме поиска
    def test_main_page(self):
        main_page = self.wait_of_element_located(MovaviLocators.LOCATOR_MN_PAGE)
        assert main_page.text == TITLE_TXT
        for dict_window_key in DICT_WINDOWS:
            tag_name = DICT_WINDOWS[dict_window_key]
            self.act_first(tag_name)
            self.handle()
            url = self.chrome.current_url
            assert (ASRT[0] in url) or (ASRT[1] in url) or (ASRT[2] in url) or (ASRT[3] in url) or (ASRT[4] in url)
            self.switch_to()

    # Проверяем кнопку поиска в хедере
    def site_search(self):
        self.wait_of_element_located(MovaviLocators.LOCATOR_HAD_SEARCH).click()
        self.wait_of_element_located(MovaviLocators.LOCATOR_ENTR_FIRLD).send_keys(TEXT_SEARCH)
        self.act_second()
        self.handle()
        time.sleep(2)
        body_text = self.chrome.find_element_by_tag_name('body').text
        assert PAGE_SORCE_ONE in body_text, "страница не соответствует запросу"
        self.chrome.switch_to.window(self.handle()[0])
        self.switch_to()

    # Проверяем все ui
    def main_ui(self):
        for locator in LOC_UI:
            self.wait_of_element_located_text(locator).click()
            time.sleep(3)
            if locator == 'Video':
                dict_page = DICT_VIDEO
            elif locator == 'Screen Recording':
                dict_page = DICT_SCREEN_RECORDING
            elif locator == 'Photo':
                dict_page = DICT_PHOTO
            elif locator == 'For Work':
                dict_page = DICT_FOR_WORK
            else:
                dict_page = DICT_FOR_EDUCATION
            for dikt_key in dict_page:
                tag_name = dict_page[dikt_key]
                self.act_ui(tag_name)
                self.handle()
                time.sleep(3)
                if locator == 'For Work':
                    DICT_HREF["Video_Converter"] = "https://www.movavi.com/videoconverter"
                url = self.chrome.current_url
                assert (DICT_HREF[dikt_key] in url)
                self.switch_to()


