class Paciente():
    def __init__(self,nombre,edad,periodos,m, infectadas, tabla0):
        self.nombre=nombre
        self.edad=edad
        self.periodos=periodos
        self.m=m
        self.infectadas=infectadas
        self.tabla0=tabla0
        self.tableros=None
        self.next=None
    def getsig(self):
        return self.next
    def setsig(self, next):
        self.siguiente=next       