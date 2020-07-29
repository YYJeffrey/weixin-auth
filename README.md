# weixin-auth
基于python封装微信小程序登录授权模块  
前端只需向服务器一次性传递`code, encrypted_data, iv`这三个参数即可获取openid

## 使用步骤
### 一、安装Python3
* 进入Python官网安装Python3 https://www.python.org/downloads/

### 二、安装cryptography
```
pip install cryptography`
```

### 三、调用方法
```Python
from wechat import wx_code_crypto, wx_data_crypto
def get_client_info(code, encrypted_data, iv):
    session_key = wx_code_crypto.check_code(code)
    if session_key is not None:
        client = wx_data_crypto.WXBizDataCrypt(session_key)
        return client.decrypt(encrypted_data, iv)
    return None
```
