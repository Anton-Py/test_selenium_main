from selenium.webdriver.common.by import By
from lib.constants import Locators
from lib.page import MainPage
# import pyautogui
import time


# ".v-header-link.v-main-menu-logo"
# page.chrome.execute_script('el = document.elementFromPoint(100, 200); el.click();')
def links(page, locator, list_for_assert):
    # print(pyautogui.position())
    # pyautogui.moveTo(100, 200, 2)
    # pyautogui.click(x=100, y=200)
    page.wait_of_element_click(locator).click()
    coll_in_product_block = Locators.COLL_IN_PRODUCT_BLOCK[locator]
    for product_and_win_mac in range(1, Locators.DICT_COL_PRODUCT[locator] + 1):
        if locator == Locators.LOC_UI[2] and product_and_win_mac == 9:
            coll_in_product_block = 3
        elif locator == Locators.LOC_UI[3] and product_and_win_mac == 9:
            coll_in_product_block = 3
        elif locator == Locators.LOC_UI[4]:
            coll_in_product_block = 2
        for win_or_mac in range(1, coll_in_product_block):
            # pyautogui.click(x=100, y=200)
            time.sleep(1)
            page.chrome.execute_script('el = document.elementFromPoint(100, 200); el.click();')
            print("Это раздел меню", locator)
            print("Это позиция элеиента", Locators.DICT_POSITION[locator], product_and_win_mac, win_or_mac)
            # перебор левой части продуктов
            element_left = page.get_element_products(locator, product_and_win_mac, win_or_mac)
            time.sleep(0.5)
            page.tap_element(element_left)
            page.actions_products(product_and_win_mac, list_for_assert, win_or_mac, locator)

    # перебор правой части продуктов
    elements_rite = page.get_element_stocks(locator)
    elements = ''

    for element in elements_rite:
        elements = element.find_elements(By.CSS_SELECTOR, "a")

    for stock in range(1, len(elements) + 1):
        child = page.get_stock_child(locator, stock)
        page.tap_element(child)
        page.actions_stock(list_for_assert, stock)


def test_all_links_dropdown_menu(chrome):
    page = MainPage(chrome)
    page.go_to_site()
    time.sleep(3)
    links(page, Locators.LOC_UI[0], Locators.LIST_VIDEO_HTTPS)
    links(page, Locators.LOC_UI[1], Locators.lIST_SCREEN_RECORDING_HTTPS)
    links(page, Locators.LOC_UI[2], Locators.lIST_PHOTO_HTTPS)
    links(page, Locators.LOC_UI[3], Locators.lIST_FOR_WORK_HTTPS)
    links(page, Locators.LOC_UI[4], Locators.lIST_FOR_EDUCATION_HTTPS)

    # pytest tests/test_c_dropdown_menu_parts.py --tb=short -s -v
