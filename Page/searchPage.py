from Base.base import Base
from Page.pageElements import PageElements


class SearchPage(Base):
    '''搜索页面类'''

    def __init__(self, driver):
        Base.__init__(self,driver)
        self.page_elements = PageElements()

    def click_search_btn(self):
        '''点击搜索按钮'''
        self.click_elem(self.page_elements.search_btn_id)

    def send_search_text(self, text):
        '''输入搜索内容'''
        self.send_elem(self.page_elements.search_text_id, text)

    def get_search_result(self):
        '''获取搜索结果'''
        results = self.select_elems(self.page_elements.search_results_id)
        return [i.text for i in results]
