import HTMLTestRunner
import os
import unittest
from abs_test import AbsTestCase
from sort_test import SortTestCase


# 设置报告文件保存路径
cur_path = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(cur_path, "report")
if not os.path.exists(report_path): os.mkdir(report_path)

# 构造测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(AbsTestCase))
suite.addTest(unittest.makeSuite(SortTestCase))


if __name__ == "__main__":
    # 打开一个文件，将result写入此file中
    html_report = report_path + r"\result.html"
    fp = open(html_report, "wb")
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2,
                                           title="单元测试报告", description="用例执行情况")
    runner.run(suite)