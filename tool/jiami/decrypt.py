r"""
私钥解密
"""
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

#密文
msg=b'eOSJCztpuxl6bFxg1Qh62zBh/kABFVy9MfuqjmN9OrQbgJMJIDiCdODNVeD6bJEbNcvNtAAy3rPjZqwVpEz2M/BlcXBALRxD3N+XIL5QXLqN0Fr8vBjZO/rCgeCaSVA17DiPSyrZ+r8yg485Qsg2T1pD2sz5dwRgTkcL3+YSGWo='

#base64解码
msg=base64.b64decode(msg)

#获取私钥
privatekey=open('private.pem').read()
rsakey=RSA.importKey(privatekey)
#进行解密
cipher=PKCS1_v1_5.new(rsakey)
text=cipher.decrypt(msg,'DecryptError')
#解密出来的是字节码格式，decode转换为字符串
print(text.decode())
