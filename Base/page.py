from Page.searchPage import SearchPage


class Page:
    '''实例化所有页面类'''

    def __init__(self, driver):
        self.driver = driver

    def search_page(self):
        '''返回页面类实例化对象'''
        return SearchPage(self.driver)
