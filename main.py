import keyboard
from tkinter import *
from tkinter import ttk

#cores

cor1 = "#1a1a1a"
cor2 = "#333333"
cor3 = "#fa6a02"
cor4 = "#ffffff"

#config janela

janela = Tk()
janela.title("Calculadora")
janela.geometry("237x316")
janela.config(bg = cor1)

#frames

frame_tela = Frame(janela, width = 237, height = 50, bg = cor2)
frame_tela.grid(row = 0, column = 0)

frame_corpo = Frame(janela, width = 237, height = 266, bg = cor1)
frame_corpo.grid(row = 1, column = 0)

#label

valor = StringVar()

app_label = Label(frame_tela, textvariable = valor, width = "16", height = "2", padx = 7, font = "Arial 18",relief = FLAT, anchor = "e", justify = RIGHT, bg = cor2, fg = cor4)
app_label.place(x = 0, y = 0)

valores = ""

#entrada de texto

def entrar_valor(event):
    
    global valores

    valores = valores + str(event)

    #passar valor para tela
    valor.set(valores)

#calculadora

def calculadora():

    global valores

    resultado = eval(valores)
    valor.set(int(resultado))

#limpar tela

def clear():
    
    global valores

    valores = ''
    valor.set('')

#botoes

btn_clear = Button(frame_corpo, command = clear, text="C", width = 16, height = 3, bg = cor1, fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_clear.place(x = 0, y = 0)

btn_prct = Button(frame_corpo, command = lambda: entrar_valor('%'), text="%", width = 7, height = 3, bg = cor1, fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_prct.place(x = 119, y = 0)

btn_div = Button(frame_corpo, command = lambda: entrar_valor('/'), text="/", width = 7, height = 3, bg = cor3,  fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_div.place(x = 179, y = 0)

btn_7 = Button(frame_corpo, command = lambda: entrar_valor('7'), text="7", width = 7, height = 3, bg = cor1, fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_7.place(x = 0, y = 57)

btn_8 = Button(frame_corpo, command = lambda: entrar_valor('8'), text="8", width = 7, height = 3, bg = cor1,  fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_8.place(x = 59, y = 57)

btn_9 = Button(frame_corpo, command = lambda: entrar_valor('9'), text="9", width = 7, height = 3, bg = cor1, fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_9.place(x = 119, y = 57)

btn_multi = Button(frame_corpo, command = lambda: entrar_valor('*'), text="*", width = 7, height = 3, bg = cor3,  fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_multi.place(x = 179, y = 57)

btn_4 = Button(frame_corpo, command = lambda: entrar_valor('4'), text="4", width = 7, height = 3, bg = cor1, fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_4.place(x = 0, y = 113)

btn_5 = Button(frame_corpo, command = lambda: entrar_valor('5'), text="5", width = 7, height = 3, bg = cor1,  fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_5.place(x = 59, y = 113)

btn_6 = Button(frame_corpo, command = lambda: entrar_valor('6'), text="6", width = 7, height = 3, bg = cor1, fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_6.place(x = 119, y = 113)

btn_sub = Button(frame_corpo, command = lambda: entrar_valor('-'), text="-", width = 7, height = 3, bg = cor3,  fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_sub.place(x = 179, y = 113)

btn_1 = Button(frame_corpo, command = lambda: entrar_valor('1'), text="1", width = 7, height = 3, bg = cor1, fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_1.place(x = 0, y = 169)

btn_2 = Button(frame_corpo, command = lambda: entrar_valor('2'), text="2", width = 7, height = 3, bg = cor1,  fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_2.place(x = 59, y = 169)

btn_3 = Button(frame_corpo, command = lambda: entrar_valor('3'), text="3", width = 7, height = 3, bg = cor1, fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_3.place(x = 119, y = 169)

btn_soma = Button(frame_corpo, command = lambda: entrar_valor('+'), text="+", width = 7, height = 3, bg = cor3,  fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_soma.place(x = 179, y = 169)

btn_0 = Button(frame_corpo, command = lambda: entrar_valor('0'), text="0", width = 16, height = 2, bg = cor1, fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_0.place(x = 0, y = 225)

btn_ponto = Button(frame_corpo, command = lambda: entrar_valor('.'), text=".", width = 7, height = 2, bg = cor1, fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_ponto.place(x = 119, y = 225)

btn_igual = Button(frame_corpo, command = calculadora, text="=", width = 7, height = 2, bg = cor3,  fg = cor4, relief = RAISED, overrelief = RIDGE)
btn_igual.place(x = 179, y = 225)

if keyboard.is_pressed('shift') == True:
    quit()

janela.mainloop()

