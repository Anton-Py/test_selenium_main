# Настройки телебота
# TOKEN = '1701745703:AAEMMJNaqoLBhdNvJxgt4NqZ-09DIDI2NRU'
# ID_CHANNEL = 387545645


class Locators:
    # ссылка на сайт
    SITE = "https://movavi.com"

    # проверка по селектору и что текст соответствует
    MAIN_TEXT = "span.title"
    TITLE_TXT = "Work with multimedia anywhere"

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
                    'v-header-account': '[href="https://movavi.id/?lng=en&asrc=main_menu"]'}

    # список для проверки ссылки после клика в хедере, что перешли на нужный URL
    ASRT = ['https://www.movavi.com/store/?asrc=main_menu',
            'https://www.movavi.com/support/?asrc=main_menu',
            'https://www.movavi.com/support/how-to/?asrc=main_menu',
            'https://www.movavi.io/?asrc=main_menu',
            'https://movavi.id/login?lng=en&asrc=main_menu']

    # список локаторов для поиска (открыть, ввести текст)
    HEADER_SEARCH = '[class="v-header-search"]'
    ENTRY_FIELD = 'div label input[placeholder="Search on movavi.com"]'
    TEXT_SEARCH = "screen recorder"
    SEARCH = '[class="v-header-link external"]'
    PAGE_SORCE_ONE = "Screen Recorder for Perfect Captures - Movavi"

    # список разделов из выпадающего списка
    LOC_UI = ['Video', 'Screen Recording', 'Photo', 'For Work', 'For Education']
    DICT_POSITION = {'Video': 1, 'Screen Recording': 2, 'Photo': 3, 'For Work': 4, 'For Education': 5}
    # DICT_COL_PRODUCT = {'Video': 7, 'Screen Recording': 4, 'Photo': 5, 'For Work': 9, 'For Education': 2}
    DICT_COL_PRODUCT = {'Video': 7, 'Screen Recording': 4, 'Photo': 5, 'For Work': 9, 'For Education': 2}

    # LOC_UI = ['Photo', 'For Work']
    # LOC_UI = ['For Work']
    LOC_UI_Video = ['Video']
    # LOC_UI = ['Photo']
    # LOC_UI = ['For Work']
    LOC_UI_For_Education = ['For Education']

    DICT_VIDEO = {'Unlimited': 'Unlimited',
                  'Video_Suite': 'Video Suite',
                  'Video_Editor_Plus': 'Video Editor Plus',
                  'Slideshow_Maker': 'Slideshow Maker',
                  'Video_Suite_Business': 'Video Suite Business',
                  'Video_Converter': 'Video Converter',
                  'Clips': 'Clips',
                  'Effects_Store': 'Effects Store',
                  'Stock_Video': 'Stock Video',
                  'Stock_Audio': 'Stock Audio',
                  'Stock_Photos': 'Stock Photos'}

    DICT_SCREEN_RECORDING = {'Unlimited': 'Unlimited',
                             'Video_Suite': 'Video Suite',
                             'Screen_Recorder': 'Screen Recorder',
                             'Gecata_by_Movavi': 'Gecata by Movavi',
                             'Effects_Store': 'Effects Store',
                             'Stock_Video': 'Stock Video',
                             'Stock_Audio': 'Stock Audio',
                             'Stock_Photos': 'Stock Photos'}

    DICT_PHOTO = {'Unlimited': 'Unlimited',
                  'Picverse': 'Picverse',
                  # 'Mobile': 'mobile ',
                  'Photo_Manager': 'Photo Manager',
                  'Slideshow_Maker': 'Slideshow Maker',
                  'Effects_Store': 'Effects Store',
                  'Stock_Audio': 'Stock Audio',
                  'Stock_Photos': 'Stock Photos'}

    DICT_FOR_WORK = {'Unlimited': 'Unlimited',
                     'Video_Suite_Business': 'Video Suite Business',
                     'Video_Editor_Plus': 'Video Editor Plus',
                     'Screen_Recorder': 'Screen Recorder',
                     'Video_Converter': 'Video Converter',
                     'Picverse': 'Picverse',
                     'PDFСhef_by_Movavi': 'PDFСhef by Movavi',
                     'Slideshow_Maker': 'Slideshow Maker',
                     'PDFChef_Scanner': 'PDFChef Scanner',
                     'Effects_Store': 'Effects Store'}

    DICT_FOR_EDUCATION = {'Students_and_Teachers': 'Students and Teachers',
                          'Schools_and_Universities': 'Schools and Universities'}

    DICT_HREF = {'Unlimited': 'https://www.movavi.com/suite-unlimited',
                 'Video_Suite': 'https://www.movavi.com/video-suite-new',
                 'Video_Editor_Plus': 'https://www.movavi.com/videoeditor',
                 'Slideshow_Maker': 'https://www.movavi.com/slideshow-maker',
                 'Video_Suite_Business': 'https://www.movavi.com/business-suite.html',
                 'Video_Converter': 'https://www.movavi.com/movavi-video-converter',
                 'Clips': 'https://www.movavi.com/android-video-editor',
                 'Effects_Store': 'https://effects-store.movavi.com',
                 'Stock_Video': 'https://www.movavi.com/stock-video-footage',
                 'Stock_Audio': 'https://www.movavi.com/stock-music',
                 'Stock_Photos': 'https://www.movavi.com/stock-photos',
                 'Screen_Recorder': 'https://www.movavi.com/screen-recorder',
                 'Gecata_by_Movavi': 'https://www.gecata.com/',
                 'Picverse': 'https://www.movavi.com/photo-editor',
                 # 'Mobile': 'https://www.movavi.com/mobile-photo-editor.html',
                 'Photo_Manager': 'https://www.movavi.com/photo-organizer',
                 'PDFСhef_by_Movavi': 'https://pdfchef.com/pdf-editor',
                 'PDFChef_Scanner': 'https://pdfchef.com/pdfchef-scanner.html',
                 'Students_and_Teachers': 'https://www.edu.movavi.com/',
                 'Schools_and_Universities': 'https://www.edu.movavi.com/academic-for-schools'}

    OSI = ["Windows", "MacOS"]

    OSI_UNLIMITED = ['[href="/suite-unlimited/?asrc=main_menu#main"]',
                     '[href="/suite-unlimited-mac/?asrc=main_menu#main"]']
    OSI_VIDEO_SUITE = ['[href="/video-suite-new/?asrc=main_menu#main"]', '[href="/suite-mac/?asrc=main_menu#main"]']
    OSI_VIDEOEDITOR = ['[href="/videoeditor/?asrc=main_menu"]', 'href="/video-editor-plus-mac/?asrc=main_menu"']
    OSI_SLIDESHOW_MARKER = ['[href="/slideshow-maker/?asrc=main_menu"]',
                            '[href="/slideshow-maker-for-mac/?asrc=main_menu"]']
    OSI_BUSINES_SUITE = ['[href="/business-suite.html?asrc=main_menu"]',
                         '[href="/business-suite-mac.html?asrc=main_menu"]']
    OSI_VIDEO_CONVERTER = ['[href="/movavi-video-converter/?asrc=main_menu"]',
                           '[href="/videoconvertermac/?asrc=main_menu"]']
    OSI_VIDEO_EDITOR = ['[href="/android-video-editor/?asrc=main_menu"]', '[href="/ios-video-editor/?asrc=main_menu"]']

    loc = ['class="list left-side"']

    element_located = ['[class ="v-header-dropdown-item unlimited"]',
                       '[class="v-header-dropdown-item videoSuite"]',
                       '[class ="v-header-dropdown-item videoEditorPlus"]'
                       # '[class="v-header-dropdown-item slideshowMaker"]',
                       # '[class="v-header-dropdown-item videoSuiteBusiness"]',
                       # '[class="v-header-dropdown-item videoConverter"]',
                       # '[class="v-header-dropdown-item clips"]',
                       # '[class="v-header-dropdown-item effectsStore"]',
                       # '[class="v-header-dropdown-item stockVideo only-desktop"]',
                       # '[class="v-header-dropdown-item stockAudio only-desktop"]',
                       # '[class="v-header-dropdown-item stockPhotos only-desktop"]'
                       ]

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


# DICT_VIDEO = {'Unlimited': ['Unlimited', '[href="/suite-unlimited/?asrc=main_menu#main"]', '[href="/suite-unlimited-mac/?asrc=main_menu#main"]'],
#               'Video_Suite': 'Video Suite',
#               'Video_Editor_Plus': 'Video Editor Plus',
#               'Slideshow_Maker': 'Slideshow Maker',
#               'Video_Suite_Business': 'Video Suite Business',
#               'Video_Converter': 'Video Converter',
#               'Clips': 'Clips',
#               'Effects_Store': 'Effects Store',
#               'Stock_Video': 'Stock Video',
#               'Stock_Audio': 'Stock Audio',
#               'Stock_Photos': 'Stock Photos'}


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
