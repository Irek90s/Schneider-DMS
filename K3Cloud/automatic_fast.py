from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from after_mapping import parse_xml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

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
time.sleep(3)
driver.find_element_by_xpath("//div[@id='ui-multiselect-btn-datacenter']/span[@class='ui-multiselect-label']").click()
driver.find_element_by_xpath("//div[@id='ui-multiselect-menu-datacenter']/ul/li[2]").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@id='user']").send_keys("DEMO")
driver.find_element_by_xpath("//input[@id='password']").send_keys("888888")
driver.find_element_by_xpath("//span[@class='ui-button-text']").click()
try:
    time.sleep(3)
    driver.find_element_by_xpath("//div[@id='wholemessage']//button").click()
except Exception:
    pass
# 打开采购订单
# time.sleep(10)
try:
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='CloudAllFunctionBtn']")))
except Exception:
    driver.quit()
    sys.exit(1)
else:
    driver.find_element_by_xpath("//div[@class='CloudAllFunctionBtn']").click()
# print("*"*50)  
i = 0
while True:
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@id='BOS_MainSystemMenu-FSYSTEMTREEVIEW_c_23_span']")))
    except Exception:
        driver.refresh()
        driver.find_element_by_xpath("//div[@class='CloudAllFunctionBtn']").click()
    else:
        driver.find_element_by_xpath("//span[@id='BOS_MainSystemMenu-FSYSTEMTREEVIEW_c_23_span']").click()
        break
    i = i + 1
    if i == 5:
        driver.quit()
        sys.exit(1)

open_stauts = driver.find_element_by_xpath("//button[@id='BOS_MainSystemMenu-FSYSTEMTREEVIEW_c_23_switch']")
if open_stauts.get_attribute("class") == "level1 switch noline_close":
    time.sleep(1)
    open_stauts.click()
xpath1 = "//span[@id='BOS_MainSystemMenu-FSYSTEMTREEVIEW_c_24_span']"
xpath2 = "//a[@title='CGDD 采购订单']"
driver.find_element_by_xpath(xpath1).click()
driver.find_element_by_xpath(xpath2).click()
# 录入表头
def input_header(xxpath, input_data):
    driver.find_element_by_xpath(xxpath).send_keys(input_data)
    driver.find_element_by_xpath("//div[@class='ui-f7grid-itemContainer']//label").click()
    try:
        driver.find_element_by_xpath("//a[@class='ui-linkbutton enter2tab btn-gray btn'][1]").click()
        time.sleep(1)
    except Exception:
        pass
    time.sleep(1)
# 单据类型选择
driver.find_element_by_xpath("//div[@class='ui-multiselect ui-widget ui-state-default ui-corner-all enter2tab']").click()
driver.find_element_by_xpath("//div[@class='ui-multiselect-menu ui-widget ui-widget-content ui-corner-all ui-multiselect-single'][1]/ul/li[1]").click()
# 单据编号
driver.find_element_by_xpath("//div[text()='单据编号']/..//input[1]").send_keys("GRN00000001")
# 采购组织选择
org_xpath = "//div[text()='采购组织']/..//div[@class='ui-f7-inputframe']/input[1]"
input_header(org_xpath, "101.1")
# 供应商选择
sup_xpath = "//div[text()='供应商']/..//div[@class='ui-f7-inputframe']/input[1]"
input_header(sup_xpath, "VEN00012")
# 采购部门选择
# dpt_xpath = "//div[text()='采购部门']/..//div[@class='ui-f7-inputframe']/input[1]"
# input_header(dpt_xpath, "BM000008")

def input_order(xpath, data):
    # 输入产品信息
    driver.find_element_by_xpath(xpath+"/td[6]").click()
    driver.find_element_by_xpath(xpath+"//input[@class='enter2tab ui-f7 ui-f7grid']").send_keys(data[7])
    try:
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='ui-f7grid-itemContainer']//label").click()
    except Exception:
        driver.find_element_by_xpath("//ul[@class='ui-toolbar-ul ui-ul-showmenu']/li/a/span[text()='删除行']").click()
        driver.find_element_by_xpath("//ul[@class='ui-toolbar-ul ui-ul-showmenu']/li/a/span[text()='新增行']").click()
        return "error"
    # 输入采购单位
    # driver.find_element_by_xpath(xpath+"/td[13]").click()
    # time.sleep(1)
    # driver.find_element_by_xpath(xpath+"//input[@class='enter2tab ui-f7 ui-f7grid']").send_keys(Keys.CONTROL, "a")
    # time.sleep(1)
    # driver.find_element_by_xpath(xpath+"//input[@class='enter2tab ui-f7 ui-f7grid']").send_keys(Keys.DELETE)
    # time.sleep(1)
    # driver.find_element_by_xpath(xpath+"//input[@class='enter2tab ui-f7 ui-f7grid']").send_keys("Pcs")
    # time.sleep(1)
    # driver.find_element_by_xpath("//div[@class='ui-f7grid-itemContainer']//label").click()
    # time.sleep(1)
    # 输入数量
    driver.find_element_by_xpath(xpath+"/td[14]").click()
    try:
        driver.find_element_by_xpath(xpath+"//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(data[1])
    except Exception:
        driver.find_element_by_xpath(xpath+"/td[14]").click()
        driver.find_element_by_xpath(xpath+"//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(data[1])
    # 输入最后交货日期
    driver.find_element_by_xpath(xpath + "/td[18]").click()
    driver.find_element_by_xpath(xpath + "//input[@class='hasDatepicker enter2tab ui-datepicker-input']").send_keys(Keys.CONTROL, "a")
    driver.find_element_by_xpath(xpath + "//input[@class='hasDatepicker enter2tab ui-datepicker-input']").send_keys(Keys.DELETE)
    last_date = data[2][0:4]+"-"+data[2][4:6]+"-"+data[2][6:]
    driver.find_element_by_xpath(xpath + "//input[@class='hasDatepicker enter2tab ui-datepicker-input']").send_keys(last_date)
    driver.find_element_by_xpath(xpath + "//input[@class='hasDatepicker enter2tab ui-datepicker-input']").send_keys(Keys.ENTER)
    # 输入含税单价
    # price = float(data["KWERT"])/float(data["KWMENG"])
    driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(str(data[6]))
    driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(Keys.ENTER)
    # 输入折扣率
    driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(str(int(data[4])*-1))
    driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(Keys.ENTER)
    # 输入税率
    driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(data[5])
    driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(Keys.ENTER)
    # 输入备注信息
    driver.find_element_by_xpath(xpath + "/td[32]").click()
    driver.find_element_by_xpath(xpath + "//textarea[@class='enter2tab ui-textarea']").send_keys("2002480010"+"|"+"113406")
    driver.find_element_by_xpath(xpath + "//textarea[@class='enter2tab ui-textarea']").send_keys(Keys.ENTER)
    # 输入供应商物料编码
    driver.find_element_by_xpath(xpath + "/td[33]").click()
    driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-text']").send_keys(data[0])
    # 新增行
    driver.find_element_by_xpath("//ul[@class='ui-toolbar-ul ui-ul-showmenu']/li/a/span[text()='新增行']").click()
# 录入第一行数据
data = parse_xml("E:\\Project\\K3Cloud\\2002480010_AfterMapping.xml", "E:\\Project\\K3Cloud\\mapping.txt")
input_order("//tr[@id='0']",data[0])
# 循环录入后面的数据
index = 1
for i in data[1:]:
    ret = input_order("//tr[@id='0']/following-sibling::tr[{}]".format(index), i)
    if ret == "error":
        index = index
    else:
        index = index + 1

# 保存采购订单
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