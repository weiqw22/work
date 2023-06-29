# 文件偏移量示例

fd = open('test','r+')

#　相对开头位置向后偏移了多少
print("当前文件偏移量位置：",fd.tell()) #0
print(fd.read(2))
print("当前文件偏移量位置：",fd.tell()) #2

#　人为调整文件偏移
fd.seek(5,0) #　相对开头位置向后偏移5个
print(fd.read(2))


fd.close()