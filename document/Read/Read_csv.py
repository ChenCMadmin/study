import csv
class Csv():
    def sjxcsv(self):
        list = []
        with open('../txt/sjx.csv','r',encoding='utf-8') as f:
            reads = csv.reader(f)
            for i in reads:
                list.append(i)
        return list
if __name__ == '__main__':
    print(Csv().sjxcsv())


