import unittest
import requests
from random import randint
from ddt import ddt, file_data
from api_class.api_keyword.keword_demo import Methon
@ddt
class Interface(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.token = None
        cls.hospitalId = None
    # token值获取
    @file_data("../api_data/token_demo.yaml")
    def test_1_token(self, **kwargs):
        res = requests.get(url=kwargs["url"], params=kwargs["data"])
        value = Methon().get_text(res.text, "message")
        Interface.token = Methon().get_text(res.text, "token")
        self.assertEqual(first=kwargs["compare"], second=value, msg="获取token失败")
    # 出生医学证明接口
    @file_data("../api_data/brith_demo.yaml")
    def test_2_brith(self, **kwargs):
        headers = kwargs["headers"]
        headers["cookie"] = "token=" + self.token
        res = requests.get(url=kwargs["url"], params=kwargs["data"], headers=headers)
        value = Methon().get_text(res.text, "msg")
        self.assertEqual(first=kwargs["compare"], second=value, msg="失败")
    # 健康证机构获取
    @file_data("../api_data/health_demo.yaml")
    def test_3_health(self, **kwargs):
        res = requests.get(url=kwargs["url"], params=kwargs["data"])
        value = Methon().get_text(res.text, "message")
        hospital = Methon().get_text(res.text, "hospitalId")
        Interface.hospitalId = hospital[randint(0, 20)]
        self.assertEqual(first=kwargs["compare"], second=value, msg="获取失败")
    # 健康证号源查询
    @file_data("../api_data/query_demo.yaml")
    def test_4_query(self, **kwargs):
        data = kwargs["data"]
        data["hospitalId"] = self.hospitalId
        res = requests.get(url=kwargs["url"], params=kwargs["data"])
        value = Methon().get_text(res.text, "message")
        self.assertEqual(first=kwargs["text"], second=value)
if __name__ == "__main__":
    unittest.main()
