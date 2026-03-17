# 导包
from api.login import LoginAPI
from api.course import CourseAPI
from api.contract import ContractAPI
import config
# 创建测试�?
class TestContract:
    # 初始�?
    token = None
    fileName=None
    # 前置处理
    def setup_method(self):
        # 实例化接口对�?
        self.login_api = LoginAPI()
        self.course_api= CourseAPI()
        self.contract_api = ContractAPI()

    # 后置处理
    def teardown_method(self):
        pass

    # 1、登录成�?
    def test_login_success(self):
        # 获取验证�?
        responseImage = self.login_api.get_verify_code()
        print(responseImage.status_code)
        print(responseImage.json())
        # 打印uuid数据
        print(responseImage.json().get("uuid"))

        # 登录
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": responseImage.json().get("uuid")
        }
        res_l = self.login_api.login(test_data=login_data)
        print(res_l.status_code)
        print(res_l.json())
        TestContract.token=res_l.json().get("token")  #添加token
        print(TestContract.token)
    # 课程新增 方法
    def test_add_Course(self):
        add_data = {"name": "测试开发提升课01", "subject": "6", "price": 899, "applicablePerson": "2", "info": "测试开发提升课01"}
        response=self.course_api.add_course(test_data=add_data,token=TestContract.token)
        print(response.json())

    # 上传合同成功
    def test_upload_contract(self):
        self.test_login_success()  # 前置条件:登录
        # 读取pdf文件数据
        # f = open("../data/test.pdf", "rb")
        f = open(config.BASE_PATH + "/data/1.txt", "rb")
        response = self.contract_api.upload_contract(test_data=f, token=TestContract.token)
        TestContract.fileName=response.json().get("fileName")
        print(response.json())

    # 合同新增成功
    def test_add_contract(self):
        self.test_upload_contract()  #前置条件-上传合同
        # contractNo: 数据唯一
        add_data = {"name": "测试888", "phone": "13612345678", "contractNo": "HT20230007", "subject": "6",
                    "courseId": " 99", "channel": "0", "activityId": 77, "fileName": TestContract.fileName}
        response = self.contract_api.add_contract(test_data=add_data, token=TestContract.token)
        print(response.json())












