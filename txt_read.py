from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
def read_text_and_display(filename, widget):
    with open(filename, "r") as f:
        text = f.read()
    widget.text = text

    def update_widget(dt):
        with open(filename, "r") as f:
            new_text = f.read()
        widget.text = new_text

    Clock.schedule_interval(update_widget, 1)

class MyApp(App):
    def build(self):
        label = Label()
        read_text_and_display("text.txt", label)
        return label

if __name__ == "__main__":
    MyApp().run()