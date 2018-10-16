# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 20:16
# @Author  : Jeffrey
from wechat import wx_code_crypto, wx_data_crypto


def get_client_info(code, encrypted_data, iv):
    session_key = wx_code_crypto.check_code(code)
    if session_key is not None:
        client = wx_data_crypto.WXBizDataCrypt(session_key)
        return client.decrypt(encrypted_data, iv)
    return None
