from abc import ABC, abstractclassmethod

class Hewan(ABC) :
    @abstractclassmethod
    def suara(self):
        print("Ini punya hewan")

class Kucing(Hewan):
    def suara(self):
        print("Meow!!!!")

Tom = Kucing()
Tom.suara()
