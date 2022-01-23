from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from lib.core import BasePage
from lib.constants import Locators
from lib.page import MainPage
import time


def test_all_links_dropdown_menu(chrome):
    page = MainPage(chrome)
    page.go_to_site()
    time.sleep(3)
    for locator in Locators.LOC_UI:
        coll_in_product_block = 4
        page.wait_of_element_click(locator).click()
        time.sleep(1)
        for product_and_win_mac in range(1, Locators.DICT_COL_PRODUCT[locator] + 1):
            # если LOC_UI==video, то берем список ссылок для видео и сравниваем в assert и т.д
            if locator == 'Video':
                list_for_assert = Locators.LIST_VIDEO_HTTPS
            elif locator == "Screen Recording":
                if product_and_win_mac == 4:
                    coll_in_product_block = 3
                list_for_assert = Locators.lIST_SCREEN_RECORDING_HTTPS
            elif locator == "Photo":
                list_for_assert = Locators.lIST_PHOTO_HTTPS
            elif locator == "For Work":
                if product_and_win_mac == 9:
                    coll_in_product_block = 3
                list_for_assert = Locators.lIST_FOR_WORK_HTTPS
            elif locator == "For Education":
                coll_in_product_block = 2
                list_for_assert = Locators.lIST_FOR_EDUCATION_HTTPS
            for win_or_mac in range(1, coll_in_product_block):
                print(locator)
                print(Locators.DICT_POSITION[locator], product_and_win_mac, win_or_mac)
                # перебор левой части продуктов
                block_with_products_from_the_left = page.chrome.find_element_by_css_selector(
                    f'.v-main-menu-item:nth-child({Locators.DICT_POSITION[locator]}) .v-header-dropdown-item:nth-child({product_and_win_mac}) .v-header-link:nth-child({win_or_mac})')
                time.sleep(2)
                page.action(block_with_products_from_the_left)
                if len(page.chrome.window_handles) == 2:
                    page.chrome.switch_to.window(window_name=page.chrome.window_handles[1])
                    time.sleep(3)
                    # если Gecata то проверяем ссылку, то особые условия проверки, ссылка страницы находится в другом теге
                    if locator == "Screen Recording" and product_and_win_mac == 4:
                        link = page.chrome.find_element_by_css_selector('link[rel="canonical"][href]')
                        link = link.get_attribute('href')
                        print("Gecata href: ", link)
                    # если pdfchef.com/, то особые условия проверки, ссылка страницы находится в другом теге
                    elif locator == "For Work" and product_and_win_mac == 7:
                        if win_or_mac == 1 or win_or_mac == 2:
                            print("For Work: ", win_or_mac)
                            link = page.chrome.find_element_by_css_selector('link[rel="icon"][href]')
                            link = link.get_attribute('href')
                            print("link = 1 or 2: ", link)
                        else:
                            link = page.chrome.find_element_by_css_selector('link[hreflang="x-default"][href]')
                            link = link.get_attribute('href')
                            print("W_m: ", win_or_mac, link)
                    # если For Education, то особые условия проверки, ссылка страницы находится в другом теге
                    elif locator == "For Education":
                        link = page.chrome.find_element_by_css_selector('link[rel="canonical"][href]')
                        link = link.get_attribute('href')
                        if product_and_win_mac == 1:
                            print("For constains: ", list_for_assert[product_and_win_mac - 1][win_or_mac - 1])
                            assert (list_for_assert[product_and_win_mac - 1][win_or_mac - 1] in link)
                        else:
                            print("For constains: ",
                                  list_for_assert[product_and_win_mac - 2][win_or_mac - 1] in link)
                            assert (list_for_assert[product_and_win_mac - 2][win_or_mac - 1] in link)
                        print("EDU href: ", link)
                    else:
                        link = page.chrome.find_element_by_css_selector('link[hreflang="x-default"][href]')
                        link = link.get_attribute('href')
                        print("For constains: ", list_for_assert[product_and_win_mac - 1][win_or_mac - 1])
                        print("defoult link: ", link)
                        print()
                        # if locator == "For Education":
                        #     if product_and_win_mac == 1:
                        #         print("For constains: ", list_for_assert[product_and_win_mac - 1][win_or_mac - 1])
                        #         assert (list_for_assert[product_and_win_mac - 1][win_or_mac - 1] in link)
                        #     else:
                        #         print("For constains: ", list_for_assert[product_and_win_mac - 2][win_or_mac - 1] in link)
                        #         assert (list_for_assert[product_and_win_mac - 2][win_or_mac - 1] in link)
                        assert (list_for_assert[product_and_win_mac - 1][win_or_mac - 1] in link)
                    page.chrome.close()
                    page.chrome.switch_to.window(window_name=page.chrome.window_handles[0])

        # перебор правой части продуктов
        block_with_products_from_the_right = page.chrome.find_elements_by_css_selector(
            f'.v-main-menu-item:nth-child({Locators.DICT_POSITION[locator]}) .right-side')

        lst = []
        for f in block_with_products_from_the_right:
            element = f.find_elements_by_css_selector("a")
            for link in element:
                lst.append(link.get_attribute('href'))
            print("List: ", lst)
        if locator == 'For Education':
            continue
        if locator == 'Video':
            list_for_assert = Locators.LIST_VIDEO_HTTPS[-1]
        elif locator == "Screen Recording":
            list_for_assert = Locators.lIST_SCREEN_RECORDING_HTTPS[-1]
        elif locator == "Photo":
            list_for_assert = Locators.lIST_PHOTO_HTTPS[-1]
        elif locator == "For Work":
            list_for_assert = Locators.lIST_FOR_WORK_HTTPS[-1]
        for f in range(1, len(element) + 1):
            s = page.chrome.find_element_by_css_selector(
                f'.v-main-menu-item:nth-child({Locators.DICT_POSITION[locator]}) .right-side .v-header-dropdown-item:nth-child({f}) .v-header-link.external')
            time.sleep(1)
            page.action(s)
            # ActionChains(self.chrome) \
            #     .move_to_element(s) \
            #     .key_down(Keys.CONTROL) \
            #     .click(s) \
            #     .key_up(Keys.CONTROL) \
            #     .perform()
            # time.sleep(1)
            if len(page.chrome.window_handles) == 2:
                page.chrome.switch_to.window(window_name=page.chrome.window_handles[1])
                time.sleep(3)
                print("Links: ", list_for_assert[f - 1], lst[f - 1])
                assert ("This is assert: ", list_for_assert[f - 1] in lst[f - 1])
                page.chrome.close()
                page.chrome.switch_to.window(window_name=page.chrome.window_handles[0])
            # self.close_last_tab()
