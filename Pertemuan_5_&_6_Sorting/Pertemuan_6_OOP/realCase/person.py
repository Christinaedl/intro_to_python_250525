from abc import ABC, abstractclassmethod

class person (ABC) :
    def __init__(self, nama, usia):
        self.nama = nama
        self._usia = usia
    def getDetail(self):
        pass
    def getUsia(self):
        return f"{self._usia}"
    
    def setUsia(self, usia):
        if usia != 0 :
            self.__usia = usia
        else:
            raise ValueError("umur tidak bernilai")