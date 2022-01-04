# from PageObgect import MainPage
# from PageObgect_1 import MainPage
from lib.training import MainPage


def test_guest_can_go_to(chrome):
    main_page = MainPage(chrome)
    main_page.go_to_site()
    # main_page.test_links_header_other_than_search()
    # main_page.test_site_search()
    main_page.test_all_links_dropdown_menu()

    # modules = dir()
    #
    # print(modules)
