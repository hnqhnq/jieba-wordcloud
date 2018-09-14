""" 
@file: 关键词提取.py
@Time: 2018/08/27
@Author:heningqiu
"""
import jieba.analyse
'''
txt为待提取的文本
topK为返回几个TF/IDF权重最大的关键词，默认值为20
'''
print("***案例1***"*3)
txt='那些你很冒险的梦，我陪你去疯，折纸飞机碰到雨天终究会坠落，伤人的话我直说，因为你会懂，冒险不冒险你不清楚，折纸飞机也不会回来，做梦的人睡不醒！'
Key=jieba.analyse.extract_tags(txt,topK=3)
print(Key)
#----------------------------------------------------------------------------------------------------
print("***案例2***"*3)
# 字符串前面加u表示使用unicode编码
content = u'中国特色社会主义是我们党领导的伟大事业，全面推进党的建设新的伟大工程，是这一伟大事业取得胜利的关键所在。党坚强有力，事业才能兴旺发达，国家才能繁荣稳定，人民才能幸福安康。党的十八大以来，我们党坚持党要管党、从严治党，凝心聚力、直击积弊、扶正祛邪，党的建设开创新局面，党风政风呈现新气象。习近平总书记围绕从严管党治党提出一系列新的重要思想，为全面推进党的建设新的伟大工程进一步指明了方向。'
# 第一个参数：待提取关键词的文本
# 第二个参数：返回关键词的数量，重要性从高到低排序
# 第三个参数：是否同时返回每个关键词的权重
# 第四个参数：词性过滤，为空表示不过滤，若提供则仅返回符合词性要求的关键词
keywords = jieba.analyse.extract_tags(content, topK=5, withWeight=True, allowPOS=())
# 访问提取结果
for item in keywords:
    # 分别为关键词和相应的权重
    print(item[0], item[1])
print("---------------------------------------------------")
# 同样是四个参数，但allowPOS默认为('ns', 'n', 'vn', 'v')
# 即仅提取地名、名词、动名词、动词
keywords = jieba.analyse.textrank(content, topK=5, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
# 访问提取结果
for item in keywords:
    # 分别为关键词和相应的权重
    print(item[0], item[1])