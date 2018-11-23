#Este programa te dice si es que con los valores intrducidos es posible realizar un triangulo


print("Ingrese sus tres valores tipo float")
x=float(input("Primer valor\n"))
y=float(input("Segundo valor\n"))
z=float(input("Tercer valor\n"))


# In[3]:


if((x+y)>z): 
    condicion=1 
elif(): 
    condicion=0 
if((x+z)>y):
    condicion=condicion+1 
elif(): 
    condicion=0 

if((y+z)>x): 
    condicion=condicion+1 
elif():
    condicion=0

if(condicion==3): 
print("SI EXISTE UN TRIANGULO CON ESTOS VALORES")