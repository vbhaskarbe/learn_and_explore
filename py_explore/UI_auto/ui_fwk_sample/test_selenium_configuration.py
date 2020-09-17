import os
import yaml

from test_selenium_configuration_dto import TestSeleniumConfigurationDTO

class TestSeleniumConfiguration( object):
    def getDefault( self, testbed_file = None):
        if testbed_file == None:
            if os.environ.get('TESTBED_CONFIG_FILE') is None:
                self.__raise_exception("TESTBED_CONFIG_FILE is not set in environment.")
            else:
                testbed_file = os.environ.get('TESTBED_CONFIG_FILE')
        ## Load properties
        try:
            tb_fh = open(testbed_file)
            default_config = yaml.load( tb_fh)
            tb_fh.close()
        except Exception as e:
            print("Error seen during yaml load : " + str( e))
        ## SITE_URL must be present in properties file
        if "SITE_URL" not in default_config:
            self.__raise_exception("TESTBED CONFIG FILE DOES NOT HAVE 'SITE_URL' VARIABLE, PLEASE DEFINE.")
        ## Set defaults for required params.
        default_config['ENABLE_SCREENSHOTS'] = default_config.get('ENABLE_SCREENSHOTS', 'False')
        default_config['WORK_SPACE']         = default_config.get('WORK_SPACE', '/tmp/test_logs')
        default_config['BROWSER']            = default_config.get('DEFAULT_BROWSER', 'Firefox')
        print( default_config)
        return TestSeleniumConfigurationDTO( **default_config)

    def __raise_exception( self, msg):
        raise RuntimeError( msg)


if __name__ == '__main__':
    #tb_properties = TestSeleniumConfiguration().getDefault(testbed_file = 'testbed_config.yml')
    tb_properties = TestSeleniumConfiguration().getDefault()
    print( tb_properties.SITE_URL)
    print( tb_properties.WORK_SPACE)
    print( tb_properties.DEFAULT_BROWSER)
    print( tb_properties.ENABLE_SCREENSHOTS)


