import pytest
from selenium import webdriver


@pytest.yield_fixture
def chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": r"D:\Main_test_one_file\test_main\First\download_files",
        "safebrowsing.enabled": "false",
        # "download.prompt_for_download": False,
        "download.directory_upgrade": True
        # "safebrowsing.enabled": True
    })
    chrome = webdriver.Chrome(options=chrome_options)
    yield chrome
    chrome.quit()
