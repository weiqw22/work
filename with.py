# ｗｉｔｈ语句

with open('test') as f:  #　生成文件对象
    data = f.read()
    print(data)

#语句块结束　ｗｉｔｈ生成的对象ｆ会被自动释放
