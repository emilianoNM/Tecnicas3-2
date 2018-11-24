#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
digitos = (’0’,’1’,’2’,’3’,’4’,’5’,’6’,’7’,’8’,’9’)
codigo = ’’
for i in range(4):
        candidato = random.choice(digitos)
        while candidato in codigo:
            candidato = random.choice(digitos)
        codigo = codigo + candidato
        
print "Bienvenido/a al Mastermind!"
print "Tenes que adivinar un numero de", 4, "cifras distintas"
propuesta = raw_input("Que codigo propones?: ")
intentos = 1
while propuesta != codigo:
        intentos = intentos + 1
        aciertos = 0
        coincidencias = 0

        for i in range(4):
                if propuesta[i] == codigo[i]:
                        aciertos = aciertos + 1
                elif propuesta[i] in codigo:
                        coincidencias = coincidencias + 1
        print "Tu propuesta (", propuesta, ") tiene", aciertos,         "aciertos y ", coincidencias, "coincidencias."

        propuesta = raw_input("Propone otro codigo: ")

        print "Felicitaciones! Adivinaste el codigo en", intentos, "intentos."

