
import GUI.MainInterface as MainInterface

if __name__ == 'name':
    interface = MainInterface()
    interface.connect('destroy',Gtk.main_quit)
    interface.show_all()    
    Gtk.main()
       