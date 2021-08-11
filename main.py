import socket
from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
import functions

Window.clearcolor = (0, 0, 0, 1)




class AppScreen(Widget):
    pass

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        # creates a Grid Layout with 2 columns and 2 rows
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 2 
        self.rows = 2
        #Creates a button and binds it to the lookup method that follows the __init__
        self.ip_lookup_button = Button(text= 'WhoIs lookup', font_size = 32)
        self.ip_lookup_button.bind(on_press = self.lookup)
        self.add_widget(self.ip_lookup_button)
        #this adds the text input space 
        self.url_input = TextInput(multiline = False, text= '')
        self.add_widget(self.url_input)
        
    # this method calls the functions imported from the module and prints in a Label widget the results
    def lookup(self, instance):
        try:
            url = self.url_input.text
            get_ip = functions.ip_from_url(str(url))
            result_who_is = functions.who_is(get_ip)
            self.add_widget(Label(text = str(result_who_is)))
        except:
            self.add_widget(Label(text = 'Invalid URL'))
        #this line clears the input after pushing the button
        self.url_input.text = '' 

        

class IP_Tool(App):
    def build(self):
        return MyGridLayout()
        

if __name__ == '__main__':
    IP_Tool().run()