from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 700)
Config.set('graphics', 'height', 900)


class CalculatorApp(App):  # создаем класс BoxApp и наследуем от App
    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if (self.formula == "0"):
            self.formula = ""
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if(str(instance.text).lower()=="x"):
            self.formula += "*"
        else:
            self.formula += str(instance.text)
        self.update_label()

    def calc_result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = "0"

    def build(self):  # создаем метод build с параметром self
        self.formula = '0'
        bl = BoxLayout(orientation='vertical')
        gl = GridLayout(cols=4, padding=5, spacing=5)
        self.lbl = Label(text='0', font_size=70, size_hint=(1, .4), halign='right',text_size=(690, 900*.4-100))

        bl.add_widget(self.lbl)

        gl.add_widget(Button(text='7', font_size=40, on_press=self.add_number))
        gl.add_widget(Button(text='8', font_size=40, on_press=self.add_number))
        gl.add_widget(Button(text='9', font_size=40, on_press=self.add_number))
        gl.add_widget(Button(text='x', font_size=40, on_press=self.add_operation))

        gl.add_widget(Button(text='4', font_size=40, on_press=self.add_number))
        gl.add_widget(Button(text='5', font_size=40, on_press=self.add_number))
        gl.add_widget(Button(text='6', font_size=40, on_press=self.add_number))
        gl.add_widget(Button(text='-', font_size=40, on_press=self.add_operation))

        gl.add_widget(Button(text='1', font_size=40, on_press=self.add_number))
        gl.add_widget(Button(text='2', font_size=40, on_press=self.add_number))
        gl.add_widget(Button(text='3', font_size=40, on_press=self.add_number))
        gl.add_widget(Button(text='+', font_size=40, on_press=self.add_operation))

        gl.add_widget(Widget())
        gl.add_widget(Button(text='0', font_size=40, on_press=self.add_number))
        gl.add_widget(Button(text='.', font_size=40, on_press=self.add_operation))
        gl.add_widget(Button(text='=', font_size=40, on_press=self.calc_result))

        bl.add_widget(gl)
        return bl

if __name__ == "__main__":  # проверяем что имя модуля main
    CalculatorApp().run()  # создаем экземляр класса BoxApp и вызываем метод run (унаследован от класса App)
