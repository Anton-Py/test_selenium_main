from PageObgect import MainPage


def test_guest_can_go_to(chrome):
    main_page = MainPage(chrome)
    main_page.go_to_site()
    main_page.test_main_page()
    main_page.sait_search()