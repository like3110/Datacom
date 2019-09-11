# -*-coding:utf-8-*-
# @Time    : 2019/6/12 15:39
# @Author  : IWC
# @Param   : 加密&解密
# @File    : PasswdUtil.py

import base64
import os
from Crypto import Random
from Crypto.Cipher import AES


# 加密函数
def encrypt(in_password):
    bs = AES.block_size
    pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    paddPassword = pad(in_password)
    iv = Random.OSRNG.new().read(bs)
    key = os.urandom(32)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    out_password = base64.b64encode(iv + cipher.encrypt(paddPassword) + key)
    return out_password


# 解密函数
def decrypt(in_password):
    base64Decoded = base64.b64decode(in_password)
    bs = AES.block_size
    unpad = lambda s: s[0:-s[-1]]
    iv = base64Decoded[:bs]
    key = base64Decoded[-32:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    out_password = unpad(cipher.decrypt(base64Decoded[:-32]))[bs:]
    return out_password
