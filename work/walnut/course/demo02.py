
""" ��ȡͼƬ """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('example.jpg')

""" ����ͨ������ʶ��, ͼƬ����Ϊ����ͼƬ """
client.basicGeneral(image);

""" ����п�ѡ���� """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" ����������ͨ������ʶ��, ͼƬ����Ϊ����ͼƬ """
client.basicGeneral(image, options)

url = "https//www.x.com/sample.jpg"

""" ����ͨ������ʶ��, ͼƬ����ΪԶ��urlͼƬ """
client.basicGeneralUrl(url);

""" ����п�ѡ���� """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" ����������ͨ������ʶ��, ͼƬ����ΪԶ��urlͼƬ """
client.basicGeneralUrl(url, options)

