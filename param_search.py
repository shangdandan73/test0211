"""
设置搜索练习：
 输⼊1: 判断"休眠"存在
 输⼊m: 判断"MAC地址"存在
 输⼊w: 判断"WPS按钮"存在
"""
import pytest
from appium import webdriver



class TestSearch:
    '''搜索测试类'''

    def setup_class(self):
        """初始化dirver"""
        # server 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # app的信息
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'

        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope='class',autouse=True)
    def goto_search(self):
        #点击搜索
        self.driver.find_element_by_id('com.android.settings:id/search').click()

    @pytest.mark.parametrize("s_text,s_exp",[('1','休眠'),('m','MAC地址'),('w','WPS按钮')])
    def test_search(self,s_text,s_exp):
        '''搜索测试方法'''
        # 输入搜索内容
        search_text=self.driver.find_element_by_id('android:id/search_src_text')
        search_text.clear()
        search_text.send_keys(s_text)
        # 获取结果
        results = self.driver.find_elements_by_id('com.android.settings:id/title')
        # 断言
        assert s_exp in [i.text for i in results]

if __name__ == '__main__':
    pytest.main()