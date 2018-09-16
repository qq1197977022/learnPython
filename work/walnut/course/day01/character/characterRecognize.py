from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '11655307'
API_KEY = 'FiBNLxVtRqGR3MOO9AvpK1xD'
SECRET_KEY = 'rxiE9hSsP1FfzH8lISFiEi6CrDa3bVZ7'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):    # 读取图片
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('img/0.png')

""" 调用通用文字识别（高精度版） """
res = client.basicAccurate(image)
print(res)

# """ 如果有可选参数 """
# options = {}
# options["detect_direction"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别（高精度版） """
# client.basicAccurate(image, options)




