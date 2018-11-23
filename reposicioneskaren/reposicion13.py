def maxlitros(presupuesto,plastico, vidrio, reembolso):
     if plastico-reembolso<plastico:
        res= max((presupuesto-reembolso)//(vidiro-reembolso),0)
        presupuesto-=res*(vidrio-reembolso)
        res+= presupuesto//plastico
        print(res)
      else:
        print(presupuesto//plastico)
presupuesto,plastico,vidrio, reembolso= 10,11,9,8
maxlitros(presupuesto,plastico,vidrio,reembolso)
