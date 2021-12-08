# Настройки телебота
token = '1701745703:AAEMMJNaqoLBhdNvJxgt4NqZ-09DIDI2NRU'
id_channel = 387545645

# Ссылка на сайт
site = "https://movavi.com"

# Проверка по селектору и что текст соответствует
main_text = "span.title"
title_txt = "Work with multimedia anywhere"
# Поиск баннера
banner_content = '[class="banner-title d-none d-xl-block"]'
banner_button = '[class="btn inverse"]'

# Текст баннера
text_for_first_banner = "Try Movavi Video Suite – an all-in-one video maker, perfect for remote work and distance " \
                        "learning. "

# Словарь ссылк для проверки хедера
dict_windows = {'store': '[href="/store/?asrc=main_menu"]',
                'support': '[href="/support/?asrc=main_menu"]',
                'how-to': '[href="/support/how-to/?asrc=main_menu"]',
                'blog': '[href="https://movavi.io/?asrc=main_menu"]',
                'v-header-account': '[href="https://movavi.id/?lng=en&asrc=main_menu"]'}

# Список для проверки ссылки после клика в хедере, что перешли на нужный URL
asrt = ['https://www.movavi.com/store/?asrc=main_menu',
        'https://www.movavi.com/support/?asrc=main_menu',
        'https://www.movavi.com/support/how-to/?asrc=main_menu',
        'https://www.movavi.io/?asrc=main_menu',
        'https://movavi.id/login?lng=en&asrc=main_menu']

header_search = '[class="v-header-search"]'

entry_field = 'div label input[placeholder="Search on movavi.com"]'
text_search = "screen recorder"


search = '[class="v-header-link external"]'
# search = '[class="v-header-search-icon icon search-icon"]'

page_source_one = "It's a lightweight and free streaming and game recording software for PCs that lets you capture and stream gameplay with one click."
page_source_two = "Check out the pricing options of Movavi Screen Recorder and choose the license type that suits your purpose. Buy the program and enjoy the benefits!"

loc_ui = '#app > header > nav > div > div.v-main-menu-sidebar > ul > li:nth-child(1) > a > span'
# loc_ui = '#app > header > nav > div > div.v-main-menu-sidebar > ul > li:nth-child(1)'
# loc_ui = '#app > header > nav > div > div.v-main-menu-sidebar > ul > li:nth-child(1) > a > svg.icon.shevron-icon'


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
