import base64
import re
from io import BytesIO
from PIL import Image
import pytesseract  # 用于图片转文

r"""
识别验证码图片
"""


def image_open(image_path):
    """
    打开图片
    :param image_path: 图片路径，相对路径  "./fusion_datasets/2.jpg"
    :return: PIL格式图片
    """
    image = Image.open(image_path)
    # 输出图片维度
    print("image_shape: ", image.size)
    # 显示图片
    image.show()
    return image


def image_to_base64(image_path):
    """
    图片转化成base64
    :param image_path: 图片的绝对路径
    :return: base64格式字符串
    """
    img_file = open(image_path, 'rb')  # 二进制打开图片文件
    img_b64encode = base64.b64encode(img_file.read())  # base64编码
    img_file.close()  # 文件关闭
    return img_b64encode


def base64_to_image(base64_str, image_path=None):
    """
    base64格式转换成PIL格式图片并保存
    :param base64_str: base64字符串
    :param image_path: 保存图片路径
    :return: PIL格式图片
    """
    # base64_str="data:image/jpeg;base64,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"
    base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    if image_path:
        img.save(image_path)
    # img.show()
    return img


def processing_image(image_obj):
    """
    首先用convert把图片转成黑白色。设置threshold阈值，超过阈值的为黑色
    :param image_obj: PIL格式，图像
    :return: 处理后的图片
    """
    img = image_obj.convert("L")  # 转灰度
    pixdata = img.load()
    w, h = img.size
    threshold = 160  # 该阈值不适合所有验证码，具体阈值请根据验证码情况设置
    # 遍历所有像素，大于阈值的为黑色
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    # img.show()
    return img


def image_str(image):
    """
    将图片转化成文字，
    （1）安装tesseract.exe，下载安装：http://www.xue51.com/soft/1594.html
    （2）设置环境变量 TESSDATA_PREFIX，它的值为tessdata目录
    :param image:PIL格式 图片
    :return:验证码
    """
    pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"  # 设置pyteseract路径
    result = pytesseract.image_to_string(image)  # 图片转文字
    print(result)
    resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
    result_four = resultj[0:4]  # 只获取前4个字符
    print("aa")
    print(resultj)  # 打印识别的验证码
    return result_four


if __name__ == '__main__':
    image = base64_to_image()
    image2 = processing_image(image)
    image_str(image2)
