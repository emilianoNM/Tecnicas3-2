def addNodo(self,nodo):
aux=self._raiz_
aux1=aux.gethijos
if len(aux1<2):
 aux1.addHijo(nodo)
hijois=aux1.getHijos()
for i in hijois:
    if i.esHoja():
       hijois.addHijo(nodo)
        return
          for i in hijois:
            if len(i.getHijos()!=2):
               hijois.addHijo(nodo)
                return

