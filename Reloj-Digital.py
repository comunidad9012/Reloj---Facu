from tkinter import Label, Tk
from time import strftime


ventana = Tk()
ventana.title("RELOJ DIGITAL")
ventana.config(bg="white")
ventana.geometry('300x250')
ventana.minsize(width=250, height=200)
        
ventana.columnconfigure(0, weight=5)
ventana.rowconfigure(0, weight=5)

ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)

ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(2, weight=1)
        
    

def obtener_datos():

    hora = strftime('%H:%M:%S')
    dia = strftime('%A')
    fecha = strftime('%d - %m - %Y')
        
    x = texto_hora.winfo_height()
    t = int((x)*0.30)

    if dia=='Monday':
        dia = 'Lunes'
    
    elif dia=='Tuesday':
        dia = 'Martes'
    
    elif dia=='Wednesday':
        dia = 'Miercoles'

    elif dia=='Thursday':
        dia = 'Jueves'
    
    elif dia=='Friday':
        dia = 'Viernes'

    elif dia=='Saturday':
        dia = 'Sabado'

    elif dia=='Sunday':
        dia = 'Domingo'

    texto_hora.config(text=hora, font= ('Century Gothic', t))
    texto_dia.config(text=dia)
    texto_fecha.config(text = fecha)

    texto_hora.after(1000, obtener_datos)

texto_hora= Label(ventana, fg='aqua', bg='white')
texto_hora.grid(row=0, sticky="nsew")

texto_dia = Label(ventana, fg= 'black', bg='LIGHT BLUE', font= ('Century Gotic', 24))
texto_dia.grid(row=1, sticky="nsew")

texto_fecha = Label(ventana, fg= 'Red', bg='coral', font= ('Lora', 20, 'bold'))
texto_fecha.grid(row=2, sticky="nsew")    


obtener_datos() 

ventana.mainloop()