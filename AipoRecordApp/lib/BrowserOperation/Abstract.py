from __future__ import annotations
from typing import Final as const
from abc import ABC, abstractmethod

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ChromeOptions
import chromedriver_binary

class AbsBrowserOperation(ABC):
    """Abstract class for browser operation."""

    def __init__(self) -> None:
        self.options: const[ChromeOptions] = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--no-sandbox')
        self.driver: const[WebDriver] = webdriver.Chrome()
        self.driver.get("""todo:ここにAipoのログインページのURLを入れる""")
        
    @abstractmethod
    def execute(self) -> list[IWorkTimeData]:
        """Execute the operation."""
        pass
    
    @abstractmethod
    def login(self) -> None:
        """Aipoへのアクセスとログインを行う."""
        pass
    
    @abstractmethod
    def move_to_timecard_page(self) -> None:
        """Timecardページへ移動する."""
        pass
    
    @abstractmethod
    def get_workdata_from_Dom(self) -> list[IWorkTimeData]:
        """DOMから勤務時間データを取得する."""
        pass
    
    @abstractmethod
    def logout(self) -> None:
        """Disconnect from Aipo."""
        pass
    
    
class IWorkTimeData:
    """_summary_
    勤務時間データを表すインターフェース
    """
    def __init__(self, date: str, wk_st_time: str, wk_en_time: str) -> None:
        """_summary_\n
        文字列情報から、勤務時間データを生成する。
        Args:
            date (str): 勤務日
            wk_st_time (str): 勤務開始時間
            wk_en_time (str): 勤務終了時間
        """
        self.date      : str = date
        self.start_time: str = wk_st_time
        self.end_time  : str = wk_en_time

class ILoginInfo:
    """_summary_
    ログイン情報を表すインターフェース
    """
    def __init__(self, id: str, pw: str) -> None:
        """_summary_\n
        文字列情報から、ログイン情報を生成する。
        Args:
            id (str): ログインID
            pw (str): ログインパスワード
        """
        self.id: str = id
        self.pw: str = pw