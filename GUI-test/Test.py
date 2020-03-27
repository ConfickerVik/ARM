import time

# webdriver это и есть набор команд для управления браузером
import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from unittest import TestCase, main
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test(TestCase):

    # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
    self.driver = webdriver.Chrome()
    # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
    self.driver.get("http://62.109.3.107:8000")
    # Разворачиваем окно, нам ведь еще скрины делать
    self.driver.maximize_window()
    # Засыпаем, чтобы загрузилось
    # проверка что мы на нужной странице
    assert "АРМ" in self.driver.title
    # Ищем поле для ввода текста
    self.driver.find_element(By.NAME, "login").click()
    # пишим логин
    self.driver.find_element(By.NAME, "login").send_keys("dfhnj")
    self.driver.find_element(By.CSS_SELECTOR, ".form-horizontal").click()
    # пишим пароль
    self.driver.find_element(By.NAME, "pass").click()
    self.driver.find_element(By.NAME, "pass").send_keys("fdhjrnf")
    # нажатие на кнопку
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    # проверка
    wait = WebDriverWait(self.driver, 10)
    element = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".display-4"), "Курсы"))
    # добавление курса
    self.driver.find_element(By.ID, "buttonAddKurs").click()
    self.driver.find_element(By.NAME, "name_dis").click()
    self.driver.find_element(By.NAME, "name_dis").send_keys("Математика")
    self.driver.find_element(By.NAME, "group_name").click()
    self.driver.find_element(By.NAME, "group_name").send_keys("ИС")
    self.driver.find_element(By.NAME, "university").click()
    self.driver.find_element(By.NAME, "university").send_keys("ИрГУПС")
    self.driver.find_element(By.NAME, "year_education").click()
    self.driver.find_element(By.NAME, "year_education").send_keys("2020")
    self.driver.find_element(By.ID, "BtnAddCourse").click()
    time.sleep(3)
    # просмотр  курса
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .fa-eye").click()
    element = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".display-4"), "Программирование"))
    # добавление занятия
    self.driver.find_element(By.ID, "buttonAddKurs").click()
    self.driver.find_element(By.ID, "topicLesson").click()
    self.driver.find_element(By.ID, "topicLesson").send_keys("введение")
    self.driver.find_element(By.ID, "selectTypeLessons").click()
    dropdown = self.driver.find_element(By.ID, "selectTypeLessons")
    dropdown.find_element(By.XPATH, "//option[. = 'Лекция']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#selectTypeLessons > option:nth-child(2)").click()
    self.driver.find_element(By.ID, "BtnAddLesson").click()
    time.sleep(3)
    # журнал
    self.driver.find_element(By.CSS_SELECTOR, ".students > .nav-content").click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".display-4"), "Студенты"))
    self.driver.find_element(By.ID, "select_course").click()
    dropdown = self.driver.find_element(By.ID, "select_course")
    dropdown.find_element(By.XPATH, "//option[. = 'Программирование']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#select_course > option:nth-child(2)").click()
    self.driver.find_element(By.ID, "select_group").click()
    dropdown = self.driver.find_element(By.ID, "select_group")
    dropdown.find_element(By.XPATH, "//option[. = 'ПИ.1-16-1']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#select_group > option:nth-child(2)").click()
    self.driver.find_element(By.ID, "showStudentsMarks").click()
    time.sleep(3)

    self.driver.find_element(By.CSS_SELECTOR, ".finalMark > .nav-content").click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".display-4"), "Итоговая оценка"))
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .fa-check").click()
    self.driver.find_element(By.ID, "select_course").click()
    dropdown = self.driver.find_element(By.ID, "select_course")
    dropdown.find_element(By.XPATH, "//option[. = 'Программирование']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#select_course > option:nth-child(2)").click()
    self.driver.find_element(By.ID, "select_group").click()
    dropdown = self.driver.find_element(By.ID, "select_group")
    dropdown.find_element(By.XPATH, "//option[. = 'ПИ.1-16-1']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#select_group > option:nth-child(2)").click()
    self.driver.find_element(By.ID, "showFinalMarks").click()
    time.sleep(3)
    self.driver.quit()

if __name__ == '__main__':
    main()