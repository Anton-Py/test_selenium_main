import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope="session")
def chrome():
    '''
    Фикстура для настройки вебрайвера Chrome с заданными аргументами
    '''
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--whitelisted-ips")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_extension('../modify_header/ModHeader_2.3.9_0.crx')
    # chrome = webdriver.Remote('http://selenium-chrome:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME, options=chrome_options)
    # для локального запуска оставляю эту строчку:
    chrome = webdriver.Chrome(options=chrome_options)
    yield chrome
    chrome.quit()


@pytest.fixture
def set_ip():
    '''
    Фикстура для настройки заголовка для изменения ip
    принимает на вход драйвер и ip в виде строки
    '''

    def set(chrome, ip):
        chrome.get('chrome-extension://idgpnmonknjnojddfkpgkljpfnnfcklj/icon.png')

        script = "localStorage.setItem('profiles', JSON.stringify([{title: 'Selenium', hideComment: true, appendMode: '', headers: ["
        script += "{enabled: true, name: 'X-Forwarded-For', value: '" + ip + "', comment: ''},"
        script += "],respHeaders:[],filters:[]}]));"

        chrome.execute_script(script)
    return set
