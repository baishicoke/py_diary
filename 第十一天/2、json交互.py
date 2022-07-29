import json

#dumps python --> Json
obj = ['foo', {'bar': ('baz', None, 1.0, 2)}]
result = json.dumps(obj)
print(result)
print(json.dumps("\"foo\bar"))
print(json.dumps('\u1234'))
print(json.dumps('\\'))


# sort_keys=True 按照ASCll编码顺序排序
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

#indent=4 美化json
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))

#和内存交互 速度更快直接可以取/用
#StringIO 将字符串写入到内存里面 在内存里面交互
#dump 是操作文件句柄
from io import StringIO
io = StringIO()
json.dump(['streaming API'], io)
result = io.getvalue()
print(result)

#表示用什么作为分割符的意思  第一个是元素怎么分割 第二个是键值对怎么分割的
print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':')))


# loads json --> python 操作文件句柄
obj = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(obj[1]["bar"])


from io import StringIO
io = StringIO('["streaming API"]')
json.load(io)





