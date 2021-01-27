#登录页面
from poium import Page,NewPageElement,PageElements

class LoginPage(Page):

    server_button=NewPageElement(css=".anticon-setting > svg")
    server_selector=NewPageElement(xpath="//span[contains(.,'请选择服务器地址')]")
    testServer_option=NewPageElement(xpath="//div[4]/div")

    mobileLogin_button=NewPageElement(id_="rc-tabs-0-tab-mobile")
    mobile_input=PageElements(id_="data0",timeout=2)
    verificationCode_input=PageElements(id_="data0",timeout=2)
    login_button=NewPageElement(xpath="//button[@type='submit']")