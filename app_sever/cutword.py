import jieba.posseg as pseg

def cut(word):
    bens='合，分装，天，合组，滋润，代号，厅，金润，果形，店實，马，切片，线页，基，双枪，众家，货号，售价，贷号，黄金，两用，人民币，票号，现金，大号，中号，小号，收银员，机号，商品，品名，计，电脑，件数，金顶，数量，电话，号码，铁，有限公司，专用，温润，中央，发票，代码，单位，公司，热线，单，机台，时，连线，货号，金额'
    words = pseg.cut(word)
    list=[]
    for word, flag in words:
        if flag=='n':
            if word in bens:
                pass
            else:
                #print("%s %s" % (word, flag))
                list.append(word)
    return list