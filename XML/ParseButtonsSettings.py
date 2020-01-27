from xml.dom import minidom


class ParseButtonSettings:
    def __init__(self):
        # xml_ = minidom.parse('XML/Button_settings.xml')
        self.xml_ = minidom.parse('XML/Button_settings.xml')
        self.settings_tree = self.xml_.documentElement
        self.settings = self.settings_tree.getElementsByTagName('Button')

    def parse_button_settings_by_name(self, name):
        for setting in self.settings:
            if  setting.getAttribute('name') == name:
                par_width = setting.getElementsByTagName('width')[0]
                self.width = int(par_width.childNodes[0].data)
                par_height = setting.getElementsByTagName('height')[0]
                self.height = int(par_height.childNodes[0].data)
    
    def return_height(self):
        return self.height

    def return_width(self):
        return self.width
