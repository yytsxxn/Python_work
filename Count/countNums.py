#coding:utf-8
#统计《三国演义》人名出现次数
import jieba

with open("三国演义.txt", "r", encoding='utf-8') as f:
    text = f.read()
    words = jieba.lcut(text)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        elif word == "诸葛亮" or word == "孔明曰":
            rword = "孔明"
        elif word == "关公" or word == "云长":
            rword = "关羽"
        elif word == "玄德" or word == "玄德曰":
            rword = "刘备"
        elif word == "孟德" or word == "丞相":
            rword = "曹操"
        else:
            rword = word
        counts[rword] = counts.get(rword, 0) + 1

    execlude = ['大军','荆州', '将军', '却说', '二人', '不可', '不能', '如此', '商议', '如何', '都督',
                '东吴', '一人', '汉中', '众将', '后主', '只见', '蜀兵', '不知', '人马', '于是', '大叫',
                '军马', '主公', '左右', '军士', '引兵', '次日', '大喜', '天下', '今日', '不敢', '陛下',
                '上马', '此人', '天子', '一面', '先主', '太守', '后人', '背后', '魏兵', '何不']
    for ch in execlude:
        del counts[ch]
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)

    #人工去噪：去除非人名，保留前十五人名
    namemax = 15
    cnt = 13
    i = 13
    while cnt < namemax:
        word, count = items[i]
        i += 1
        ch = input("{:<10}{:>5} (y/n)".format(word, count))
        if ch == 'n':
            execlude.append(word)
            del counts[word]
        else:
            cnt += 1
    #print(execlude)
    #输出结果
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(namemax):
        word,count = items[i]
        print("{:\u3000<8}{:>8}".format(word, count))

        
