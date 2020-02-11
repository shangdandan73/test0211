import pytest

from Base.getDriver import get_android_driver
from Base.page import Page


class TestParaSearch:
    '''搜索测试类'''

    def setup_class(self):
        self.driver = get_android_driver('com.android.settings', '.Settings')

        '''实例化统一入口类'''
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope='class', autouse=True)
    def goto_search(self):
        # 点击搜索按钮
        self.page_obj.search_page().click_search_btn()

    @pytest.mark.parametrize('s_text,s_exp', [('1', '休眠'), ('m', 'MAC地址'), ('w', 'WPS按钮')])
    def test_para_search(self, s_text, s_exp):
        '''搜索测试类'''
        # 输入搜索内容
        self.page_obj.search_page().send_search_text(s_text)
        # 获取搜索结果
        result = self.page_obj.search_page().get_search_result()
        # 断言
        assert s_exp in result
