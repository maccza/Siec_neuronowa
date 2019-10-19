import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from GUI import MainInterface


interface = MainInterface.MainInterface()
interface.connect('destroy',Gtk.main_quit)
interface.show_all() 
Gtk.main()