import os

class TestSeleniumUtilities():
    def __init__( self, testname):
        self.counter   = 1
        self.testname  = testname
    
    ## Take screenshots to help with debug later.
    def take_screenshot( self, ui_driver):
        ui_driver.save_screenshot( self.testname + '_' + str(self.counter).zfill(3) + '.PNG')
        self.counter = self.counter + 1
    
    def process_screenshots( self):
        import glob
        from zipfile import ZipFile
        try:
            png_files_list = glob.glob( os.path.join( self.testname + '_*.PNG'))
            with ZipFile( self.testname + '.zip', 'w') as zipObj:
                for filename in png_files_list:
                    zipObj.write( filename, os.path.basename(filename))
                    os.remove( filename)
            zipObj.close()
        except Exception as e:
            print("process_screenshots: Failed: %s" % str(e))
        finally:
            print( "Screenshots are zipped up in to %s" % (self.testname + '.zip'))


