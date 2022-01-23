from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from lib.core import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from lib.constants import Locators
from lib.page import MainPage
import pyautogui
import time


def links(page, locator, list_for_assert):
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
            print(locator)
            print(Locators.DICT_POSITION[locator], product_and_win_mac, win_or_mac)
            # перебор левой части продуктов
            element_left = page.block_with_products_from_the_left(locator, product_and_win_mac, win_or_mac)
            time.sleep(0.5)
            page.action(element_left)
            page.actions_left(product_and_win_mac, list_for_assert, win_or_mac, locator)
    # перебор правой части продуктов
    element_rite = page.block_with_products_from_the_right(locator)
    elements = ''
    for f in element_rite:
        elements = f.find_elements(By.CSS_SELECTOR, "a")
    for i in range(1, len(elements) + 1):
        child = page.num_child_for_right_block(locator, i)
        page.action(child)
        page.actions_right(list_for_assert, i)


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
