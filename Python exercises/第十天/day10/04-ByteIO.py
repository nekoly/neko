from io import BytesIO

byte_io = BytesIO()
#向内存写入二进制数据
byte_io.write("哈哈".encode("utf-8"))
#读取数据,获取写入内存中的全部数据
data = byte_io.getvalue()
print(data)
#解码
content = data.decode("utf-8")
print(content)
# str = "100"
# print(id(str))
#固定内存地址
#将数据写入到内存里面是不就是开辟了一块空间存储100 内存地址永远不会改变


