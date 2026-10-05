from pages.search_page import SearchPage


def test_search_returns_relevant_products(driver):

    driver.get("https://demo.nopcommerce.com/")

    search_page = SearchPage(driver)

    search_term = "computer"

    search_page.search_product(search_term)

    products = search_page.get_product_titles()

    assert len(products) > 0

    for product in products:
        assert search_term.lower() in product.lower()