import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from lib.basepage import BasePage
from lib.constants import Locators


class MainPage(BasePage):

    def act_first(self, tag_name):
        element = self.wait_of_element_located(tag_name)
        ActionChains(self.chrome) \
            .move_to_element(element) \
            .key_down(Keys.CONTROL) \
            .click(element) \
            .key_up(Keys.CONTROL) \
            .perform()

    # def act_second(self):
    #     element = self.wait_of_element_located(Locators.SEARCH)
    #     ActionChains(self.chrome) \
    #         .move_to_element(element) \
    #         .key_down(Keys.CONTROL) \
    #         .click(element) \
    #         .key_up(Keys.CONTROL) \
    #         .perform()

    # def act_ui(self, tag_name):
    #     element = self.chrome.find_element_by_partial_link_text(tag_name)
    #     ActionChains(self.chrome) \
    #         .move_to_element(element) \
    #         .key_down(Keys.CONTROL) \
    #         .click(element) \
    #         .key_up(Keys.CONTROL) \
    #         .perform()

    def handle(self):
        default_handle = self.chrome.window_handles
        self.chrome.switch_to.window(default_handle[1])
        # return default_handle

    def switch_to(self):
        self.chrome.switch_to.window(self.handle()[0])
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
            time.sleep(1)
            self.chrome.close()
            self.chrome.switch_to.window(window_name=self.chrome.window_handles[0])

    # Проверяем ссылки в хедере, кроме поиска
    def test_links_header_other_than_search(self):
        main_page = self.wait_of_element_located(Locators.MAIN_TEXT)
        assert main_page.text == Locators.TITLE_TXT

        for dict_window_key in Locators.DICT_WINDOWS:
            tag_name = Locators.DICT_WINDOWS[dict_window_key]
            self.act_first(tag_name)
            self.handle()
            url = self.chrome.current_url
            assert (Locators.ASRT[0] in url) or (Locators.ASRT[1] in url) or (Locators.ASRT[2] in url) or (Locators.ASRT[3] in url) or (Locators.ASRT[4] in url)
            self.switch_to()

    # Проверяем кнопку поиска в хедере
    def test_site_search(self):
        self.wait_of_element_located(Locators.HEADER_SEARCH).click()
        self.wait_of_element_located(Locators.ENTRY_FIELD).send_keys(Locators.TEXT_SEARCH)
        self.act_first(Locators.SEARCH)
        self.handle()
        time.sleep(2)
        body_text = self.chrome.find_element_by_tag_name('body').text
        # print(body_text)
        assert Locators.PAGE_SORCE_ONE in body_text, "страница не соответствует запросу"
        self.close_last_tab()

    # Проверяем все ссылки в выпадающем меню
    def test_all_links_dropdown_menu(self):
        time.sleep(3)
        for locator in Locators.LOC_UI:
            max_w_m = 4
            self.wait_of_element_click(locator).click()
            time.sleep(1)
            for small_position in range(1, Locators.DICT_COL_PRODUCT[locator] + 1):
                if locator == "Screen Recording" and small_position == 4:
                    max_w_m = 3
                elif locator == "For Work" and small_position == 9:
                    max_w_m = 3
                elif locator == "For Education":
                    max_w_m = 2
                for w_m in range(1, max_w_m):
                    print(Locators.DICT_POSITION[locator], small_position, w_m)
                    a = self.chrome.find_element_by_css_selector(
                        f'.v-main-menu-item:nth-child({Locators.DICT_POSITION[locator]}) .v-header-dropdown-item:nth-child({small_position}) .v-header-link:nth-child({w_m})')
                    time.sleep(1)
                    # self.act_first(a)
                    ActionChains(self.chrome) \
                        .move_to_element(a) \
                        .key_down(Keys.CONTROL) \
                        .click(a) \
                        .key_up(Keys.CONTROL) \
                        .perform()
                    time.sleep(1)
                    self.close_last_tab()
            b = self.chrome.find_elements_by_css_selector(
                f'.v-main-menu-item:nth-child({Locators.DICT_POSITION[locator]}) .right-side')

            def get_len_element():
                for f in b:
                    element = f.find_elements_by_css_selector("a")
                    return element

            if locator == 'For Education':
                continue
            for f in range(1, len(get_len_element()) + 1):
                s = self.chrome.find_element_by_css_selector(
                    f'.v-main-menu-item:nth-child({Locators.DICT_POSITION[locator]}) .right-side .v-header-dropdown-item:nth-child({f}) .v-header-link.external')
                time.sleep(1)
                ActionChains(self.chrome) \
                    .move_to_element(s) \
                    .key_down(Keys.CONTROL) \
                    .click(s) \
                    .key_up(Keys.CONTROL) \
                    .perform()
                time.sleep(1)
                self.close_last_tab()

