from hashlib import *
md5_obj = md5()
sha1_obj = sha1()
print(md5_obj.name, md5_obj)
print(sha1_obj.name, sha1_obj)


md5_obj.update(b'ab')
print(md5_obj.hexdigest())

print(md5_obj.digest())
print(md5_obj.name)
'''
1.hashlib实现了很多不同安全哈希和信息摘要算法的通用接口
    包括
        1.FIPS安全哈希算法
            1.SHA1, SHA224, SHA256, SHA384, SHA512
        2.RSA
            1.MD5
2.旧算法叫信息摘要,新算法叫安全哈希
'''



