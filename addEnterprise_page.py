"""
企业入驻认证页面
"""
from poium import Page,NewPageElement,PageElements

class EntPage(Page):
    # 企业认证按钮
    button1 = NewPageElement(xpath='//*[@id="root"]/div[1]/section/section/main/div/div/div/div[1]/div/div[2]/button')

    entName_input = NewPageElement(id_='entName')
    uniscid_input = NewPageElement(id_='uniscid')
    # 选择主要经营模式
    busiModel_input = NewPageElement(id_='busiModel')
    # 选择独立经营
    busiModel_option = NewPageElement(xpath='/html/body/div[10]/div/div/div/div[2]/div[1]/div/div/div[1]/div')

    industry_input = NewPageElement(id_='industry')
    principal_input = NewPageElement(id_='mobile')
    address_input = NewPageElement(id_='address')
    address_input = NewPageElement(xpath='/html/body/div[7]/div/div/div/ul[2]/li')

