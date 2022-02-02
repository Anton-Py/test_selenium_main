from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from lib.constants import Locators
from lib.page import MainPage
import pyautogui
import time
import os.path
import urllib.request

# прокрутка баннера и проберка кнопки Learn more и Download for Free
def test_scroll_main_page(chrome):
    page = MainPage(chrome)
    page.go_to_site()
    time.sleep(1)
    for key in range(1, 8):
        page.get_banner(key).click()
        button = page.get_button(key)
        page.tap_element(button)
        page.switch_to_second_tab()
        url = page.chrome.current_url
        assert Locators.BANNERS[key] in url
        page.close_last_tab()
        # time.sleep(2)
        if key != 2 and key != 3:
            page.get_button_download(key).click()
            time.sleep(250)
            # check if file downloaded file path exists
            page.check_downloaded_distributiv(Locators.BANNER_DOWNLOAD_FILES[key])


# pytest tests/test_d_main_banners.py --disable-warnings --tb=short -s -v
# pytest tests --disable-warnings --tb=short -s

