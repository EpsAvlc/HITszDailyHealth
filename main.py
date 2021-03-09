from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os
import json
import datetime
import time
import traceback
# import re

date_of_today = datetime.datetime.now()  # 当日日期
daily_report_url = 'http://xgsm.hitsz.edu.cn/zhxy-xgzs/xg_mobile/shsj/loginChange'
current_folder = os.path.split(os.path.realpath(__file__))[0]
req_url = "https://www.baidu.com"
chrome_options=Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=os.path.join(current_folder, "chromedriver"), chrome_options=chrome_options)

def login(user_id, password):
    """登录"""
    user_id_input = driver.find_element_by_id("username")
    password_input = driver.find_element_by_id("password")
    login_button = driver.find_element_by_class_name("login_box_landing_btn")

    user_id_input.send_keys(user_id)
    password_input.send_keys(password)
    login_button.click()

def wait_element_by_class_name(drv, class_name, timeout):
    """等待某个class出现"""
    WebDriverWait(drv, timeout).until(lambda d: d.find_element_by_class_name(class_name))

def wait_element_by_id(drv, id, timeout):
    """等待某个class出现"""
    WebDriverWait(drv, timeout).until(lambda d: d.find_element_by_id(id))

def check_todays_report():
    """检查当日是否填写过报告"""
    wait_element_by_class_name(driver, "content_title", 30)
    time.sleep(1)
    items = driver.find_elements_by_class_name("content_title")
    print ("发现%d条上报记录"%len(items))
    item_newest = items[1]
    year_str = item_newest.text[5:9]
    month_str = item_newest.text[10:12]
    day_str = item_newest.text[-2:]
    # print(item_newest.text)
    if int(year_str) == date_of_today.year and int(month_str) == date_of_today.month and int(day_str) == date_of_today.day:
        return True
    else:
        return False

def daily_report():
    wait_element_by_id(driver, "mrsb", 30)
    report_daily_button = driver.find_element_by_id("mrsb")
    report_daily_button.click()
    # today_has_reported = True
    today_has_reported = check_todays_report()
    if not today_has_reported:
        print("今日尚未上报")
        report_new_button = driver.find_element_by_class_name("right_btn")
        report_new_button.click()
    else:
        print("今日已上报，尝试修改并重新上报")
        button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]')
        button.click()

    time.sleep(1)
    report_check_box = driver.find_element_by_id("txfscheckbox")
    report_check_box.click()
    # time.sleep(1)
    buttons = driver.find_elements_by_class_name("right_btn")
    for bttn in buttons:
        if bttn.text == "提交":
            bttn.click()
            print("确认提交")
            break

def run(user_id, password):
    try:
        driver.get(daily_report_url)
        button_div = driver.find_element_by_class_name("login-box")
        button_logins = button_div.find_elements_by_tag_name("button")
        button_login = button_logins[0]
        button_login.click()
        login(user_id, password)
        print("登录成功")
        time.sleep(0.5)
        daily_report()
    except Exception:
        exception = traceback.format_exc()
        print(exception)
        print("遇到不可抗力而失败了...")
    finally:
        time.sleep(2)
        driver.quit()


if __name__ == '__main__':
    with open(os.path.join(current_folder, "config.json"), encoding='UTF-8') as config_file:
        j = json.load(config_file)
        user_id = j['user_id']
        password = j['password']
        run(user_id, password)