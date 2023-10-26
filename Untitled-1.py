from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class CalculatorApp(App):
    def calculate_result(self, instance):
        try:
            result = eval(self.input_field.text)
            self.result_label.text = str(result)
        except:
            self.result_label.text = "ТЫ ТУПОЙ ТАК НЕЛЬЗЯ"

    def build(self):
        layout = GridLayout(cols=4)

        self.input_field = Button(text='', font_size=30)
        layout.add_widget(self.input_field)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        for button_text in buttons:
            button = Button(text=button_text, font_size=30)
            button.bind(on_press=self.button_pressed)
            layout.add_widget(button)

        self.result_label = Button(text='', font_size=30)
        layout.add_widget(self.result_label)

        return layout

    def button_pressed(self, instance):
        current_text = self.input_field.text
        button_text = instance.text

        if button_text == '=':
            self.calculate_result(instance)
        else:
            self.input_field.text = current_text + button_text


if __name__ == '__main__':
    CalculatorApp().run()