from __future__ import annotations
from typing import Final as const
from selenium.webdriver.common.by import By

from Abstract import AbsBrowserOperation, IWorkTimeData, ILoginInfo
from constans import Dom
#todo: ログイン情報の暗号化
class BrowserOperation(AbsBrowserOperation):
    
    WAIT_TIME: const[int] = 10
    
    def __init__(self, login_info:ILoginInfo) -> None:
        super().__init__()
        self.login_info = login_info
        self.data: list[IWorkTimeData] = []
        
    def execute(self) -> list[IWorkTimeData]:

        self.login()
        self.driver.implicitly_wait(self.WAIT_TIME)
        self.move_to_timecard_page()
        self.driver.implicitly_wait(self.WAIT_TIME)
        self.data = self.get_workdata_from_Dom()
        self.logout()
        
        return self.data
    
    
    def login(self) -> None:
        user_name_input = self.driver.find_element(By.CSS_SELECTOR, Dom.USERNAME.value)
        user_name_input.send_keys(self.login_info.id)
        password_input = self.driver.find_element(By.CSS_SELECTOR, Dom.PASSWORD.value)
        password_input.send_keys(self.login_info.pw)
        execute_login_btn = self.driver.find_element(By.CSS_SELECTOR, Dom.LOGIN_BTN.value)
        execute_login_btn.click()