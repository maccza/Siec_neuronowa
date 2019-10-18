import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
 
class MainInterface(Gtk.Window):
    def __init__(self, *args, **kwargs):
        Gtk.Window.__init__(self)
        self.window_init()
    def window_init(self):
       self.set_size_request(1000,1000)
       self.set_position(Gtk.WindowPosition.CENTER)  

interface = MainInterface()
interface.connect('destroy',Gtk.main_quit)
interface.show_all()
Gtk.main()
       