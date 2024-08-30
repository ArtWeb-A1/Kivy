# Base app in python.

import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class NameApp(App): # For change name of app change to 'Your name app'App.

  def build(self):

    fl = FloatLayout(size=(500, 250)) # Layout for place a object.

    return fl # Show a all object in layout.

if __name__ == "__main__":
  NameApp().run() # Change this to name of class.
