from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class CalculatorApp(App):
    def calculate_result(self, instance):
        try:
            result = eval(self.input_field.text)
            self.result_label.text = str(result)
        except:
            self.result_label.text = "ТАК НЕЛЬЗЯ"
