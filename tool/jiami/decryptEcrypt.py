r"""
分段加密和解密
如果数据长度超过了当前秘钥的所能处理最大长度，则需要进行分段加密。
分段加密：通俗易懂的讲就是把原来一长串的数据，分割成多段，每段的大小控制在秘钥的最大加密数量之内，加密完了之后再把数据进行拼接。
分段解密：经过分段加密的数据，在进行解密的时候我们也要将它进行分成多段，然后解密之后再进行拼接就能得到原来的数据内容。
"""
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
def cipher(msg):
    """
    公钥加密
    :param msg: 要加密内容
    :return: 加密之后的密文
    """
    #获取公钥
    key=open('public.pem').read()
    publickey=RSA.importKey(key)
    #分段加密
    pk=PKCS1_v1_5.new(publickey)
    encrypt_text=[]
    for i in range(0,len(msg),100):
        cont=msg[i:i+100]
        encrypt_text.append(pk.encrypt(cont.encode()))
    #加密完机型拼接
    cipher_text=b''.join(encrypt_text)
    #base64进行编码
    result=base64.b64encode(cipher_text)
    return result.decode()

def decrypt(msg):
    """
    私钥进行解密
    :param msg: 密文：字符串类型
    :return: 解密之后的内容
    """
    #base64解码
    msg=base64.b64decode(msg)
    #获取私钥
    privatekey=open('private.pem').read()
    rsakey=RSA.importKey(privatekey)
    cipher=PKCS1_v1_5.new(rsakey)
    #进行解密
    text=[]
    for i in range(0,len(msg),128):
        cont=msg[i:i+128]
        text.append(cipher.decrypt(cont,1))
    text=b''.join(text)
    return text.decode()

if __name__ == '__main__':
    msg=cipher('我要加密')
    msg2=decrypt(msg)
    print(msg2)
