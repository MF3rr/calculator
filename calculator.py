from tkinter import *
from math import *

# OPERACOES
def btnClik(num):
    global operator
    operator=operator+str(num)
    input_text.set(operator)
    
# APRESENTA O RESULTADO
def result():
    global operator
    try:
        opera=str(eval(operator))
        input_text.set(opera)
    except:
        input_text.set("ERROR")
    operator = ""
 
# LIMPA A TELA
def clear():
    global operator
    operator=("")
    input_text.set("0")

# CRIANDO JANELA PRINCIPAL
root = Tk()
root.title('CALCULATOR')
root.geometry("392x600")
#root.configure(background= "SkyBlue4" ) # configura cor
operator = ""

input_text=StringVar()

# CONFIGURACOES DE TELA
Display=Entry(root,font=('arial',20,'bold'),width=22,
textvariable=input_text,bd=20,insertwidth=4,bg="powder blue",justify="right")
Display.place(x=10,y=60)

# BOTOES
Button(root,text="0",bg="gray77",width=11,height=3,command=lambda:btnClik(0)).place(x=17,y=180)
Button(root,text="1",bg="gray77",width=11,height=3,command=lambda:btnClik(1)).place(x=107,y=180)
Button(root,text="2",bg="gray77",width=11,height=3,command=lambda:btnClik(2)).place(x=197,y=180)
Button(root,text="3",bg="gray77",width=11,height=3,command=lambda:btnClik(3)).place(x=287,y=180)
Button(root,text="4",bg="gray77",width=11,height=3,command=lambda:btnClik(4)).place(x=17,y=240)
Button(root,text="5",bg="gray77",width=11,height=3,command=lambda:btnClik(5)).place(x=107,y=240)
Button(root,text="6",bg="gray77",width=11,height=3,command=lambda:btnClik(6)).place(x=197,y=240)
Button(root,text="7",bg="gray77",width=11,height=3,command=lambda:btnClik(7)).place(x=287,y=240)
Button(root,text="8",bg="gray77",width=11,height=3,command=lambda:btnClik(8)).place(x=17,y=300)
Button(root,text="9",bg="gray77",width=11,height=3,command=lambda:btnClik(9)).place(x=107,y=300)
Button(root,text="π",bg="gray77",width=11,height=3,command=lambda:btnClik("pi")).place(x=197,y=300)
Button(root,text=",",bg="gray77",width=11,height=3,command=lambda:btnClik(".")).place(x=287,y=300)
Button(root,text="+",bg="gray77",width=11,height=3,command=lambda:btnClik("+")).place(x=17,y=360)
Button(root,text="-",bg="gray77",width=11,height=3,command=lambda:btnClik("-")).place(x=107,y=360)
Button(root,text="*",bg="gray77",width=11,height=3,command=lambda:btnClik("*")).place(x=197,y=360)
Button(root,text="/",bg="gray77",width=11,height=3,command=lambda:btnClik("/")).place(x=287,y=360)
Button(root,text="√",bg="gray77",width=11,height=3,command=lambda:btnClik("sqrt(")).place(x=17,y=420)
Button(root,text="(",bg="gray77",width=11,height=3,command=lambda:btnClik("(")).place(x=17,y=480)
Button(root,text=")",bg="gray77",width=11,height=3,command=lambda:btnClik(")")).place(x=107,y=480)
Button(root,text="%",bg="gray77",width=11,height=3,command=lambda:btnClik("%")).place(x=197,y=480)
Button(root,text="ln",bg="gray77",width=11,height=3,command=lambda:btnClik("log(")).place(x=287,y=480)
Button(root,text="C",bg="gray77",width=11,height=3,command=clear).place(x=107,y=420)
Button(root,text="EXP",bg="gray77",width=11,height=3,command=lambda:btnClik("**")).place(x=197,y=420)
Button(root,text="=",bg="gray77",width=11,height=3,command=result).place(x=287,y=420)

 
root.mainloop()
