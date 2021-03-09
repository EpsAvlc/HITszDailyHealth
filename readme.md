# 哈尔滨工业大学（深圳）疫情每日上报脚本

参照 [github repo](https://github.com/wangyz1997/seu_daily_report)编写，感谢作者。

> 免责声明：本脚本仅为个人为学习python之目的所编写，使用该脚本造成的一切后果均由使用者承担。
本人仍然提倡每日按时手动进行疫情上报与入校申请，配合学校进行好疫情防控。

## 使用方法
### 1. git clone 本仓库 
### 2. 下载WebDriver

ubuntu 下
```bash
sudo apt-get install chromium-browser
```

随后去[chrome-driver](https://chromedriver.chromium.org/downloads)下载对应的chromedriver到该文件夹下

### 3. 下载python依赖
pip3 install -r requrements.txt
### 4. 配置脚本&运行
将config-example.json文件修改为config.json，并填上自己信息门户的学号与密码
随后
``` python3
python main.py
```
### 5. 自动化

正在尝试以github action为依托的自动化
