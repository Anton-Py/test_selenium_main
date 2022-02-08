# Настройки телебота
# TOKEN = '1701745703:AAEMMJNaqoLBhdNvJxgt4NqZ-09DIDI2NRU'
# ID_CHANNEL = 387545645


class Locators:
    # ссылка на сайт
    SITE = "https://movavi.com"
    # SITE = "https://vdusheyko-php74.sandbox.movavi.com/"
    # проверка по селектору и что текст соответствует
    MAIN_TEXT = "span.title"
    TITLE_TEXT = "Work with multimedia anywhere"

    # поиск баннера
    BANNER_CONTENT = '[class="banner-title d-none d-xl-block"]'
    BANNER_BUTTON = '[class="btn inverse"]'

    # текст баннера
    TEXT_FOR_FIRST_BANNER = "Try Movavi Video Suite – an all-in-one video maker, perfect for remote work and distance learning."

    # словарь ссылк для проверки хедера
    DICT_WINDOWS = {'store': '[href="/store/?asrc=main_menu"]',
                    'support': '[href="/support/?asrc=main_menu"]',
                    'how-to': '[href="/support/how-to/?asrc=main_menu"]',
                    'blog': '[href="https://movavi.io/?asrc=main_menu"]',
                    'My Account': '[href="https://movavi.id/?lng=en&asrc=main_menu"]'}

    # список для проверки ссылки после клика в хедере, что перешли на нужный URL
    HEADER_TOP_SIDEBAR_LINKS = {'store': 'https://www.movavi.com/store/?asrc=main_menu',
                                'support': 'https://www.movavi.com/support/?asrc=main_menu',
                                'how-to': 'https://www.movavi.com/support/how-to/?asrc=main_menu',
                                'blog': 'https://www.movavi.io/?asrc=main_menu',
                                'My Account': 'https://movavi.id/login?lng=en&asrc=main_menu'}

    # список локаторов для поиска (открыть, ввести текст)
    HEADER_SEARCH = '[class="v-header-search"]'
    ENTRY_FIELD = 'div label input[placeholder="Search on movavi.com"]'
    TEXT_SEARCH = "screen recorder"
    SEARCH = '[class="v-header-link external"]'
    SEARCH_RESULT_TEXT = "Screen Recorder for Perfect Captures - Movavi"

    # список разделов из выпадающего списка
    LOC_UI = ('Video', 'Screen Recording', 'Photo', 'For Work', 'For Education')
    DICT_POSITION = {'Video': 1, 'Screen Recording': 2, 'Photo': 3, 'For Work': 4, 'For Education': 5}
    DICT_COL_PRODUCT = {'Video': 7, 'Screen Recording': 4, 'Photo': 4, 'For Work': 9, 'For Education': 2}
    COLL_IN_PRODUCT_BLOCK = {'Video': 4, 'Screen Recording': 3, 'Photo': 4, 'For Work': 4, 'For Education': 2}

    # ссылка на странице для assert
    MAIN_LINK_IN_PAGE_OLL = 'link[hreflang="x-default"][href]'
    MAIN_LINK_IN_PAGE_SR_AND_EDUCATION = 'link[rel="canonical"][href]'

    # список ссылок для проверки в assert для меню
    LIST_VIDEO_HTTPS = [["https://www.movavi.com/android-video-editor",
                         "https://www.movavi.com/android-video-editor",
                         "https://www.movavi.com/ios-video-editor"],

                        ["https://www.movavi.com/suite-unlimited",
                         "https://www.movavi.com/suite-unlimited",
                         "https://www.movavi.com/suite-unlimited-mac"],

                        ["https://www.movavi.com/video-suite",
                         "https://www.movavi.com/video-suite",
                         "https://www.movavi.com/suite-mac"],

                        ["https://www.movavi.com/videoeditor",
                         "https://www.movavi.com/videoeditor",
                         "https://www.movavi.com/video-editor-plus-mac"],

                        ["https://www.movavi.com/slideshow-maker",
                         "https://www.movavi.com/slideshow-maker",
                         "https://www.movavi.com/slideshow-maker-for-mac"],

                        ["https://www.movavi.com/business-suite.html",
                         "https://www.movavi.com/business-suite.html",
                         "https://www.movavi.com/business-suite-mac.html"],

                        ["https://www.movavi.com/movavi-video-converter",
                         "https://www.movavi.com/movavi-video-converter",
                         "https://www.movavi.com/videoconvertermac"],

                        ["https://effects-store.movavi.com",
                         "https://www.movavi.com/stock-video-footage",
                         "https://www.movavi.com/stock-music",
                         "https://www.movavi.com/stock-photos"]
                        ]

    lIST_SCREEN_RECORDING_HTTPS = [["https://www.movavi.com/suite-unlimited",
                                    "https://www.movavi.com/suite-unlimited",
                                    "https://www.movavi.com/suite-unlimited-mac"],

                                   ["https://www.movavi.com/video-suite",
                                    "https://www.movavi.com/video-suite",
                                    "https://www.movavi.com/suite-mac"],

                                   ["https://www.movavi.com/screen-recorder",
                                    "https://www.movavi.com/screen-recorder",
                                    "https://www.movavi.com/movavi-screen-recorder-mac"],

                                   ["https://www.gecata.com",
                                    "https://www.gecata.com"],

                                   ["https://effects-store.movavi.com",
                                    "https://www.movavi.com/stock-video-footage",
                                    "https://www.movavi.com/stock-music",
                                    "https://www.movavi.com/stock-photos"]]

    lIST_PHOTO_HTTPS = [["https://www.movavi.com/suite-unlimited",
                         "https://www.movavi.com/suite-unlimited",
                         "https://www.movavi.com/suite-unlimited-mac"],

                        ["https://www.movavi.com/photo-editor",
                         "https://www.movavi.com/photo-editor",
                         "https://www.movavi.com/mac-photo-editor"],

                        ["https://www.movavi.com/mobile-photo-editor.html",
                         "https://www.movavi.com/mobile-photo-editor.html",
                         "https://www.movavi.com/mobile-photo-editor.html"],

                        ["https://www.movavi.com/slideshow-maker",
                         "https://www.movavi.com/slideshow-maker",
                         "https://www.movavi.com/slideshow-maker-for-mac"],

                        ["https://effects-store.movavi.com/",
                         "https://www.movavi.com/stock-music",
                         "https://www.movavi.com/stock-photos"]]

    lIST_FOR_WORK_HTTPS = [["https://www.movavi.com/suite-unlimited",
                            "https://www.movavi.com/suite-unlimited",
                            "https://www.movavi.com/suite-unlimited-mac"],

                           ["https://www.movavi.com/business-suite.html",
                            "https://www.movavi.com/business-suite.html",
                            "https://www.movavi.com/business-suite-mac.html"],

                           ["https://www.movavi.com/videoeditor",
                            "https://www.movavi.com/videoeditor",
                            "https://www.movavi.com/video-editor-plus-mac"],

                           ["https://www.movavi.com/screen-recorder-for-business.html",
                            "https://www.movavi.com/screen-recorder-for-business.html",
                            "https://www.movavi.com/screen-recorder-mac-for-business.html"],

                           ["https://www.movavi.com/videoconverter",
                            "https://www.movavi.com/videoconverter/",
                            "https://www.movavi.com/videoconvertermac"],

                           ["https://www.movavi.com/photo-editor",
                            "https://www.movavi.com/photo-editor",
                            "https://www.movavi.com/mac-photo-editor"],

                           ["https://pdfchef.com/pdf-editor",
                            "https://pdfchef.com/pdf-editor",
                            "https://pdfchef.com/pdf-editor-mac"],

                           ["https://www.movavi.com/slideshow-maker",
                            "https://www.movavi.com/slideshow-maker",
                            "https://www.movavi.com/slideshow-maker-for-mac"],

                           ["https://pdfchef.com/pdfchef-scanner.html",
                            "https://pdfchef.com/pdfchef-scanner.html"],

                           ["https://effects-store.movavi.com/"]]

    lIST_FOR_EDUCATION_HTTPS = [["https://www.edu.movavi.com",
                                 "https://www.edu.movavi.com/academic-for-schools"]]
    # данные для перебор продуктов в круглишках 4 шт. Для нажатия на learn more и скачивания
    NUMBER_OF_ROUNDS = 4

    LEARN_MORE_DICT = {0: '[alt = "Edit videos"]',
                       1: '[alt="Capture<br/>screens"]',
                       2: '[alt="Convert media"]',
                       3: '[alt="Edit photos"]'}
    # вопрос почему так работает, выдает как список если перебирать lst_pages и pages
    lst_pages = ('[alt = "Edit videos"]', '[alt="Capture<br/>screens"]', '[alt="Convert media"]', '[alt="Edit photos"]')
    pages = ["Edit videos", "Capture", "Convert media", "Edit photos"]

    LEARN_MORE_DICT_CSS_SELECTOR = {0: '.carousel-slide:nth-child(2) .desc-links > .btn > .link-title',
                                    1: '.carousel-slide:nth-child(3) .desc-links > .btn > .link-title',
                                    2: '.carousel-slide:nth-child(4) .desc-links > .btn > .link-title',
                                    3: '.carousel-slide:nth-child(5) .desc-links > .btn > .link-title'}

    LEARN_MORE_DICT_URL = {0: 'https://www.movavi.com/video-editor-plus',
                           1: 'https://www.movavi.com/screen-recorder',
                           2: 'https://www.movavi.com/movavi-video-converter',
                           3: 'https://www.movavi.com/photo-editor'}

    DOWNLOAD_LINKS = {0: '.carousel-slide:nth-child(2) > .row .btn:nth-child(2) > .link-title',
                      1: '.carousel-slide:nth-child(3) .btn:nth-child(2)',
                      2: '.carousel-slide:nth-child(4) .btn:nth-child(2) > .link-title',
                      3: '.carousel-slide:nth-child(5) > .row .btn:nth-child(2) > .link-title'}

    NAME_DOWNLOAD_FILES = {0: 'MovaviVideoEditorPlusSetupC.exe',
                           1: 'MovaviScreenRecorderSetupC.exe',
                           2: 'MovaviVideoConverterSetupC.exe',
                           3: 'MovaviPicverseSetupC.exe'}

    LOOKING_FOR_URLS = {0: "https://www.movavi.com/store",
                        1: "https://www.movavi.com/store/mac",
                        2: "https://www.movavi.com/support/"}

    LOOKING_FOR_SELECTORS = {0: "div:nth-child(1) > a.btn.btn-support.outline-primary",
                             1: ".support-link > span",
                             2: "div:nth-child(2) > a.btn.btn-support.outline-primary"}

    # данные для проверки блока баннер на главной странице
    BANNERS = {1: "https://www.movavi.com/video-suite-new",
               2: "https://www.movavi.com/suite-unlimited",
               3: "https://effects-store.movavi.com",
               4: "https://www.movavi.com/photo-editor",
               5: "https://www.movavi.com/video-editor-plus",
               6: "https://www.movavi.com/slideshow-maker",
               7: "https://www.movavi.com/screen-recorder"}

    BANNER_DOWNLOAD_FILES = {1: 'MovaviVideoSuiteSetupC.exe',
                             4: 'MovaviPicverseSetupC.exe',
                             5: 'MovaviVideoEditorPlusSetupC.exe',
                             6: 'MovaviSlideshowMakerSetupC.exe',
                             7: 'MovaviScreenRecorderSetupC.exe'}







# block = self.wait_of_element_located('[class="v-header-dropdown full-width dropdown-row v-main-menu-dropdown"]')
# block = self.chrome.find_element_by_xpath('//*[@id="app"]/header/nav/div[2]/div[2]/ul/li[1]/div/div/ul[1]')
# block = self.wait_of_element_located('[class ="v-header-dropdown-item unlimited"]')
# block = self.wait_of_element_located('[class="v-header-dropdown-item videoSuite"]')
# block = self.wait_of_element_located('[class ="v-header-dropdown-item videoEditorPlus"]')
# block = self.wait_of_element_located('[class="v-header-dropdown-item slideshowMaker"]')
# block = self.wait_of_element_located('[class="v-header-dropdown-item videoSuiteBusiness"]')
# block = self.wait_of_element_located('[class="v-header-dropdown-item videoConverter"]')
# block = self.wait_of_element_located('[class="v-header-dropdown-item clips"]')
# block = self.wait_of_element_located('[class="v-header-dropdown-item effectsStore"]')
# block = self.wait_of_element_located('[class="v-header-dropdown-item stockVideo only-desktop"]')
# block = self.wait_of_element_located('[class="v-header-dropdown-item stockAudio only-desktop"]')
# block = self.wait_of_element_located('[class="v-header-dropdown-item stockPhotos only-desktop"]')


# # Сообщения ошибок
# ok_messages = {
#     site: "Мы на главной"
# }
#
# errors_messages = {
#     site: "Что то пошло не так"
# }
#
# ok_button = {
#     site: "Кнопка есть"
# }
#
# not_button = {
#     site: "Кнопки нет"
# }
#
# ok_bunner = {
#     site: "Баннер есть"
# }
#
# not_bunner = {
#     site: "Баннера нет"
# }
