import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_207_contains_btn_add_to_basket(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    button_add_to_basket = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button_add_to_basket, "Кнопка добавления в корзину отсутсвует"
    time.sleep(3)

