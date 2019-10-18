import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from XML import ParseWindowSettings
class MainInterface(Gtk.Window):
    def __init__(self, *args, **kwargs):
        Gtk.Window.__init__(self)
        self.window_init()
    def window_init(self):
       self.read_window_settings()
       self.set_size_request(self.width,self.height)
       self.set_position(Gtk.WindowPosition.CENTER)  
    def read_window_settings(self):
        parse_xml = ParseWindowSettings.ParseWindowSettings()
        self.width = parse_xml.return_width()
        self.height = parse_xml.return_height()
interface = MainInterface()
interface.connect('destroy',Gtk.main_quit)
interface.show_all()
Gtk.main()
       