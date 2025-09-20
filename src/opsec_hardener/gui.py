import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class OpsecHardener(Gtk.Window):
    def __init__(self):
        super().__init__(title="Opsec Hardener")
        self.set_default_size(600, 400)

        notebook = Gtk.Notebook()
        self.add(notebook)

        notebook.append_page(Gtk.Label(label="System Snapshots"), Gtk.Label(label="Snapshots"))
        notebook.append_page(Gtk.Label(label="Network Hardening"), Gtk.Label(label="Network"))
        notebook.append_page(Gtk.Label(label="Monitoring"), Gtk.Label(label="Monitoring"))
        notebook.append_page(Gtk.Label(label="Logs & Config"), Gtk.Label(label="Logs"))

def main():
    win = OpsecHardener()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
