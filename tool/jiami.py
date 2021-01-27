import base64
from urllib.parse import quote,unquote
import hashlib

def base64_test():
    """
    base64加密，解密
    特征是尾部经常带有= 号
    :return:
    """
    byte_str = "I like you".encode('utf-8')
    encode_str=base64.b64encode(byte_str)
    print(encode_str)

    #解码
    decode_str=base64.b64decode(encode_str)
    print(decode_str.decode("utf-8"))

def urlencode_test():
    """
    URL 编码,特征是 % 很多
    :return:
    """
    q='菜鸟'
    url='http://www.baidu.com/?text={}'.format(quote(q))

    #解码
    b=unquote('%E8%8F%9C%E9%B8%9F')

def md5_test():
    """
md5 不是编码，也不是加密，它叫做摘要算法，又称哈希算法和散列算法。 他的主要作用是：

防止篡改

校验数据

比如你下载了一个软件，会担心这个软件被人修改，植入了病毒。软件开发者为了防止自己的软件被别人修改，会在官网附带一个摘要信息。
    摘要算法是不可逆的，
    :return:
    """
    hash=hashlib.md5()
    hash.update(b'hello you')
    hash_str=hash.hexdigest()

def salt_test():
    """
    网站开发者会提供一个类似于秘钥的东西，我们称为 salt, 其实就是一个随便起的字符串。然后将原始密码 + salt 得到一个新字符串，再对他进行 hash。
    :return:
    """
    salt='the salt'
    pwd='8888'
    salt_pwd=pwd+salt

    hash=hashlib.md5()
    hash.update(salt_pwd.encode('utf-8'))
    hash_str=hash.hexdigest()
