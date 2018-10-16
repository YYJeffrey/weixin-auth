import base64
import json
from Crypto.Cipher import AES
from configparser import ConfigParser

conf = ConfigParser()
path = os.path.split(os.path.realpath(__file__))[0] + '../config.ini'
conf.read(path)


class WXBizDataCrypt:
    def __init__(self, session_key):
        self.app_id = conf.get('wechat', 'app_id')
        self.session_key = session_key

    def decrypt(self, encrypted_data, iv):
        # base64 decode
        # noinspection PyBroadException
        try:
            session_key = base64.b64decode(self.session_key)
            encrypted_data = base64.b64decode(encrypted_data)
            iv = base64.b64decode(iv)

            cipher = AES.new(session_key, AES.MODE_CBC, iv)
            decrypted = json.loads(self._unpad(cipher.decrypt(encrypted_data)))
        except Exception:
            return None

        if decrypted['watermark']['appid'] != self.app_id:
            raise Exception('Invalid Buffer')
        return decrypted

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]
