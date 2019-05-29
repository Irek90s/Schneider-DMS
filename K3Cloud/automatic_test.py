from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from after_mapping import parse_xml
from email.header import Header  # 用来设置邮件头和邮件主题
from email.mime.text import MIMEText 

import smtplib
import time
import sys

# 定义邮件发送方法
def send_mail(msg, mode="a", mail_title="K3Cloud进货订单报警"):
    #mail_title 邮件标题 msg 邮件内容 path 日志路径 mode 日志追加模式
    # 创建一个实例
    # sender = "K3Cloud_order_autoinput"
    sender = "jeffrey.liu@powere2e.com"
    receiver = "jeffrey.liu@powere2e.com"
    message = MIMEText(msg, 'plain','utf-8')  # 邮件正文
    message['From'] = sender  # 邮件上显示的发件人
    message['To'] = receiver  # 邮件上显示的收件人
    message['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题

    try:
        smtp = smtplib.SMTP()  # 创建一个连接
        smtp.connect("smtp.powere2e.com")  # 连接发送邮件的服务器
        smtp.login("jeffrey.liu@powere2e.com","jeffrey@0126")  # 登录服务器
        smtp.sendmail(sender, receiver, message.as_string())  # 填入邮件的相关信息并发送
        # log("邮件发送成功！！！",mode, path=maillog)
        smtp.quit()
    except smtplib.SMTPException:
        # log("邮件发送失败！！！",mode, path=maillog)
        print("**********")
        # pass

# 启动浏览器
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Chrome()
driver.implicitly_wait(20)
# 登录K3
driver.get("http://127.0.0.1/K3Cloud/html5")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath("//div[@id='ui-multiselect-btn-datacenter']/span[@class='ui-multiselect-label']").click()
time.sleep(1)
driver.find_element_by_xpath("//div[@id='ui-multiselect-menu-datacenter']/ul/li[2]").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@id='user']").send_keys("DEMO")
time.sleep(1)
driver.find_element_by_xpath("//input[@id='password']").send_keys("888888")
time.sleep(1)
driver.find_element_by_xpath("//span[@class='ui-button-text']").click()
try:
    time.sleep(3)
    driver.find_element_by_xpath("//div[@id='wholemessage']//button").click()
except Exception:
    pass
# 打开采购订单
time.sleep(5)
driver.find_element_by_xpath("//div[@class='CloudAllFunctionBtn']").click()
time.sleep(1)
driver.find_element_by_xpath("//span[@id='BOS_MainSystemMenu-FSYSTEMTREEVIEW_c_23_span']").click()
time.sleep(1)
open_stauts = driver.find_element_by_xpath("//button[@id='BOS_MainSystemMenu-FSYSTEMTREEVIEW_c_23_switch']")
if open_stauts.get_attribute("class") == "level1 switch noline_close":
    time.sleep(1)
    open_stauts.click()
xpath1 = "//span[@id='BOS_MainSystemMenu-FSYSTEMTREEVIEW_c_24_span']"
xpath2 = "//a[@title='CGDD 采购订单']"
time.sleep(1)
driver.find_element_by_xpath(xpath1).click()
time.sleep(1)
driver.find_element_by_xpath(xpath2).click()
time.sleep(5)
# 录入表头
def input_header(xxpath, input_data):
    time.sleep(1)
    driver.find_element_by_xpath(xxpath).send_keys(input_data)
    time.sleep(1)
    driver.find_element_by_xpath("//div[@class='ui-f7grid-itemContainer']//label").click()
    try:
        driver.find_element_by_xpath("//a[@class='ui-linkbutton enter2tab btn-gray btn'][1]").click()
        time.sleep(1)
    except Exception:
        pass
    time.sleep(1)
# 单据类型选择
time.sleep(1)
driver.find_element_by_xpath("//div[@class='ui-multiselect ui-widget ui-state-default ui-corner-all enter2tab']").click()
time.sleep(1)
driver.find_element_by_xpath("//div[@class='ui-multiselect-menu ui-widget ui-widget-content ui-corner-all ui-multiselect-single'][1]/ul/li[1]").click()
# 单据编号
time.sleep(1)
driver.find_element_by_xpath("//div[text()='单据编号']/..//input[1]").send_keys("GRN00000001")
# 采购组织选择
org_xpath = "//div[text()='采购组织']/..//div[@class='ui-f7-inputframe']/input[1]"
input_header(org_xpath, "101.1")
# 供应商选择
sup_xpath = "//div[text()='供应商']/..//div[@class='ui-f7-inputframe']/input[1]"
input_header(sup_xpath, "VEN00012")
# 采购部门选择
dpt_xpath = "//div[text()='采购部门']/..//div[@class='ui-f7-inputframe']/input[1]"
input_header(dpt_xpath, "BM000008")

def input_order(xpath, data):
    # 输入产品信息
    time.sleep(1)
    driver.find_element_by_xpath(xpath+"/td[6]").click()
    time.sleep(2)
    driver.find_element_by_xpath(xpath+"//input[@class='enter2tab ui-f7 ui-f7grid']").send_keys(data[7])
    try:
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='ui-f7grid-itemContainer']//label").click()
    except Exception:
        time.sleep(1)
        driver.find_element_by_xpath("//ul[@class='ui-toolbar-ul ui-ul-showmenu']/li/a/span[text()='删除行']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//ul[@class='ui-toolbar-ul ui-ul-showmenu']/li/a/span[text()='新增行']").click()
        time.sleep(3)
        return "error"
    time.sleep(1)
    # 输入数量
    while True:
        driver.find_element_by_xpath(xpath+"/td[14]").click()
        time.sleep(1)
        try:
            driver.find_element_by_xpath(xpath+"//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(data[1])
            time.sleep(1)
            break
        except Exception:
            continue
    # 输入最后交货日期
    while True:
        try:
            driver.find_element_by_xpath(xpath + "/td[18]").click()
            time.sleep(1)
            driver.find_element_by_xpath(xpath + "//input[@class='hasDatepicker enter2tab ui-datepicker-input']").send_keys(Keys.CONTROL, "a")
            time.sleep(1)
            driver.find_element_by_xpath(xpath + "//input[@class='hasDatepicker enter2tab ui-datepicker-input']").send_keys(Keys.DELETE)
            last_date = data[2][0:4]+"-"+data[2][4:6]+"-"+data[2][6:]
            time.sleep(1)
            driver.find_element_by_xpath(xpath + "//input[@class='hasDatepicker enter2tab ui-datepicker-input']").send_keys(last_date)
            time.sleep(1)
            driver.find_element_by_xpath(xpath + "//input[@class='hasDatepicker enter2tab ui-datepicker-input']").send_keys(Keys.ENTER)
            time.sleep(1)
            break
        except Exception:
            pass
    # 输入含税单价
    # price = float(data["KWERT"])/float(data["KWMENG"])
    while True:
        try:
            driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(str(data[6]))
            time.sleep(1)
            break
        except Exception:
             driver.find_element_by_xpath(xpath + "/td[20]").click()
             continue
    driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(Keys.ENTER)
    time.sleep(1)
    # 输入折扣率
    driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(str(int(data[4])*-1))
    time.sleep(1)
    driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(Keys.ENTER)
    time.sleep(1)
    # 输入税率
    driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(data[5])
    time.sleep(1)
    driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(Keys.ENTER)
    time.sleep(1)
    # 输入备注信息
    driver.find_element_by_xpath(xpath + "/td[32]").click()
    time.sleep(1)
    driver.find_element_by_xpath(xpath + "//textarea[@class='enter2tab ui-textarea']").send_keys("2002480010"+"|"+"113406")
    time.sleep(1)
    driver.find_element_by_xpath(xpath + "//textarea[@class='enter2tab ui-textarea']").send_keys(Keys.ENTER)
    time.sleep(1)
    # 输入供应商物料编码
    driver.find_element_by_xpath(xpath + "/td[33]").click()
    time.sleep(1)
    driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-text']").send_keys(data[0])
    time.sleep(1)
    # 新增行
    driver.find_element_by_xpath("//ul[@class='ui-toolbar-ul ui-ul-showmenu']/li/a/span[text()='新增行']").click()
    time.sleep(1)
# 录入数据
data = parse_xml("E:\\Project\\K3Cloud\\2002480010_AfterMapping.xml", "E:\\Project\\K3Cloud\\mapping.txt")
index = 0
for i in data:
    # print(data.index(i))
    # print("//tr[@id={}]".format(data.index(i)))
    ret = input_order("//tr[@id={}]".format(index), i)
    index = index + 1
    if ret == "error":
        send_mail("ERP中无编号为{}的产品".format(i[0]).encode("utf-8"))
        # 退出采购订单页面
        time.sleep(3)
        driver.find_element_by_xpath("//ul[@class='ui-toolbar-ul ui-ul-showmenu']//span[text()='退出']").click()
        # 不保存订单
        time.sleep(1)
        driver.find_element_by_xpath("//span[text()='否']").click()
        # 退出K3
        time.sleep(5)
        driver.find_element_by_xpath("//span[text()='退出']").click()
        # 退出浏览器
        time.sleep(5)
        driver.quit()
        # 退出程序
        sys.exit(1)
# 保存采购订单
time.sleep(5)
driver.find_element_by_xpath("//ul[@class='ui-toolbar-ul ui-ul-showmenu']//span[text()='保存']").click()
# 退出采购订单页面
time.sleep(10)
driver.find_element_by_xpath("//ul[@class='ui-toolbar-ul ui-ul-showmenu']//span[text()='退出']").click()
# 退出K3
time.sleep(5)
driver.find_element_by_xpath("//span[text()='退出']").click()
# 退出浏览器
time.sleep(5)
driver.quit()