import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import XML.ParseWindowSettings as ParseWindowSettings
import XML.ParseButtonsSettings as ParseButtonsSettings
from functools import partial

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

        self.init_menu_bar() 
    def read_window_settings(self):
        parse_xml = ParseWindowSettings.ParseWindowSettings()
        
        self.width = parse_xml.return_width()
        
        self.height = parse_xml.return_height()
        
        self.widow_title = parse_xml.return_window_title()

    def panel_init(self):
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        

        self.add(self.main_box)
        
        self.menu_box = Gtk.Box()

        
        self.main_box.add(self.menu_box)
        


        self.button_frame = Gtk.Grid()

        
        self.chart_frame = Gtk.Grid()

        self.chart_buttons_grid = Gtk.Grid()

        self.chart_buttons_grid.add(self.button_frame)

        self.chart_buttons_grid.attach_next_to(self.chart_frame ,
                                                self.button_frame,
                                                Gtk.PositionType.RIGHT,
                                                100,
                                                100)
        self.main_box.add(self.chart_buttons_grid)

        self.button_grid = Gtk.Grid()

        self.button_frame.add(self.button_grid)

        self.button_panel_init()
    
    def button_panel_init(self):
        
        print("dfsddsgfvsdfgdfsgdsfgdsfg")
        self.start_button()
        
        self.stop_button()
        
        self.button_grid.add(self.start_button_)
        
        self.button_grid.attach_next_to(self.stop_button_,self.start_button_,Gtk.PositionType.BOTTOM,2,2)

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

    
    def init_menu_bar(self):

        self.create_ui_menager()


        self.menubar = self.uimanager.get_widget("/MenuBar")
        
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        
        box.pack_start(self.menubar, False, False, 0)

        self.menu_box.add(box)
    def create_ui_menager(self):
        
        self.uimanager = Gtk.UIManager()

        self.uimanager.add_ui_from_file('XML/Menu_bar.xml')
   
        accelgroup = self.uimanager.get_accel_group()

        self.add_accel_group(accelgroup)

        action_group = Gtk.ActionGroup("my_actions")
        
        self.add_file_menu_actions(action_group)

        self.uimanager.insert_action_group(action_group)

    def add_file_menu_actions (self, action_group):
        action_filemenu = Gtk.Action("FileMenu", "File", None, None)
        action_group.add_action(action_filemenu)

        action_filenewmenu = Gtk.Action("LoadXml", None, None, Gtk.STOCK_NEW)
        action_group.add_action(action_filenewmenu)
        
    def show_message(self,return_tuple):

        message_dialog = None

        if len(return_tuple) < 2:
            print("zły format ")
        else:
            message_dialog = Gtk.MessageDialog(parent=self,
                                          flags=Gtk.DialogFlags.MODAL,
                                          type=Gtk.MessageType.WARNING,
                                          buttons=Gtk.ButtonsType.OK_CANCEL,
                                          message_format=return_tuple[1]   )
        
        
        
        message_dialog.connect("response", self.destroy_message_box)

        message_dialog.show()

        

    def destroy_message_box(self,widget,response_id):
        widget.destroy()

