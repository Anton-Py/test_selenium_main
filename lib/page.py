from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from lib.constants import Locators
from lib.core import BasePage
import pyautogui
import os.path
import time


class MainPage(BasePage):

    def tap_element(self, element):
        ActionChains(self.chrome) \
            .move_to_element(element) \
            .key_down(Keys.CONTROL) \
            .click(element) \
            .key_up(Keys.CONTROL) \
            .perform()
        time.sleep(4)
        pyautogui.click()

    def tap_tag(self, tag_name):
        element = self.wait_of_element_located(tag_name)
        ActionChains(self.chrome) \
            .move_to_element(element) \
            .key_down(Keys.CONTROL) \
            .click(element) \
            .key_up(Keys.CONTROL) \
            .perform()

    def actions_products(self, product_and_win_mac, list_for_assert, win_or_mac, locator):
        if len(self.chrome.window_handles) == 2:
            self.chrome.switch_to.window(window_name=self.chrome.window_handles[1])
            time.sleep(1)
            url = self.chrome.current_url
            if locator == Locators.LOC_UI[4] and product_and_win_mac == 2:
                assert (list_for_assert[product_and_win_mac - 2][win_or_mac - 1] in url)
            else:
                assert (list_for_assert[product_and_win_mac - 1][win_or_mac - 1] in url)
            self.chrome.close()
            self.chrome.switch_to.window(window_name=self.chrome.window_handles[0])

    def actions_stock(self, list_for_assert, stock):
        if len(self.chrome.window_handles) == 2:
            self.chrome.switch_to.window(window_name=self.chrome.window_handles[1])
            time.sleep(2)
            url = self.chrome.current_url
            assert ("This is assert: ", list_for_assert[-1][stock - 1] in url)
            self.chrome.close()
            self.chrome.switch_to.window(window_name=self.chrome.window_handles[0])

    def get_element_products(self, locator, product_and_win_mac, win_or_mac):
        element = self.chrome.find_element(
            By.CSS_SELECTOR,
            f'.v-main-menu-item:nth-child({Locators.DICT_POSITION[locator]}) .v-header-dropdown'
            f'-item:nth-child({product_and_win_mac}) .v-header-link:nth-child({win_or_mac})'
        )
        return element

    def get_element_stocks(self, locator):
        elements = self.chrome.find_elements(
            By.CSS_SELECTOR,
            f'.v-main-menu-item:nth-child({Locators.DICT_POSITION[locator]}) .right-side'
        )

        return elements

    def get_stock_child(self, locator, i):
        element = self.chrome.find_element(
            By.CSS_SELECTOR,
            f'.v-main-menu-item:nth-child({Locators.DICT_POSITION[locator]}) .right-side .v-header-dropdown-item:nth-child({i}) .v-header-link.external'
        )
        time.sleep(1)

        return element

    def get_banner(self, key):
        element = self.chrome.find_element(
            By.CSS_SELECTOR,
            f".banner-carousel-dots > .carousel-dot:nth-child({key})"
        )

        return element

    def get_button(self, key):
        element = self.chrome.find_element(
            By.CSS_SELECTOR,
            f".carousel-slide:nth-child({key + 1}) > .container .btn:nth-child(1) > .link-title"
        )

        return element

    def get_button_download(self, key):
        element = self.chrome.find_element(
            By.CSS_SELECTOR,
            f".carousel-slide:nth-child({key + 1}) > .container .btn:nth-child(3) > .link-title"
        )

        return element


    # def check_downloaded_files(self, element):
    #     while not os.path.exists('D:\\Main_test_one_file\\test_main\\First\\download_files\\'):
    #         time.sleep(2)
    #     # check file
    #         if os.path.isfile(f'D:\\Main_test_one_file\\test_main\\First\\download_files\\{element}'):
    #             print(f"File download: {element} is completed")
    #         else:
    #             print(f"File download: {element} is not completed")
    #         time.sleep(3)
    #         os.remove(f'D:\\Main_test_one_file\\test_main\\First\\download_files\\{element}')