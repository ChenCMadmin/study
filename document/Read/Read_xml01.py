from xml.dom import minidom

class Xml01():
    def xml01(self,sx,xb,bc):
        # 解析文件
        du = minidom.parse('../txt/sjx.xml')
        # 获取值
        zhi = du.documentElement
        # 获取元素
        shu = zhi.getElementsByTagName(sx)[int(xb)]
        return shu.getElementsByTagName(bc)[0].firstChild.data
    def len1(self,sx):
        # 解析文件
        du = minidom.parse('../txt/sjx.xml')
        # 获取值
        zhi = du.documentElement
        return len(zhi.getElementsByTagName(sx))



if __name__ == '__main__':
    print(Xml01().xml01('bian',0,'b2'))
    print(Xml01().len1('bian'))
