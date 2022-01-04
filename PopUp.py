import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from lib.basepage import BasePage
from lib.constants import *


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
    def test_main_page(self):
        main_page = self.wait_of_element_located(MovaviLocators.LOCATOR_MN_PAGE)
        assert main_page.text == TITLE_TXT
        try:

            driver.switch_to.frame(element)
            self.chrome.switch_to.frame("iframe")
            self.chrome.find_element_by_tag_name("iframe")
            self.chrome.find_element_css_selector('[class="CloseButton__ButtonElement-sc-79mh24-0 gapnof luverne-CloseButton luverne-close luverne-ClosePosition--top-right"]').click()
        finally:
            for dict_window_key in DICT_WINDOWS:
                tag_name = DICT_WINDOWS[dict_window_key]
                self.act_first(tag_name)
                self.handle()
                url = self.chrome.current_url
                assert (ASRT[0] in url) or (ASRT[1] in url) or (ASRT[2] in url) or (ASRT[3] in url) or (ASRT[4] in url)
                self.switch_to()



    #
    # # Проверяем кнопку поиска в хедере
    # def site_search(self):
    #     self.wait_of_element_located(MovaviLocators.LOCATOR_HAD_SEARCH).click()
    #     self.wait_of_element_located(MovaviLocators.LOCATOR_ENTR_FIRLD).send_keys(TEXT_SEARCH)
    #     self.act_second()
    #     self.handle()
    #     time.sleep(2)
    #     body_text = self.chrome.find_element_by_tag_name('body').text
    #     # print(type(body_text))
    #     print(body_text)
    #     assert PAGE_SORCE_ONE in body_text, "страница не соответствует запросу"
    #     self.chrome.switch_to.window(self.handle()[0])
    #     self.switch_to()


    # def main_video_experiment(self):
    #     time.sleep(3)
    #     for locator in LOC_UI:
    #         max_w_m = 4
    #         self.wait_of_element_click(locator).click()
    #         time.sleep(1)
    #         for small_position in range(1, DICT_COL_PRODUCT[locator] + 1):
    #             if locator == "Screen Recording" and small_position == 4:
    #                 max_w_m = 3
    #             elif locator == "For Work" and small_position == 9:
    #                 max_w_m = 3
    #             elif locator == "For Education":
    #                 max_w_m = 2
    #             for w_m in range(1, max_w_m):
    #                 print(DICT_POSITION[locator], small_position, w_m)
    #                 a = self.chrome.find_element_by_css_selector(
    #                     f'.v-main-menu-item:nth-child({DICT_POSITION[locator]}) .v-header-dropdown-item:nth-child({small_position}) .v-header-link:nth-child({w_m})')
    #                 time.sleep(1)
    #                 ActionChains(self.chrome) \
    #                     .move_to_element(a) \
    #                     .key_down(Keys.CONTROL) \
    #                     .click(a) \
    #                     .key_up(Keys.CONTROL) \
    #                     .perform()
    #                 time.sleep(1)
    #                 self.close_last_tab()
    #         b = self.chrome.find_elements_by_css_selector(f'.v-main-menu-item:nth-child({DICT_POSITION[locator]}) .right-side')
    #         def get_len_element():
    #             for f in b:
    #                 element = f.find_elements_by_css_selector("a")
    #                 return element
    #         if locator == 'For Education':
    #             continue
    #         for f in range(1, len(get_len_element()) + 1):
    #             s = self.chrome.find_element_by_css_selector(f'.v-main-menu-item:nth-child({DICT_POSITION[locator]}) .right-side .v-header-dropdown-item:nth-child({f}) .v-header-link.external')
    #             time.sleep(1)
    #             ActionChains(self.chrome) \
    #                 .move_to_element(s) \
    #                 .key_down(Keys.CONTROL) \
    #                 .click(s) \
    #                 .key_up(Keys.CONTROL) \
    #                 .perform()
    #             time.sleep(1)
    #             self.close_last_tab()






                    # a = self.chrome.find_element_by_css_selector(
                    #     f'.v-main-menu-item:nth-child({position}) .v-header-dropdown-item:nth-child(1) .v-header-link:nth-child(2)').click()
                    # time.sleep(4)
            # for small_position in range(1, 8):
            #     for w_m in (2, 3):
            #         a = self.chrome.find_element_by_css_selector(
            #             f'.v-main-menu-item:nth-child({position}) .v-header-dropdown-item:nth-child({small_position}) .v-header-link:nth-child({w_m})')
            #         a.click()
            # self.act_first(a)
            # time.sleep(7)
            # self.handle()
            # time.sleep(7)
            # self.close_last_tab()
            # time.sleep(4)

        ##### '.v-main-menu-item:nth-child(1) .right-side .v-header-dropdown-item:nth-child(1) .v-header-link.external'

        #             el = self.chrome.find_elements_by_css_selector(".v-header-dropdown-item")
        #             lst = []
        #             for f in el:
        #                 element = f.find_elements_by_css_selector("li a")
        #                 for link in element:
        #                     lst.append(link.get_attribute('href'))
        #             print(lst)

    # Получаем текст всех ссылок, но при клике на win и mac мы попадаем на первые в списке
    # def main_video(self):
    #     lst = []
    #     self.wait_of_element_located_text("Video").click()
    #     time.sleep(10)
    # for f in element_located:
    #     block = self.wait_of_element_located(f)
    # block = self.wait_of_element_located('[class="v-header-dropdown full-width dropdown-row v-main-menu-dropdown"]')
    # block = self.chrome.find_element_by_xpath('//*[@id="app"]/header/nav/div[2]/div[2]/ul/li[1]/div/div/ul[1]')
    # block = self.wait_of_element_located('[class ="v-header-dropdown-item unlimited"]')
    # block = self.wait_of_element_located('[class="v-header-dropdown-item videoSuite"]')
    # block = self.wait_of_element_located('[class ="v-header-dropdown-item videoEditorPlus"]')
    # block = self.wait_of_element_located('[class="v-header-dropdown-item slideshowMaker"]')
    # block = self.wait_of_element_located('[class="v-header-dropdown-item videoSuiteBusiness"]')
    # block = self.wait_of_element_located('[class="v-header-dropdown-item videoConverter"]')
    # block = self.wait_of_element_located('[class="v-header-dropdown-item effectsStore"]')
    # block = self.wait_of_element_located('[class="v-header-dropdown-item stockVideo only-desktop"]')
    # block = self.wait_of_element_located('[class="v-header-dropdown-item stockAudio only-desktop"]')
    # block = self.wait_of_element_located('[class="v-header-dropdown-item stockPhotos only-desktop"]')

    # time.sleep(10)
    #
    # links = block.find_elements_by_tag_name("a")
    # lst = []
    # for link in links:
    #     a = link.text
    #     if a == '':
    #         continue
    #     if "mobile" in a:
    #         a = a[:-7]
    #     if "new" in a:
    #         a = a[:-4]
    #     # a = link.get_attribute("href")
    #     lst.append(a)
    #     time.sleep(2)
    #     print(lst)
    #
    # for a in lst:
    #     # time.sleep(2)
    #     self.act_ui(a)
    #     time.sleep(7)
    #     self.handle()
    #     time.sleep(7)
    #     self.close_last_tab()

    # Проверяем For Education
    # def for_education(self):
    #     for locator in LOC_UI_For_Education:
    #         self.wait_of_element_located_text(locator).click()
    #         # qw = self.wait_of_element_located('[class="v-header-dropdown full-width dropdown-row v-main-menu-dropdown"]')
    #         block = self.chrome.find_element_by_xpath('//*[@id="app"]/header/nav/div/div[2]/ul/li[5]/div')
    #         links = block.find_elements_by_tag_name("a")
    #         # links = self.wait_of_element_located_tag_name("a")
    #         for link in links:
    #             a = link.text
    #             print(a)
    # self.wait_of_element_click(a).click()
    # time.sleep(2)
    # self.act_first_for_links(a)
    # time.sleep(2)
    # self.handle()
    # time.sleep(2)
    # self.chrome.switch_to.window(self.handle()[0])
    # self.switch_to()

    # self.wait_of_element_located(loc)

    # ul = self.wait_of_elements_located_css(".v-header-dropdown-item")
    # lst = []
    # for link in ul:
    #     st = link.text
    #     # print(st)
    #     st = link.text.splitlines()
    #     lst.append(st)
    # print(lst)

    # block = self.chrome.find_element_by_css_selector('[class="list left-side"]')
    # time.sleep(1)
    # all_vid = block.find_elements_by_tag_name("v-header-dropdown-item")
    # all_vid = block.find_elements_by_tag_name("a")
    # # # получили список всех видео
    # values = []
    # for video in all_vid:
    #     atribs = video.get_attribute("href")
    #     values.append(atribs)
    #
    # print(values)
    #     hrefs = [x.get_attribute('href') for x in link.find_elements_by_css_selector('a')]
    #     print(hrefs)

# Как вариан вытащил ссылки
#             el = self.chrome.find_elements_by_css_selector(".v-header-dropdown-item")
#             lst = []
#             for f in el:
#                 element = f.find_elements_by_css_selector("li a")
#                 for link in element:
#                     lst.append(link.get_attribute('href'))
#             print(lst)


# for link in ul:
#     st = link.find_elements_by_tag_name("li a")
#     for video in st:
#         atribs = video.get_partial_link_text('')
#         values.append(atribs)
# print(values)

# Как вариант
#             uli = self.chrome.find_element_by_xpath(
#                 '//*[@id="app"]/header/nav/div[2]/div[2]/ul/li[1]/div/div/ul[1]/li[2]')
#             ul = uli.find_elements_by_tag_name("a")
#             # ul = self.chrome.find_elements_by_xpath(".v-header-dropdown-item")
#             values = []
#             for video in ul:
#                 atribs = video.get_attribute("href")
#                 values.append(atribs)
#             print(values)


# .v-header-dropdown-item
