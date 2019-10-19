import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import XML.ParseWindowSettings as ParseWindowSettings

class MainInterface(Gtk.Window):
    def __init__(self, *args, **kwargs):
        Gtk.Window.__init__(self)
        self.window_init() 
       
    def window_init(self):
        self.read_window_settings()
        self.set_size_request(self.width,self.height)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_title(self.widow_title)  
    def read_window_settings(self):
        parse_xml = ParseWindowSettings.ParseWindowSettings()
        self.width = parse_xml.return_width()
        self.height = parse_xml.return_height()
        self.widow_title = parse_xml.return_window_title()
     