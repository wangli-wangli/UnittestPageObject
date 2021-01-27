#首页
from poium import Page,NewPageElement,PageElements

class FirstPage(Page):
    #企业入驻认证按钮
    addEnterprise_button = NewPageElement(xpath='//*[@id="root"]/div[1]/section/aside/div/div[1]/ul/li[2]/a')
