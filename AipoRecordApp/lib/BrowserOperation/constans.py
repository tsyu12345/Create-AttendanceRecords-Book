from __future__ import annotations
from enum import Enum

class Dom(Enum):
    """_summary_\n
    必要なDOMのセレクタを定義する。
    """
    USERNAME = "#member_username"
    PASSWORD = "#password"
    LOGIN_BTN = "#auiLoginInner > form > div:nth-child(6) > div.floatRight > input"