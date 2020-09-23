from xml.dom import minidom
class Xml():
    def sjxxml(self,shuxi,xiaobiao,bianchang):
        reads = minidom.parse('../txt/sjx.xml')
        dom = reads.documentElement
        qubian  = dom.getElementsByTagName(shuxi)[int(xiaobiao)]
        return qubian.getElementsByTagName(bianchang)[0].firstChild.data
    def sum(self,shuxi):
        reads = minidom.parse('../txt/sjx.xml')
        dom = reads.documentElement
        return len(dom.getElementsByTagName(shuxi))

if __name__ == '__main__':
    print(Xml().sjxxml('bian',0,'b1'))
    print(Xml().sum('bian'))