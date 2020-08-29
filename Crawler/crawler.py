from user import User


class Crawler:

    def __init__(self, method=None, usr=None, pwd=""):
        '''
        :param crawler_method - method which app will crawl data 
        '''
        self.method = method
        self.usr = User(usr=usr, pwd=pwd)

    @property
    def crawler_method(self):
        return self.method

    @crawler_method.setter
    def crawler_method(self, method):

        if method == 'bs4':
            self.method = method

        elif method == 'selenium':
            self.method = method

        else:
            self.method = None

    @property
    def username(self):
        return self.usr.usr

    @username.setter
    def username(self, usr):
        self.usr.usr = usr

    @property
    def password(self):
        return self.usr.pwd

    @password.setter
    def password(self, pwd):
        self.usr.pwd = pwd

    def crawl(self, headless=False):
        '''
        :param usr - username to crawl
        :param headless - do not open browser
        '''

        if self.crawler_method == 'bs4':
            return self.crawl_with_bs4()

        if self.crawler_method == 'selenium':
            return self.crawl_with_selenium(headless)

        # def crawl_with_bs4(usr):
        #     pass

    def crawl_with_bs4(self):
        '''
        :param usr: username to crawl
        :return:
        '''
        from Crawler.Method.bs4_crawler import crawl
        pass

    def crawl_with_selenium(self, headless=False):
        '''
        :param headless: do not open browser
        :return: dictionary with user's information
        '''

        # Import needed Selenium class
        from Crawler.Method.selenium_crawler import SeleniumCrawler

        selenium = SeleniumCrawler(self.username, headless=headless)

        if len(self.password) > 0:

            selenium.logged_in, response = selenium.log_in(self.username, self.password)

            if selenium.logged_in is False and len(response) > 0:
                return None, response['response']

        if selenium.status is not 200:
            return None, 'Username is not found.'

        return {
            'username': self.username,
            'posts': selenium.get_posts(),
            'followers': selenium.get_followers(),
            'following': selenium.get_following(),
            'biography': selenium.get_account_biography(),
            'post': selenium.get_all_posts(limit=28)
        }, 'Successful'
