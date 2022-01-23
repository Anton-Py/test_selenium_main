# from PageObg import MainPage
# from PageObg_1 import MainPage
from lib.page import MainPage


def test_guest_can_go_to(chrome):
    main_page = MainPage(chrome)
    main_page.go_to_site()
    # main_page.test_links_header_other_than_search()
    # main_page.test_site_search()
    # main_page.test_all_links_dropdown_menu()
    # main_page.test_scroll_main_page()

    # modules = dir()
    #
    # print(modules)

# pytest tests/_test_main_page.py --disable-warnings --tb=short -s -v

# Проверить наличие чилда у мэйн Console
# document.querySelector('main').children.length
# document.querySelector('.main').children.length
