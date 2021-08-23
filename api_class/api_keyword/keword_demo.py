#字段校验方法
import json,jsonpath
class Methon:
    def get_text(self,res,key):
        if res is not None:
            try:
                # 将res文本转换为json，通过jsonpath解析获取到指定的key的value值
                text = json.loads(res)
                # jsonpath获取获取的结果是list类型数据
                value = jsonpath.jsonpath(text, "$..%s"%key)
                if len(value) == 1:
                    return value[0]
                return value
            except Exception as e:
                return e
        else:
            return None