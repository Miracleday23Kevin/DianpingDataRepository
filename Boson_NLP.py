#!/usr/bin/env python
# _*_ coding: utf-8 _*_


from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
from pprint import pprint
import uniout

nlp = BosonNLP('lTUXeys9.4043.1m_8jMIzyROQ')

# Text_nlp = u'宝马中国召回1418辆进口X5汽车'
def main():
    Text_nlp = u'''
    一直和同事朋友在他们家吃火锅的，但是也一直没有点评，这次来好好和大家分享一下。
    首先说说他们家的服务，海底捞的服务一直在行业中也是鼎鼎有名的，大家都众所周知的，所以也不用我多说什么了。另外他们等位的时候也考虑的比较周到，等位处有一个很大的空间放满桌子，客人可以在那里吃吃瓜子聊聊天等位，另外还设有儿童区，小朋友等位的时候可以在翻斗乐里面玩玩，另外还有按摩区和美甲区，都是可以让客人在等位中打发时间的。
    再来说说他们的菜品，他们家点菜都是可以点半份的，我觉得这个是非常好的，尤其对于两个人去吃火锅，又不能吃很多，又都想尝尝味道，而且他们半分的量也都是分量很足的。特别喜欢吃他们家的嫩牛肉，味道有点辣辣的，牛肉在火锅里面涮好之后嫩嫩的，小朋友也能吃。最近去吃的一次点了他们家的番茄锅底，味道超级赞~\(≧▽≦)/~味道很浓郁，而且服务员在还没有涮锅之前会帮你调一份番茄牛肉汤，在吃饭之前喝一碗汤，超级暖胃。
    总之，在他们家吃饭，有种宾至如归的感觉，皇帝的待遇啊！！！
    '''
    # SentimentsAnalysis(Text_nlp)
    # KeywordsExtraction(Text_nlp)
    # TagsOfTheWordsInTexts(Text_nlp)

def SentimentsAnalysis(text):
    r = nlp.sentiment(text)
    print (r)
    print ('--------------------------')
    print ('\n')


# r2 = nlp.ner(Text_nlp)[0]
# words = r2['word']
# entities = r2['entity']
#
# for entity in entities:
#     print (''.join(words[entity[0]:entity[1]]),entity[2])
#
# # print(nlp.sentiment(Text_nlp))
# pprint(nlp.extract_keywords(Text_nlp,top_k=10))
'''
Top K most related words.

'''
def TopKrelatedWordsWithTheSeeds(text):

    # text = '火锅'
    result = nlp.suggest(text, top_k=10)
    for item in result:
        print(item[0], item[1].strip())
    print ('--------------------------')
    print ('\n')





'''
Keywords extraction
'''
def KeywordsExtraction(text):
    result = nlp.extract_keywords(text,top_k= 50)
    temp = 1
    for weight, word in result:
        if temp == 1:
            TopKrelatedWordsWithTheSeeds(word)
            temp = 0
        print (weight,word)
    print ('--------------------------')
    print ('\n')



'''

Tags of the review tests, separate the word according to its noun/ verb or adj.

'''

def TagsOfTheWordsInTexts(text):
    tag_result = nlp.tag(text)
    # 完整的参数调用格式如下：
    # tag_result = nlp.tag(text, space_mode=0, oov_level=3, t2s=0, special_char_conv=0)
    # 修改space_mode选项为1，如下：
    tag_result = nlp.tag(text, space_mode=1, oov_level=3, t2s=0, special_char_conv=0)
    # 修改oov_level选项为1，如下：
    # tag_result = nlp.tag(text, space_mode=0, oov_level=1, t2s=0, special_char_conv=0)
    # 修改t2s选项为1，如下：
    # tag_result = nlp.tag(text, space_mode=0, oov_level=3, t2s=1, special_char_conv=0)
    # 修改特殊字符转换选项为1,如下：
    # tag_result = nlp.tag(text, space_mode=0, oov_level=3, t2s=0, special_char_conv=1)
    List = []
    for d in tag_result:
        List.append(zip(d['word'],d['tag']))
        # pprint(zip(d['word'],d['tag']))
        print (d['tag'])
        print(zip(d['word'],d['tag']))
    print ('\n')
    '''
    Use the List and the for loop to print out different categories of the words.
    '''
    for item in List:
        for temp in item:
            if temp[1] == 'n':
                print (temp[0],temp[1])
            # print (temp[1])
        # print (item)
    # print (List[0][3][1])


    print ('--------------------------')
    for d in tag_result:
        if d['tag'] == u'n':
            print (zip(d['word'],d['tag']))


        # pprint(' '.join(['%s%s'% it for it in zip(d['word'],d['tag'])]))
        # print(' '.join(['%s/%s' % it for it in zip(d['word'], d['tag'])]))
        # pprint(' '.join(['%s%s'% it for it in zip(d['word'],d['tag'])))
        # if d['tag'] == 'n':
        #     pprint('%s%s',zip(d['word'],d['tag']))

main()