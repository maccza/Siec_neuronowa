import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import multiprocessing as multi

from GUI import MainInterface


def main():
    interface = MainInterface.MainInterface()
    interface.connect('destroy', Gtk.main_quit)
    interface.show_all()
    Gtk.main()


if __name__ == '__main__':
    main_process = multi.Process(target=main)
    main_process.start()
    main_process.join()
