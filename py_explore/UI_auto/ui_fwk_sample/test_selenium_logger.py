import os
import logging
import  inspect

from test_selenium_configuration import TestSeleniumConfiguration

class MyLogger(object):
    def __init__( self, workspace = None):
        self.workspace     = workspace
        if self.workspace == None:
            self.workspace = str(TestSeleniumConfiguration().getDefault().WORK_SPACE)
        self.logger = logging.getLogger()

    def initialize_testsuite( self, suitename):
        self.testsuite_name = suitename #str(inspect.stack()[-1].filename).split('.')[0]
        log_level = setattr( logging, TestSeleniumConfiguration().getDefault().LOG_LEVEL, str(TestSeleniumConfiguration().getDefault().LOG_LEVEL))
        self.logger.setLevel( logging.DEBUG)
        self.log_dirname = os.path.join( self.workspace, self.testsuite_name)
        if not os.path.exists( self.log_dirname):
            os.makedirs( self.log_dirname)
        self.initialized = True
        print("INFO: Logger initialized")

    def get_logger(self):
        return self.logger

    def start_logging(self, testcase_name):
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        self.testcase_name = testcase_name
        self.logger = logging.getLogger( self.testcase_name)
        logging.basicConfig( level    = logging.DEBUG,
                             format   = '%(asctime)s:%(filename)s:%(funcName)s:%(lineno)s:%(levelname)s:%(message)s',
                             datefmt  = '%Y-%m-%d %H:%M:%S',
                             filename = os.path.join( self.log_dirname, testcase_name + '.log'),
                             filemode = 'w')
        self.logger.info("Start logging for %s" % testcase_name)
         
    def stop_logging( self):
        self.initialized = False
        for handler in logging.root.handlers[:]:
            handler.close()
            logging.root.removeHandler(handler)
        #self.logger.info("Stop logging for %s" % self.testcase_name)

ml_object = MyLogger()
logger    = ml_object.get_logger()

if __name__ == '__main__':
    import os
    this_filename = os.path.splitext(os.path.basename(__file__))[0]
    print(this_filename)
    ml_obj = MyLogger()
    ml_obj.initialize_testsuite()
    ml_obj.start_logging('test_framework_001')
    ml_obj.logger.info("This is an informative message")
    ml_obj.stop_logging()

