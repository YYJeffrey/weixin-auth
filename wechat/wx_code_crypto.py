# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 19:37
# @Author  : Jeffrey
import requests
from configparser import ConfigParser

conf = ConfigParser()
path = os.path.split(os.path.realpath(__file__))[0] + '../config.ini'
conf.read(path)


def check_code(code):
    app_id = conf.get('wechat', 'app_id')
    app_secret = conf.get('wechat', 'app_secret')
    # noinspection PyBroadException
    try:
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid={app_id}&secret={app_secret}&js_code={code}&' \
              'grant_type=authorization_code'.format(app_id=app_id, app_secret=app_secret, code=code)
        rs = requests.get(url).text
        data = eval(rs)
        if 'openid' in data and 'session_key' in data:
            return data['session_key']
        return None
    except Exception:
        return None
