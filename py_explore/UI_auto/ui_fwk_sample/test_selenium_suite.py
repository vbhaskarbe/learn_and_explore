import os
import unittest

#from test_selenium_logger import ml_object, logger

from test_selenium_base    import TestSeleniumBase
from test_selenium_library import UiTestDecorator
from test_selenium_logger  import MyLogger, logger
from test_selenium_service import TestSeleniumService

class TestSeleniumDemoSuite( unittest.TestCase):
    def setUp(self):
        #self.mylog = MyLogger()
        #self.mylog.initialize_testsuite( 'TestSeleniumSuite')
        
        self.selbase_obj = TestSeleniumBase()
        self.selbase_obj.start_browser()
        import time
        time.sleep(2)

        self.selui_object = TestSeleniumService( self.selbase_obj.b_driver)
        self.selui_object.close_popup()

    @UiTestDecorator
    def test_single_input_field_01( self):
        logger.info("Go to simple form demo page")
        self.selui_object.go_to_simple_form_demo()
        field_text = 'UI_AUTOMATION'
        logger.info("Test single input field with %s" % field_text)
        result = self.ui_object.single_input_field_test( field_text)
        self.assertEqual( field_text, result)    

    @UiTestDecorator
    def DIS_test_single_input_field_02( self):
        logger.info("This is new log line 01")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def tearDown(self):
        self.selbase_obj.close_browser()

if __name__ == '__main__':
    unittest.main()


