# Kivy Installment

```python
pip install kivy
```

## Requirements
```python
py -m pip install --upgrade pip wheel setuptools
py -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew

```

# Kivy Widgets
Let us take a look at various kivy widgets. The kivy widgets can be categorized in the following manner.
- UX Widgets
- Layouts
- Complex UX Widgets
- Behavior Widgets
- Screen Manager

# UX Widgets
- Label
- Button
- Checkbox
- Image
- Slider
- Progress Bar
- Text Input
- Toggle Button
- Switch
- Video

## Label
The label widget is used for rendering text. It supports both ascii and unicode strings. Here is a simple example to show how we can use label widget in our application.
```python
from kivy.app import App
from kivy.uix.label import Label
 
 
class SimpleApp(App):
    def build(self):
        l = Label(text="Edureka!",font_size=150)
        return l
 
 
if __name__ == "__main__":
    SimpleApp().run()
```

## Button
The button is a label with actions that get triggered when a button is pressed. To configure a button, the same settings are used as that of a label. Here is a simple example to show the button widget. It changes state when clicked, and we can even add properties or bind some actions to the button as well.

```python
from kivy.app import App
from kivy.uix.button import Button
 
 
class SimpleApp(App):
    def build(self):
        def a(instance,value):
            print("welcome to edureka")

        btn = Button(text="Edureka!",font_size=150)
        btn.bind(state=a)

        return btn
 
if __name__ == "__main__":
    SimpleApp().run()
```

# Progress Bar
It is used to track the progress of any task. Here is a simple example to show how we use a progress bar in a kivy application.

```python
from kivy.app import App
from kivy.uix.progressbar import ProgressBar
 
 
class SimpleApp(App):
    def build(self):
        Progress  = ProgressBar(max=1000)
        Progress.value = 650
        return Progress
 
 
if __name__ == "__main__":
    SimpleApp().run()
```

# Image
This widget is used to display an image. When you run this program, it will show an image in the application.

```python
from kivy.app import App
from kivy.uix.image import Image
 
 
class SimpleApp(App):
    def build(self):
        img = Image(source="logo.png")
        return img
 
 
if __name__ == "__main__":
    SimpleApp().run()
```

# Slider
The slider widget supports horizontal and vertical orientations and is used as a scrollbar. Here is a simple example to show a slider in a kivy application.
```python
from kivy.app import App
from kivy.uix.slider import Slider
 
 
class SimpleApp(App):
    def build(self):
        slide = Slider(orientation='vertical', value_track=True, value_track_color=(1,0,0,1))
        return slide
 
 
if __name__ == "__main__":
    SimpleApp().run()
```

# Video
It is used to display video files or streams. Here is a simple example to show how it works in a kivy app.

```python
from kivy.app import App
from kivy.uix.video import Video
 
 
class SimpleApp(App):
    def build(self):
 
        s = Video(source="abc.mp4", play=True)
        return s
 
 
if __name__ == "__main__":
    SimpleApp().run()
```
Output: It will play the video given in the file link.

# Layouts
A layout widget does no rendering but just acts as a trigger that arranges its children in a specific way.
- Anchor Layout
- Box Layout
- Float Layout
- Grid Layout
- Page Layout
- Relative Layout
- Scatter Layout
- Stack Layout
  
## Anchor Layout
It aligns the child widgets to a border(left, right, up, down) or center. Here is a simple example to show how anchor layout is used in a kivy application when the anchor is set to center position, we can set it to different positions like bottom-left, bottom-up, etc.

```python
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
 
 
class SimpleApp(App):
    def build(self):
        layout = AnchorLayout(
            anchor_x='center', anchor_y='center')
        btn = Button(text='Hello World')
        layout.add_widget(btn)
        return layout
 
 
if __name__ == "__main__":
    SimpleApp().run()
```

## Box Layout
It arranges the child widgets in horizontal or vertical boxes. In the example, the box layout stores the widgets in the two boxes as shown below.
```python
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
 
 
class SimpleApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn = Button(text='Hello World')
        btn1 = Button(text="Welcome to edureka")
        layout.add_widget(btn)
        layout.add_widget((btn1))
        return layout
 
if __name__ == "__main__":
    SimpleApp().run()
```

## Float Layout
It honors the size_hint and pos_hint properties of its child widgets.

```python
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
 
 
class SimpleApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text="Edureka!", font_size=150)
 
        f.add_widget(s)
        s.add_widget(l)
        return f
 
 
if __name__ == "__main__":
    SimpleApp().run()
```