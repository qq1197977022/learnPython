from aip import AipFace

""" 你的 APPID AK SK """
APP_ID = '11645185'
API_KEY = 't7As5Fwztlpaet14mB0riYY6'
SECRET_KEY = 'iyvcZW2cMOO9NwZSYRaGH7wpna3QGwUe'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)



""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('img/0.png')

""" 调用通用文字识别（高精度版） """
res = client.basicAccurate(image)
print(res)


""" 如果有可选参数 """
options = {}
options["detect_direction"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别（高精度版） """
client.basicAccurate(image, options)


