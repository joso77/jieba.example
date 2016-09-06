import jieba
import json
import tablib

headers = ('word', 'count')  

ret = open("speech.txt", "r").read()
seglist2 = jieba.cut(ret, ) # 精確模式(默認) cut_all=False
seglist3 = jieba.cut_for_search(ret) # 搜索引擎模式
#print seglist

seglist = seglist3

hash = {}
for item in seglist: 
    if item in hash:
      hash[item] += 1
    else:
      hash[item] = 1
    
data = tablib.Dataset(title="seglist3")
data.headers = headers
for k in hash:
    data.append([k.encode("utf_8"), hash[k]])
    
#data = tablib.Dataset(*hash, headers=headers) 

open('seglist3.xls', 'wb').write(data.xls)
#open('seglist1.csv', 'wb').write(data.csv)
open('seglist3.json', 'wb').write(data.json)
#json.dump(hash,open("count.json","w"))

