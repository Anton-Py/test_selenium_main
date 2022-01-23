from selenium.webdriver.common.by import By
from lib.constants import Locators
from lib.page import MainPage
import pyautogui
import time
import os.path


def test_download(chrome):
    chrome.get("https://www.seleniumhq.org/download/")
    # click download link
    l = chrome.find_element_by_link_text("32 bit Windows IE")
    time.sleep(1)
    l.click()
    time.sleep(3)
    # check if file downloaded file path exists
    # while not os.path.exists('DD:\\Main_test_one_file\\test_main\\First\\download_files\\'):
    #     time.sleep(2)
    #     # check file
    if os.path.isfile('D:\\Main_test_one_file\\test_main\\First\\download_files\\IEDriverServer_Win32_4.0.0.zip'):
        print("File download is completed")
    else:
        print("File download is not completed")
    time.sleep(10)
    os.remove('D:\\Main_test_one_file\\test_main\\First\\download_files\\IEDriverServer_Win32_4.0.0.zip')
    # close browser
    # driver.quit()
