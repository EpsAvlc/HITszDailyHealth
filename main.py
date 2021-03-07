from selenium import webdriver
import os
import json

daily_report_url = 'http://xgsm.hitsz.edu.cn/zhxy-xgzs/xg_mobile/shsj/loginChange'
current_folder = os.path.split(os.path.realpath(__file__))[0]
driver = webdriver.Chrome(executable_path=os.path.join(current_folder, "chromedriver"))

def login(user_id, password):
    """登录"""
    user_id_input = driver.find_element_by_id("username")
    password_input = driver.find_element_by_id("password")
    login_button = driver.find_element_by_class_name("login_box_landing_btn")

    user_id_input.send_keys(user_id)
    password_input.send_keys(password)
    login_button.click()

def daily_report():
    report_daily_button = driver.find_element_by_id("mrsb")
    report_daily_button.click()
    report_new_button = driver.find_element_by_class_name("right_btn")
    report_new_button.click()
    pass

def run(user_id, password):
    try:
        driver.get(daily_report_url)
        button_div = driver.find_element_by_class_name("login-box")
        button_logins = button_div.find_elements_by_tag_name("button")
        button_login = button_logins[0]
        button_login.click()
        login(user_id, password)
        daily_report()
    except Exception:
        pass
    finally:
        time.sleep(3)
        driver.quit()


if __name__ == '__main__':
    with open(os.path.join(current_folder, "config.json"), encoding='UTF-8') as config_file:
        j = json.load(config_file)
        user_id = j['user_id']
        password = j['password']
        run(user_id, password)