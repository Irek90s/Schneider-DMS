from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from parse_xml import parse_xml
from after_mapping import parse_xml
import time

class AutomaticInput(object):
    def __init__(self, data):
        self.login_url = "http://127.0.0.1/K3Cloud/html5"
        # 加启动配置
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')

        self.driver = webdriver.Chrome(options=option)
        # self.driver = webdriver.Chrome()
        self.data = data

    def find_order(self, xpath1, xpath2):
        self.driver.find_element_by_xpath("//div[@class='CloudAllFunctionBtn']").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("//span[@id='BOS_MainSystemMenu-FSYSTEMTREEVIEW_c_23_span']").click()
        time.sleep(2)
        open_stauts = self.driver.find_element_by_xpath(
            "//button[@id='BOS_MainSystemMenu-FSYSTEMTREEVIEW_c_23_switch']")
        if open_stauts.get_attribute("class") == "level1 switch noline_close":
            open_stauts.click()
        time.sleep(2)
        self.driver.find_element_by_xpath(xpath1).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(xpath2).click()

    def input_header(self, xpath, input_data):
        self.driver.find_element_by_xpath(xpath).send_keys(input_data)
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='ui-f7grid-itemContainer']//label").click()
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//a[@class='ui-linkbutton enter2tab btn-gray btn'][1]").click()
        except Exception:
            pass

    def input_order(self, xpath, data):
        # 输入产品信息
        self.driver.find_element_by_xpath(xpath+"/td[6]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(xpath+"//input[@class='enter2tab ui-f7 ui-f7grid']").send_keys(data[7])
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//div[@class='ui-f7grid-itemContainer']//label").click()
        except Exception:
            self.driver.find_element_by_xpath("//ul[@class='ui-toolbar-ul ui-ul-showmenu']/li/a/span[text()='删除行']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//ul[@class='ui-toolbar-ul ui-ul-showmenu']/li/a/span[text()='新增行']").click()
            time.sleep(1)
            return "error"
        time.sleep(2)
        # 输入采购单位
        # self.driver.find_element_by_xpath(xpath+"/td[13]").click()
        # time.sleep(2)
        # # time.sleep(2)
        # # # pur_unit.clear()
        # # pur_unit.click()
        # self.driver.find_element_by_xpath(xpath+"//input[@class='enter2tab ui-f7 ui-f7grid']").send_keys(Keys.CONTROL, "a")
        # time.sleep(1)
        # self.driver.find_element_by_xpath(xpath+"//input[@class='enter2tab ui-f7 ui-f7grid']").send_keys(Keys.DELETE)
        # time.sleep(1)
        # self.driver.find_element_by_xpath(xpath+"//input[@class='enter2tab ui-f7 ui-f7grid']").send_keys("Pcs")
        # time.sleep(2)
        # # try:
        # self.driver.find_element_by_xpath("//div[@class='ui-f7grid-itemContainer']//label").click()
        # time.sleep(2)
        # 输入数量
        self.driver.find_element_by_xpath(xpath+"/td[14]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(xpath+"//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(data[1])
        time.sleep(2)
        # 输入最后交货日期
        self.driver.find_element_by_xpath(xpath + "/td[18]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(xpath + "//input[@class='hasDatepicker enter2tab ui-datepicker-input']").send_keys(Keys.CONTROL, "a")
        time.sleep(2)
        self.driver.find_element_by_xpath(xpath + "//input[@class='hasDatepicker enter2tab ui-datepicker-input']").send_keys(Keys.DELETE)
        time.sleep(1)
        last_date = data[2][0:4]+"-"+data[2][4:6]+"-"+data[2][6:]
        time.sleep(1)
        # last_date_element = self.driver.find_element_by_xpath(xpath + "//input[@class='hasDatepicker enter2tab ui-datepicker-input']")
        # time.sleep(1)
        # last_date_element.click()
        # time.sleep(2)
        self.driver.find_element_by_xpath(xpath + "//input[@class='hasDatepicker enter2tab ui-datepicker-input']").send_keys(last_date)
        # time.sleep(1)
        # last_date_element = self.driver.find_element_by_xpath(xpath + "//input[@class='hasDatepicker enter2tab ui-datepicker-input']")
        # time.sleep(1)
        # last_date_element.click()
        time.sleep(1)
        self.driver.find_element_by_xpath(xpath + "//input[@class='hasDatepicker enter2tab ui-datepicker-input']").send_keys(Keys.ENTER)
        # time.sleep(1)
        # self.driver.find_element_by_xpath(xpath + "/td[18]").click()
        # time.sleep(2)
        # 输入含税单价
        # self.driver.find_element_by_xpath(xpath + "/td[20]").click()
        # print(price)
        time.sleep(2)
        self.driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(str(data[6]))
        time.sleep(2)
        self.driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(Keys.ENTER)
        time.sleep(2)
        # 输入折扣率
        self.driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(str(int(data[4])*-1))
        time.sleep(2)
        self.driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(Keys.ENTER)
        time.sleep(2)
        # 输入税率
        self.driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(data[5])
        time.sleep(2)
        self.driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-numberfield ui-widget']").send_keys(Keys.ENTER)
        time.sleep(2)
        # 输入备注信息
        self.driver.find_element_by_xpath(xpath + "/td[32]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(xpath + "//textarea[@class='enter2tab ui-textarea']").send_keys("2002480010"+"|"+"113406")
        time.sleep(2)
        self.driver.find_element_by_xpath(xpath + "//textarea[@class='enter2tab ui-textarea']").send_keys(Keys.ENTER)
        time.sleep(2)
        # 输入供应商物料编码
        self.driver.find_element_by_xpath(xpath + "/td[33]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(xpath + "//input[@class='enter2tab ui-text']").send_keys(data[0])
        time.sleep(2)
        # 新增行
        self.driver.find_element_by_xpath("//ul[@class='ui-toolbar-ul ui-ul-showmenu']/li/a/span[text()='新增行']").click()
        time.sleep(2)

    def login(self):
        self.driver.get(self.login_url)
        # self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@id='ui-multiselect-btn-datacenter']/span[@class='ui-multiselect-label']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='ui-multiselect-menu-datacenter']/ul/li[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='user']").send_keys("DEMO")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys("888888")
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[@class='ui-button-text']").click()
        time.sleep(5)
        try:
            self.driver.find_element_by_xpath("//div[@id='wholemessage']//button").click()
        except Exception:
            pass
        time.sleep(20)

    def save_order(self):
        """保存退出"""
        self.driver.find_element_by_xpath("//ul[@class='ui-toolbar-ul ui-ul-showmenu']//span[text()='保存']").click()
        time.sleep(15)
        self.driver.find_element_by_xpath("//ul[@class='ui-toolbar-ul ui-ul-showmenu']//span[text()='退出']").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("//span[text()='退出']").click()
        time.sleep(5)
        self.driver.quit()
        time.sleep(5)

    def grn_order_input(self):
        pur_xpath = "//span[@id='BOS_MainSystemMenu-FSYSTEMTREEVIEW_c_24_span']"
        pur_order_xpath = "//a[@title='CGDD 采购订单']"
        self.find_order(pur_xpath, pur_order_xpath)
        time.sleep(10)

        # 单据类型选择
        self.driver.find_element_by_xpath("//div[@class='ui-multiselect ui-widget ui-state-default ui-corner-all enter2tab']").click()
        # ActionChains(self.driver).move_to_element(danju_select).perform()
        # danju_select.click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='ui-multiselect-menu ui-widget ui-widget-content ui-corner-all ui-multiselect-single'][1]/ul/li[1]").click()
        time.sleep(1)
        # 单据编号
        self.driver.find_element_by_xpath("//div[text()='单据编号']/..//input[1]").send_keys("GRN00000001")
        time.sleep(1)
        # 采购组织选择
        org_xpath = "//div[text()='采购组织']/..//div[@class='ui-f7-inputframe']/input[1]"
        self.input_header(org_xpath, "101.1")
        time.sleep(1)
        # 供应商选择
        sup_xpath = "//div[text()='供应商']/..//div[@class='ui-f7-inputframe']/input[1]"
        self.input_header(sup_xpath, "VEN00012")
        time.sleep(1)
        dpt_xpath = "//div[text()='采购部门']/..//div[@class='ui-f7-inputframe']/input[1]"
        self.input_header(dpt_xpath, "BM000008")
        time.sleep(1)
        # 订单数据录入
        self.input_order("//tr[@id='0']",self.data[0])
        index = 1
        for i in self.data[1:]:
            ret = self.input_order("//tr[@id='0']/following-sibling::tr[{}]".format(index), i)
            if ret == "error":
                index = index
            else:
                index = index + 1

            # if self.data.index(i)+1 >= 13:
            #     break
        # 保存订单
        self.save_order()

    def run(self):
        self.driver.maximize_window()
        time.sleep(5)
        # 登录
        self.login()
        # 进货订单录入
        self.grn_order_input()
        # tuichu
        # self.driver.quit()



if __name__ == '__main__':
    data = parse_xml("E:\\Project\\K3Cloud\\2002480010_AfterMapping.xml", "E:\\Project\\K3Cloud\\mapping.txt")

    auto_input = AutomaticInput(data)
    auto_input.run()