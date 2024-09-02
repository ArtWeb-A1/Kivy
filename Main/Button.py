# Base app in python.

import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class NameApp(App): # For change name of app change to 'Your name app'App.

  def build(self):

    fl = FloatLayout(size=(500, 250)) # Layout for place a object.

    def callback(instance):
      print('The button <%s> is being pressed' % instance.text)

    btn = Button(text="hello", pos=(100, 200), size_hint=(.5, .15)) # Make button use: pos=(x, y), to change position button. size_hint=(x%, x%), to change size. text="Your text", to chane text in button.

    btn.bind(on_press=callback) # Bind button to function.

    fl.add_widget(btn) # add widget to screen.

    return fl # Show a all object in layout.

if __name__ == "__main__":
  NameApp().run() # Change this to name of class.
