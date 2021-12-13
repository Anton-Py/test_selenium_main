from PageObgect import MainPage
# from PageObgect_1 import MainPage

def test_guest_can_go_to(chrome):
    main_page = MainPage(chrome)
    main_page.go_to_site()
    main_page.test_main_page()
    main_page.site_search()
    main_page.main_ui()
