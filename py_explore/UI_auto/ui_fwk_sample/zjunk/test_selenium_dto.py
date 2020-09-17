
class TestSeleniumDTO():
    def __init__( self, **kwargs):
        self.browser  = kwargs.get('browser', 'Firefox')
        self.site_url = kwargs.get('site_url', 'https://www.seleniumeasy.com/test/')

    def __repr__(self):
        return str(self.__dict__)

if __name__ == '__main__':
    ts_obj = TestSeleniumDTO( browser = 'Chrome')
    print( "Browser is : " + ts_obj.browser)
    print( "Site URL is: " + ts_obj.site_url)


