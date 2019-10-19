import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import XML.ParseWindowSettings as ParseWindowSettings
import XML.ParseButtonsSettings as ParseButtonsSettings

class MainInterface(Gtk.Window):
    def __init__(self, *args, **kwargs):
        Gtk.Window.__init__(self)
        self.window_init() 
       
    def window_init(self):
        self.read_window_settings()
        self.set_size_request(self.width,self.height)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_title(self.widow_title) 
        self.panel_init()
    def read_window_settings(self):
        parse_xml = ParseWindowSettings.ParseWindowSettings()
        self.width = parse_xml.return_width()
        self.height = parse_xml.return_height()
        self.widow_title = parse_xml.return_window_title()
    def panel_init(self):
        self.main_box = Gtk.Box()
        self.add(self.main_box)
        self.button_box = Gtk.Grid()
        self.charts_box = Gtk.Grid()
        self.main_box.add(self.button_box)
        self.main_box.add(self.charts_box)
        self.button_panel_init()
    
    def button_panel_init(self):
        self.start_button()
        self.stop_button()
        self.button_box.add(self.start_button_)
        self.button_box.attach_next_to(self.stop_button_,self.start_button_,Gtk.PositionType.BOTTOM,2,2)

    def start_button(self):
        self.start_button_ = Gtk.Button(label = 'Start')
        parse_xml = ParseButtonsSettings.ParseButtonSettings()
        parse_xml.parse_button_settings_by_name('Start')
        self.start_button_.set_size_request(parse_xml.return_width(),parse_xml.return_height())   
    def stop_button(self):
        self.stop_button_ = Gtk.Button(label = 'Stop')
        parse_xml = ParseButtonsSettings.ParseButtonSettings()
        parse_xml.parse_button_settings_by_name('Stop')
        self.stop_button_.set_size_request(parse_xml.return_width(),parse_xml.return_height())