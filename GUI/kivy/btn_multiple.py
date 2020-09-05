from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class CalcApp(App):
    def build(self):
        layout = BoxLayout( orientation='horizontal')
        btn_scan = Button(text='Scan Disk', font_size ="20sp",
                    background_color =(2, 1, 2, 1), height=100)  # use (r, g, b, a) tuple for color
        btn_format = Button(text='Format Disk', font_size ="20sp",
                    background_color =(1, 0, 2, 1), height=100)

      

        layout.add_widget(btn_scan)
        layout.add_widget(btn_format)

        return layout

mainApp = CalcApp()  
mainApp.run()