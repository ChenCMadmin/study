class  TxT():
    def sjxtxt(self):
        list = []                                                 #文本内容装到list
        with open('../txt/sjx.txt','r',encoding='utf-8') as f :   #读取文本txt
            reads = f.readlines()
            for x in reads:                                       #循环文本添加到 list
                list.append(x.strip().split(','))
        return list[1:]                                           #返回文本内容

if __name__ == '__main__':
    print(TxT().sjxtxt())
