# 中文分词
import jieba
seg_list = jieba.cut("北京野生动物园轿车遭黑熊围堵")
print("Default Mode:", ' '.join(seg_list))
