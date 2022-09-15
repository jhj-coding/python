import pandas as pd

#读取csv
# pd.read_csv(path,usecols=[使用列名称]，names=[当第一行不是表头时 添加])
#下载到csv
# DataFrame.to_csv(path,columns=[想要保存列名称]，index=False标识不要行索引 ,mode='a'追加模式，header=False 标识不要表头)

#hdf5可以理解存储3维数据的 是压缩的 比较快
# 读取hdf5需要安装tables
# 一个键对应一个hdf
# 如果只有一个键 可以不传参数key
# pd.read_hdf(path,key=读取的键)
# DataFrame.to_hdf(path,key=保存的键)

#json
# pd.read_json(path,orient="recoeds",lines=True 是否按行作为一个样本读取)
#DataFrame.to_json(path,orient="recoeds",lines=True 是否按行作为一个样本读取)