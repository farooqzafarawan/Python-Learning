from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class CalcApp(App):
    def build(self):
        layout = BoxLayout( orientation='horizontal')
        btn_scan = Button(text='Scan Disk', font_size ="20sp",
                    background_color=(2, 1, 2, 1))  # use (r, g, b, a) tuple for color
        btn_format = Button(text='Format Disk', font_size ="20sp",
                    background_color=(1, 0, 2, 1))

        btn_scan.bind(on_press=self.onPress_scan)
        btn_format.bind(on_press=self.onPress_format)

        layout.add_widget(btn_scan)
        layout.add_widget(btn_format)

        return layout

    def onPress_scan(self, instance):
        print('You pressed Scan Disk button!')

    def onPress_format(self, instance):
        print('You pressed Format button!')


mainApp = CalcApp()  
mainApp.run()