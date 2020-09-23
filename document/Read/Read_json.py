import json

class Json():
    def sjxjson(self):
        with open('../txt/sjx.json','r',encoding='utf-8') as f:
            reads = json.load(f)
        return reads['data']

if __name__ == '__main__':
    print(Json().sjxjson()[0]['expect'])