from selenium.webdriver.support.wait import WebDriverWait


class Base:
    '''基础操作类'''
    def __init__(self,driver):
        self.driver = driver

    def select_elem(self,location,timeout=5,poll=1):
        '''
        定位元素方法
        :param location: 元组，元素定位方法，(By.ID,'元素id')，(By.class_name,'元素class')，(By.xpath,'xpath')
        :param timeout: 元素等待时间
        :param poll:元素搜索间隔
        :return: 返回元素定位对象
        '''
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*location))

    def select_elems(self,location,timeout=5,poll=1):
        '''
        定位一组元素方法
        :param location: 元组，元素定位方法，(By.ID,'元素id')，(By.class_name,'元素class')，(By.xpath,'xpath')
        :param timeout: 元素等待时间
        :param poll:元素搜索间隔
        :return: 返回元素列表
        '''
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(*location))

    def click_elem(self,location,timeout=5,poll=1):
        '''
        点击元素方法
        :param location: 元组，元素定位方法，(By.ID,'元素id')，(By.class_name,'元素class')，(By.xpath,'xpath')
        :param timeout: 元素等待时间
        :param poll:元素搜索间隔
        :return:
        '''
        self.select_elem(location,timeout,poll).click()

    def send_elem(self,location,text,timeout=5,poll=1):
        '''
        点击元素方法
        :param location: 元组，元素定位方法，(By.ID,'元素id')，(By.class_name,'元素class')，(By.xpath,'xpath')
        :param timeout: 元素等待时间
        :param poll:元素搜索间隔
        :return:
        '''
        element = self.select_elem(location,timeout,poll)
        element.clear()
        element.send_keys(text)

