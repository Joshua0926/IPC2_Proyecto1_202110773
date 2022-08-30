from xml.dom import minidom
from xml.etree.cElementTree import parse, Element
from tkinter import filedialog as fd
from Nodo import Paciente 
from listasimple import listasimple
import numpy as np
    
print("Predicción de Enfermedades")
lista = listasimple()
a=input("¿Desea abrir un Archivo? SI/NO")
if a == "SI":
    filename = fd.askopenfilename(initialdir="C:/", title="Select a File", filetypes=(("Text files", "*.xml*"), ("Todos los archivos",".*")))
    docxml = minidom.parse(filename)
    paciente = docxml.getElementsByTagName('paciente')
    for i in paciente:
        nombre = i.getElementsByTagName('nombre')
        edad = i.getElementsByTagName('edad')
        periodo = i.getElementsByTagName('periodos')
        m = i.getElementsByTagName('m')
        rejilla = i.getElementsByTagName('rejilla')
        celda = i.getElementsByTagName('celda') 

        dimensiones = int(m[0].firstChild.data) 
        tabla0=[]
        a = np.zeros((dimensiones, dimensiones))
        for j in rejilla:
            n=0
            for k in celda:
                a[(int(celda[n].attributes['f'].value)-1)][(int(celda[n].attributes['c'].value)-1)]=1
                n+=1
            coord = np.zeros((n, 2))
            p=0
            for l in celda:            
                coord[p][0]=(int(celda[p].attributes['f'].value))
                coord[p][1]=(int(celda[p].attributes['c'].value))
                p+=1
         
           

        lista.insertlast( nombre[0].firstChild.data, edad[0].firstChild.data, periodo[0].firstChild.data, m[0].firstChild.data, coord, a )
    print("Ingrese Nombre de Paciente: ")
    name=input()
    lista.getpacientes(nombre=name)

