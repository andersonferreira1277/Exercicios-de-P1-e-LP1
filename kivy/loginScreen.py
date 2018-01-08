#!/usr/bin/env python3
# -*- coding: utf-8-*-

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyLayout(GridLayout):

    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.cols=2

        self.add_widget(Label(text='User name'))

        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password'))

        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)


class MyApp(App):

    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()

