from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
import socket
import whois


Window.clearcolor = (0, 0, 0, 1)
Window.size = (400, 600)

class AppScreen(Widget):
    pass

class IP_Tool(App):
    def build(self):
        layout = GridLayout(rows = 2)
        self.url_input = TextInput(text= 'Enter URL')
        self.ip_lookup_button = Button(text = 'WhoIs lookup', on_press = self.ip_Lookup)
        layout.add_widget(self.url_input)
        layout.add_widget(self.ip_lookup_button)
        return layout
        #this method should get an IP number from a URL and then lookup through the whois 
    def ip_Lookup(self, who_is = None):
        self.who_is = who_is
        try:
            self.url = str(self.url_input)
            self.ip_address = socket.gethostbyname(self.url)
            self.who_is = whois.whois(self.ip_address)
            return self.who_is
        except Exception:
            print ()
        



if __name__ == '__main__':
    IP_Tool().run()