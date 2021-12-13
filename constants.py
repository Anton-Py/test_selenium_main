# Настройки телебота
TOKEN = '1701745703:AAEMMJNaqoLBhdNvJxgt4NqZ-09DIDI2NRU'
ID_CHANNEL = 387545645

# Ссылка на сайт
SITE = "https://movavi.com"

# Проверка по селектору и что текст соответствует
MAIN_TEXT = "span.title"
TITLE_TXT = "Work with multimedia anywhere"

# Поиск баннера
BANNER_CONTENT = '[class="banner-title d-none d-xl-block"]'
BANNER_BUTTON = '[class="btn inverse"]'

# Текст баннера
TEXT_FOR_FIRST_BANNER = "Try Movavi Video Suite – an all-in-one video maker, perfect for remote work and distance learning."

# Словарь ссылк для проверки хедера
DICT_WINDOWS = {'store': '[href="/store/?asrc=main_menu"]',
                'support': '[href="/support/?asrc=main_menu"]',
                'how-to': '[href="/support/how-to/?asrc=main_menu"]',
                'blog': '[href="https://movavi.io/?asrc=main_menu"]',
                'v-header-account': '[href="https://movavi.id/?lng=en&asrc=main_menu"]'}

# Список для проверки ссылки после клика в хедере, что перешли на нужный URL
ASRT = ['https://www.movavi.com/store/?asrc=main_menu',
        'https://www.movavi.com/support/?asrc=main_menu',
        'https://www.movavi.com/support/how-to/?asrc=main_menu',
        'https://www.movavi.io/?asrc=main_menu',
        'https://movavi.id/login?lng=en&asrc=main_menu']

HEADER_SEARCH = '[class="v-header-search"]'
ENTRY_FIELD = 'div label input[placeholder="Search on movavi.com"]'
TEXT_SEARCH = "screen recorder"
SEARCH = '[class="v-header-link external"]'
PAGE_SORCE_ONE = "It's a lightweight and free streaming and game recording software for PCs that lets you capture and stream gameplay with one click."
PAGE_SORCE_TWO = "Check out the pricing options of Movavi Screen Recorder and choose the license type that suits your purpose. Buy the program and enjoy the benefits!"

# раскрыввем ui
<<<<<<< HEAD
# LOC_UI = '#app > header > nav > div > div.v-main-menu-sidebar > ul > li:nth-child(1) > a > span'
# список разделов из выпадающего списка
# LOC_UI = ['Video', 'Screen Recording', 'Photo', 'For Work', 'For Education']
LOC_UI = ['Photo', 'For Work', 'For Education']
# LOC_UI = ['For Work']


# нажимаем на продукт из ui
# UN = {"Unlimited", "Video Suite", "Video Editor Plus", "Slideshow Maker", "Video Suite Business", "Video Converter",
#       "Clips", "Effects Store", "Stock Video", "Stock Audio", "Stock Photos"}

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
=======
LOC_UI = '#app > header > nav > div > div.v-main-menu-sidebar > ul > li:nth-child(1) > a > span'

# нажимаем на продукт из ui
UN = {"Unlimited", "Video Suite", "Video Editor Plus", "Slideshow Maker", "Video Suite Business", "Video Converter", "Clips", "Effects Store", "Stock Video", "Stock Audio", "Stock Photos"}
DICT_UN = {'Unlimited': 'Unlimited',
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

DICT_HREF = {'Unlimited': 'https://www.movavi.com/suite-unlimited',
           'Video_Suite': 'https://www.movavi.com/video-suite-new',
           'Video_Editor_Plus': 'https://www.movavi.com/videoeditor',
           'Slideshow_Maker': 'https://www.movavi.com/slideshow-maker',
           'Video_Suite_Business': 'https://www.movavi.com/business-suite.html',
           'Video_Converter': 'https://www.movavi.com/movavi-video-converter',
           'Clips': 'https://www.movavi.com/android-video-editor',
           'Effects_Store': 'https://effects-store.movavi.com/',
           'Stock_Video': 'https://www.movavi.com/stock-video-footage',
           'Stock_Audio': 'https://www.movavi.com/stock-music',
           'Stock_Photos': 'https://www.movavi.com/stock-photos'}


>>>>>>> 8fc7f33e22c59855cc300988995020152e56c608

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
