
class TestSeleniumElements():
    """
        Define all you elements UI elements here.
    """

    el_close_popup      = ('id', 'at-cv-lightbox-close')    

    el_basic_example    = ('id', 'btn_basic_example')
    el_simple_form_demo = ('link_text', 'Simple Form Demo')

    el_si_user_message  = ('id', 'user-message')
    el_si_show_message  = ('xpath', "//button[text()='Show Message']")
    el_si_display       = ('xpath', "//span[@id='display']")

    def __init__(self, ui_driver):
        self.ui_driver = ui_driver

    def get_element( self, el_name):
        if hasattr( self, el_name):
            (attr_type, attr_value) = getattr( self, el_name)
            if attr_type in [ 'id', 'class', 'xpath', 'link_text' ]:
                find_func = getattr( self.ui_driver, 'find_element_by_' + attr_type)
                ui_element   = find_func( attr_value)
                return ui_element
            else:
                print("Error: Element definition for %s contains invalid attribute type %s" % (el_name, attr_type))
        else:
            print("ERROR: Element definition for '%s' is not present here." % el_name)

