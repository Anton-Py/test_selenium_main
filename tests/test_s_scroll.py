from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from lib.constants import Locators
from lib.page import MainPage
import pyautogui
import time
import os.path
import urllib.request

# скролл страницы до 4 кругляжков и проверка каждого на переход в продукт и что продукт скачивается
def test_scroll_main_page(chrome):
    page = MainPage(chrome)
    page.go_to_site()
    time.sleep(1)
    page.chrome.execute_script("window.scrollBy(0,1030)")
    # time.sleep(1)
    for key in range(1, 5):
        pyautogui.click()
        page.wait_of_element_located(Locators.LEARN_MORE_DICT[key]).click()
        time.sleep(2)
        pyautogui.click()
        button = page.wait_of_element_located(Locators.LEARN_MORE_DICT_CSS_SELECTOR[key])
        page.tap_element(button)
        page.switch_to_second_tab()
        url = page.chrome.current_url
        assert Locators.LEARN_MORE_DICT_URL[key] in url
        page.close_last_tab()
        page.wait_of_element_located(Locators.DOWNLOAD_LINKS[key]).click()
        time.sleep(55)
        # check if file downloaded file path exists
        page.check_downloaded_files(Locators.NAME_DOWNLOAD_FILES[key])

# pytest tests/test_s_scroll.py --disable-warnings --tb=short -s
# pytest tests --disable-warnings --tb=short -s

