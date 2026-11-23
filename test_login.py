from playwright.sync_api import Page, expect
import pathlib

# Берём адрес файла прямо с диска — никакой сети не нужно
URL = (pathlib.Path(__file__).parent / "login_page.html").as_uri()

def test_login_success(page: Page):
    page.goto(URL)
    page.locator("[data-test=\"email\"]").fill("customer@test.com")
    page.locator("[data-test=\"password\"]").fill("welcome01")
    page.click('[data-test="login-submit"]')
    # После успешного логина форма скрылась, появился заголовок "My account"
    expect(page.locator("[data-test=\"page-title\"]")).to_contain_text("My account")
    expect(page.locator('[data-test="error"]')).to_be_hidden()

def test_login_wrong_password(page: Page):
    page.goto(URL)
    page.fill('[data-test="email"]', "customer@test.com")
    page.fill('[data-test="password"]', "wrong_password")
    page.click('[data-test="login-submit"]')
    expect(page.locator('[data-test="error"]')).to_contain_text("Invalid email or password")