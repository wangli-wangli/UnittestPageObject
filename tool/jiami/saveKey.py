r"""
Python实现RSA加解密和签名加解签
python上面的名字是pycrypto它是一个第三方库，但是已经停止更新三年了，所以不建议安装这个库；
pip install pycryptodome
C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Lib\site-packages
找到这个路径，下面有一个文件夹叫做crypto,将c改成C
r"""
from Crypto import Random
from Crypto.PublicKey import RSA

# 伪随机数生成器
random_gen = Random.new().read

# 生成密钥对实例对象：1024是密钥的长度
rsa = RSA.generate(1024, random_gen)
# 获取私钥，保存到文件
private_pem = rsa.exportKey()
with open('private.pem', 'wb') as f:
    f.write(private_pem)

# 获取公钥保存到文件
public_pem = rsa.publickey().export_key()
with open('public.pem', 'wb') as f:
    f.write(public_pem)
