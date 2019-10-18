from xml.dom import minidom
class ParseWindowSettings:
    def __init__(self):
        xml_ = minidom.parse('XML/Window_settings.xml')
        settings_tree = xml_.documentElement
        settings = settings_tree.getElementsByTagName('window_settings')
        for setting in settings:
            par_width= setting.getElementsByTagName('width')[0]
            self.width= int(par_width.childNodes[0].data)
            par_height = setting.getElementsByTagName('height')[0]
            self.height = int(par_height.childNodes[0].data)
    def return_height(self):
        return self.height
    def return_width(self):
        return self.width               
       