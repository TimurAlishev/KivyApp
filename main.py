from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class BoxApp(App):  # создаем класс BoxApp и наследуем от App
    def build(self):  # создаем метод build с параметром self
        bl = GridLayout(cols=10, padding=10, spacing=5)  # присваиваем методу BoxLayout переменную bl
        for x in range(50):
            bl.add_widget(Button(text='X'))  # вызываем метод add_widget с кнопкой и текстом
        return bl  # возвращаем переменную bl


if __name__ == "__main__":  # проверяем что имя модуля main
    BoxApp().run()  # создаем экземляр класса BoxApp и вызываем метод run (унаследован от класса App)
