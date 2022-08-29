from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from servico import Servico

class Tela(MDFloatLayout):
    def sortearLista(self):
        result = self.ids.lista.text.split("\n")
        result = Servico.sortear(result)
        self.ids.lb.text = result

class App(MDApp):
    pass

if __name__ == "__main__":
    App().run()