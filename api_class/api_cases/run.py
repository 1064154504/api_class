import unittest,HTMLTestRunner
if __name__ == "__main__":
    discover = unittest.defaultTestLoader.discover(start_dir="./",pattern="api_case.py")
    result = open("./api_report.html","wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=result,title="接口测试报告",description="执行测试情况")
    runner.run(discover)
    result.close()


if __name__ == "__main__":
    discover = unittest.defaultTestLoader.discover(start_dir="./",pattern="api_case.py")
    result = open("./api_report.html","wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=result,title="接口测试报告",description="执行测试情况")
    runner.run(discover)
    result.close()