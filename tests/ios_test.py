from ios_pages.gorest_login_page import GorestLoginPage
from ios_pages.gorest_base64_page import GorestBase64Page
from ios_pages.gorest_url_encode_page import GorestUrlEncodePage


def test_user_can_open_login_page(gorest_safari):
    gorest = GorestLoginPage(gorest_safari)
    gorest.open_burger_menu()
    gorest.click_on_login_menu_item()
    actual_login_links = gorest.get_links_from_login_buttons()
    expected_login_links = ["/oauth/github", "/oauth/facebook", "/oauth/microsoft"]
    assert actual_login_links == expected_login_links


def test_base64_encode_tool(gorest_safari):
    page = GorestBase64Page(gorest_safari)
    page.open_burger_menu()
    page.click_on_tools_menu_item()
    page.click_on_base64_menu_item()
    page.enter_text_into_base64_input("text_to_check base64")
    page.click_on_encode_button()
    assert page.check_base64_result("dGV4dF90b19jaGVjayBiYXNlNjQ=")


def test_url_decode(gorest_safari):
    page = GorestUrlEncodePage(gorest_safari)
    page.open_burger_menu()
    page.click_on_tools_menu_item()
    page.click_on_url_encode_menu_item()
    url_to_decode = (
        "%7C%7C%7CM%20O%20N%20E%20S%20E%20i%20s%20c%20o%20o%20l%20a%20n%20d"
        "%20n%20i%20c%20e%20p%20l%20a%20c%20e%20t%20o%20w%20o%20r%20k%20.%21%25"
    )
    page.enter_text_into_input(url_to_decode)
    page.click_on_decode_button()
    assert page.check_url_result(
        "|||M O N E S E i s c o o l a n d n i c e p l a c e t o w o r k .!%"
    )
