import os
print(f'<{repr(os.linesep)}>')
print(f'<{str(os.linesep)}>')

# 一.不同模式打开文件区别
#   1.文本模式 ~ 行分隔符
#     1.win: \r\n
#     2.Unix/linux/Mac: \n
#     3.老Mac: \r
#   2.在字节模式 ~ 两个独立字符\ n
#   3.Note
#       1.当以文本模式, 在win平台写入\n时, 会自动转换为\r\n, 但读数据过程不会转换

f1 = open('file/t_mode.txt', 'wt')    # 文本写模式
f2 = open('file/b_mode.txt', 'wb')    # 字节写模式
f1.write('HHH\nHHH')    # 写入字符串
f2.write(b'HHH\nHHH')   # 写入bytes
f1.close()
f2.close()


f1 = open('file/t_mode.txt', 'rb')    # 字节读模式
f2 = open('file/b_mode.txt', 'rb')
b_data1 = f1.read()    # 读取字节数据
b_data2 = f2.read()
f1.close()
f2.close()

print(b_data1)
print(b_data2)




