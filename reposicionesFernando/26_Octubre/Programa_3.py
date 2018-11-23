#Este Programa convierte decimal a binario usando recursion

def ConvertiraBinario(n):
   
   if n > 1:
       ConvertiraBinario(n//2)
   print(n % 2,end = '')

dec = 34

ConvertiraBinario(dec)