from selenium.webdriver.common.by import By


class PageElements:
    '''页面元素类'''

    '''搜索页面'''
    # 搜素按钮
    search_btn_id = (By.ID, 'com.android.settings:id/search')
    # 搜索输入框
    search_text_id = (By.ID, 'android:id/search_src_text')
    # 搜索结果
    search_results_id = (By.ID, 'com.android.settings:id/title')
