import allure
import time
from selenium import webdriver


@allure.title("Поиск Яндекс Маркет")
@allure.severity(severity_level='BLOCKER')
def test_search():
    driver = webdriver.Chrome()
    with allure.step("Открываем страницу https://ya.ru/"):
        driver.get('https://ya.ru/')
        time.sleep(2)
    with allure.step("Задаем в поиске: yandex маркет"):
        search_input = driver.find_element_by_xpath('//*[@id="text"]')
        search_btn = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/div[2]/button')
        search_input.send_keys('yandex маркет')
        search_btn.click()
        time.sleep(2)
    with allure.step("Переходим по первой ссылке результата поиска"):
        search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        link = search_results[0].find_element_by_tag_name("a")
        link.click()
        driver.switch_to.window(driver.window_handles[-1])
    with allure.step("Проверяем имя окна на содержание Яндекс.Маркет"):
        assert 'Яндекс.Маркет' in driver.title
    driver.close()
