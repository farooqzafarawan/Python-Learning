import kivy
#kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.label import Label

class Sample(App):
   # display content on screen
   def build(self):
    # Return a label widget with Sample
    return Label(text ="Tutorialpoint")

sample = Sample()
sample.run()