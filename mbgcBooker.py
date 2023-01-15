import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from datetime import date

def getDate():
    today = date.today()

    print("today", today)
    print("Today day: ", int(today.strftime("%d")) + 11)

    print("first day of month: ", (today.replace(day=1).isoweekday()))

if __name__ == "__main__":
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')

    # in main: wait until midnight then execute
    target_time = datetime.datetime(2022, 1, 24, 0)  # 12am on 23 Jan 2022

    while datetime.datetime.now() < target_time:
        time.sleep(1)

    # getDate()

    driver.get('https://booking.mbgc.com.sg/OnlineBooking/BookingDetails')

    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div/div/div/div/div/center/a').click()
    time.sleep(0.5)

    dateInputField = driver.find_element(By.ID, 'DisplayPlayDate')
    dateInputField.click()

    goNextMonthButton = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[2]')
    goNextMonthButton.click()

    targetDate = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[6]')
    targetDate.click()

    time.sleep(0.2)
    eighteenHoleOption = driver.find_element(By.XPATH, '//*[@id="AvailCourse"]/a[1]')
    eighteenHoleOption.click()

    # i am not a robot check
    # driver.switchTo().frame(driver.findElement(By.xpath, '//*[@id="ReCaptchContainer"]/div/div/iframe'))
    # driver.findElement(By.xpath("xpath_of_reCaptcha_checkbox")).click()