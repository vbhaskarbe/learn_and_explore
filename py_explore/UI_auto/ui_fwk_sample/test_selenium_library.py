
import traceback
import inspect
import os

#from test_selenium_logger import ml_object, logger
from test_selenium_logger import logger

def UiTestDecorator(UiTestMethod):
    def wrap(*args, **kwargs):
        retval = None
        try:
            ml_object = MyLogger()
            logger = ml_object.get_logger()
            ml_object.start_logging(UiTestMethod.__name__)
            #print("Test method to run is : %s" % UiTestMethod.__name__)
            retval = UiTestMethod(*args)
            #print("Test Result is %s" % retval)
            ml_object.stop_logging()
            return retval
        except:
            print("Exception while running Test method : %s" %  UiTestMethod.__name__)
            tb = traceback.format_exc()
            ml_object.stop_logging()
            raise RuntimeError("*************test case %s has error*************" % UiTestMethod.__name__)
    return wrap

