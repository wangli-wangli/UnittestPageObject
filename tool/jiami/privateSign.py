r"""
私钥签名
"""
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Sig_pk
from Crypto.PublicKey import RSA
import base64

def sign(name):
    """
    私钥签名
    :param name:待签名内容
    :return:签名后的内容
    """
    #获取私钥
    key=open('private.pem','r').read()
    rsakey=RSA.importKey(key)
    #根据sha算法处理签名内容（此处的hash算法不一定是sha,看开发）
    data=SHA.new(name.encode())
    #私钥进行签名
    sig_pk=Sig_pk.new(rsakey)
    sign=sig_pk.sign(data)
    #将签名后的内容，转换成base64编码
    result=base64.b64encode(sign)
    #签名结果转换成字符串
    data=result.decode()
    print(data)
    return data

def checkSign(name,data):
    """
    验签
    :param name: 签名之前的内容
    :param data: 签名之后的内容
    :return: 验证是否通过
    """
    #base64解码
    data=base64.b64decode(data)
    #获取公钥
    key=open('public.pem').read()
    rsakey=RSA.importKey(key)
    #将签名之前的内容进行hash处理
    sha_name=SHA.new(name.encode())
    #验证签名
    signer=Sig_pk.new(rsakey)
    result=signer.verify(sha_name,data)
    #验证通过返回True  不通过返回False
    print(result)

if __name__ == '__main__':
    name='mensun'
    data=sign(name)
    checkSign(name,data)