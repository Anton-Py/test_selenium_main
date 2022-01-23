from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from lib.constants import Locators
from lib.core import BasePage
import time


class MainPage(BasePage):

    def action(self, element):
        ActionChains(self.chrome) \
            .move_to_element(element) \
            .key_down(Keys.CONTROL) \
            .click(element) \
            .key_up(Keys.CONTROL) \
            .perform()
        time.sleep(4)

    def act_first(self, tag_name):
        element = self.wait_of_element_located(tag_name)
        ActionChains(self.chrome) \
            .move_to_element(element) \
            .key_down(Keys.CONTROL) \
            .click(element) \
            .key_up(Keys.CONTROL) \
            .perform()

    def actions_left(self, product_and_win_mac, list_for_assert, win_or_mac, locator):
        # wait(self.chrome, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "epik_localstore")))
        # self.chrome.switch_to.default_content()
        if len(self.chrome.window_handles) == 2:
            self.chrome.switch_to.window(window_name=self.chrome.window_handles[1])
            time.sleep(1)
            url = self.chrome.current_url
            # if locator != Locators.LOC_UI[4]:
            #     print(list_for_assert[product_and_win_mac - 1][win_or_mac - 1] in url)
            if locator == Locators.LOC_UI[4] and product_and_win_mac == 2:
                assert (list_for_assert[product_and_win_mac - 2][win_or_mac - 1] in url)
            else:
                assert (list_for_assert[product_and_win_mac - 1][win_or_mac - 1] in url)
        self.chrome.close()
        self.chrome.switch_to.window(window_name=self.chrome.window_handles[0])

    def actions_right(self, list_for_assert, f):
        if len(self.chrome.window_handles) == 2:
            self.chrome.switch_to.window(window_name=self.chrome.window_handles[1])
            time.sleep(2)
            url = self.chrome.current_url
            print(list_for_assert[-1][f - 1] in url)
            assert ("This is assert: ", list_for_assert[-1][f - 1] in url)
            self.chrome.close()
            self.chrome.switch_to.window(window_name=self.chrome.window_handles[0])

    # def handle(self):
    #     default_handle = self.chrome.window_handles
    #     self.chrome.switch_to.window(default_handle[1])
    #     return default_handle
    #
    # def switch_to(self):
    #     self.chrome.switch_to.window(self.handle()[0])
    #     default_handle = self.chrome.current_window_handle
    #     handles = list(self.chrome.window_handles)
    #     assert len(handles) > 1
    #     handles.remove(default_handle)
    #     assert len(handles) > 0
    #     self.chrome.switch_to.window(handles[0])
    #     self.chrome.close()
    #     self.chrome.switch_to.window(default_handle)

    # def close_last_tab(self):
    #     if len(self.chrome.window_handles) == 2:
    #         self.chrome.switch_to.window(window_name=self.chrome.window_handles[1])
    #         time.sleep(2)
    #         self.chrome.close()
    #         self.chrome.switch_to.window(window_name=self.chrome.window_handles[0])

    def block_with_products_from_the_left(self, locator, product_and_win_mac, win_or_mac):
        element = self.chrome.find_element(By.CSS_SELECTOR,
                                           f'.v-main-menu-item:nth-child({Locators.DICT_POSITION[locator]}) .v-header-dropdown'
                                           f'-item:nth-child({product_and_win_mac}) .v-header-link:nth-child({win_or_mac})')
        return element

    def block_with_products_from_the_right(self, locator):
        elements = self.chrome.find_elements(By.CSS_SELECTOR,
                                             f'.v-main-menu-item:nth-child({Locators.DICT_POSITION[locator]}) .right-side')

        return elements

    def num_child_for_right_block(self, locator, i):
        element = self.chrome.find_element(By.CSS_SELECTOR,
                                           f'.v-main-menu-item:nth-child({Locators.DICT_POSITION[locator]}) .right-side .v-header-dropdown-item:nth-child({i}) .v-header-link.external')
        time.sleep(1)

        return element
