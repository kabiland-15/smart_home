from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def login(username, password, room_name):
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys(username)
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)
    room_field = driver.find_element(By.NAME, "room_id")
    room_field.send_keys(room_name)
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()


def write_and_click():
    textarea = driver.find_element(By.ID, "msg")
    textarea.clear()
    textarea.send_keys("I AM HERE")
    submit_button = driver.find_element(By.CLASS_NAME, "submit")
    submit_button.click()

if __name__ == '__main__':
    service = Service('D:/projects/chromedriver.exe')
    service.start()
    driver = webdriver.Chrome(service=service)
    driver.get("https:/krishna1111.pythonanywhere.com/")

    login("sachin333", "sachin123", "smarthome")
    time.sleep(5)

    while True:
        write_and_click()
        time.sleep(3)
