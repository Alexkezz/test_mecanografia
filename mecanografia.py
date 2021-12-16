import random
from tkinter import *
import time
import threading
from pynput import keyboard

lista_palabras = []

def texto_palabras_lista():
    global lista_palabras
    texto = """
    Yo quiero ser llorando el hortelano
    de la tierra que ocupas y estercolas
    compañero del alma, tan temprano.
    Alimentando lluvias, caracolas
    y órganos mi dolor sin instrumento,
    a las desalentadas amapolas
    daré tu corazón por alimento.
    Tanto dolor se agrupa en mi costado
    que por doler me duele hasta el aliento.
    Un manotazo duro, un golpe helado,
    un hachazo invisible y homicida,
    un empujón brutal te ha derribado.
    No hay extensión más grande que mi herida,
    lloro mi desventura y sus conjuntos
    y siento más tu muerte que mi vida.
    Ando sobre rastrojos de difuntos,
    y sin calor de nadie y sin consuelo
    voy de mi corazón a mis asuntos.
    Temprano levantó la muerte el vuelo,
    temprano madrugó la madrugada,
    temprano estás rodando por el suelo.
    No perdono a la muerte enamorada,
    no perdono a la vida desatenta,
    no perdono a la tierra ni a la nada.
    En mis manos levanto una tormenta
    de piedras, rayos y hachas estridentes
    sedienta de catástrofes y hambrienta.
    Quiero escarbar la tierra con los dientes,
    quiero apartar la tierra parte a parte
    a dentelladas secas y calientes.
    Quiero minar la tierra hasta encontrarte
    y besarte la noble calavera
    y desamordazarte y regresarte.
    Volverás a mi huerto y a mi higuera:
    por los altos andamios de las flores
    pajareará tu alma colmenera
    de angelicales ceras y labores.
    Volverás al arrullo de las rejas
    de los enamorados labradores.
    Alegrarás la sombra de mis cejas,
    y tu sangre se irá a cada lado
    disputando tu novia y las abejas.
    Tu corazón, ya terciopelo ajado,
    llama a un campo de almendras espumosas
    mi avariciosa voz de enamorado.
    A las aladas almas de las rosas
    del almendro de nata te requiero,
    que tenemos que hablar de muchas cosas,
    compañero del alma, compañero 
    """
    palabra = ""
    for i in texto:
        if i != "." and i != " " and i != "," and i != "\n" and i != "" and i != '' and i != ":":
            palabra += i
        else:
            if palabra != "":
                lista_palabras.append(palabra)
                palabra = ""
            
texto_palabras_lista()

def palabra_aleatoria():
    indice_palabra = random.randrange(0, len(lista_palabras))
    palabra = lista_palabras[indice_palabra]
    return palabra

root = Tk()
root.title("TEST DE MECANOGRAFIA")
root.resizable(0, 0)

mi_frame = Frame(root, bg="#a8ffff")
mi_frame.pack()

#METODOS---------------------------------------------------------------

txt_entry = StringVar()
validador_primera_vez = 0

def comienzo_juego_tiempo():
    global validador_primera_vez
    global finalizar
    numero_segundos = 59
    numero_minutos = 1
    if validador_primera_vez == 0:
        segundos.config(text=numero_segundos)
        numero_minutos -= 1
        minutos.config(text=numero_minutos)
        validador_primera_vez = 1
    while True:
        numero_segundos -= 1
        time.sleep(1)
        if numero_segundos < 10:
            segundos.config(text="0"+str(numero_segundos))
        else:
            segundos.config(text=numero_segundos)
        if numero_segundos == 0:
            numero_minutos -= 1
            if numero_minutos == -1:
                texto_pantalla.config(text="Has acertado {} palabras".format(numero_aciertos))
                finalizar = 1
                break
            minutos.config(text=numero_minutos)
            numero_segundos = 59
            segundos.config(text=numero_segundos)
            
validator_of_thread = 0 

def new_thread():
    global validator_of_thread
    if validator_of_thread == 0:
        thread1 = threading.Thread(target=comienzo_juego_tiempo)
        thread2 = threading.Thread(target=keylogger)
        thread1.setDaemon(True)
        thread2.setDaemon(True)
        thread1.start()
        thread2.start()
        test_mecanograifa()
        validator_of_thread = 1

def test_mecanograifa():
    global numero_palabra
    global palabra_fuera
    mi_palabra = palabra_aleatoria()
    palabra_fuera = mi_palabra
    texto_pantalla.config(text=mi_palabra)

palabra_fuera = ""
numero_aciertos = 0

def resolution_word():
    global palabra_fuera
    global numero_aciertos
    my_word = entrada_texto.get()
    if my_word == palabra_fuera:
        numero_aciertos += 1
        entrada_texto.delete(0, END)
    else:
        entrada_texto.delete(0, END)

validator_test = 0
finalizar = 0

def keylogger():
    def on_press(key):
        global validator_test
        if key == keyboard.Key.space:
            if finalizar == 0:
                resolution_word()
                test_mecanograifa()
            else:
                pass

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  
   
#ESTRUCTURA TKINTER----------------------------------------------------

texto_principal = Label(mi_frame, text="Escribe el numero de palabras\n en el menor tiempo posible!", font=("Noto Mono", 30), bg="#c6b8e9", relief="raised")
texto_principal.grid(row=0, column=0, columnspan=1, pady=(10, 50), padx=10)

texto_pantalla = Label(mi_frame, text="Palabra", font=("Calibri",30), relief="flat", bg="#a8ffff")
texto_pantalla.grid(row=1, column=0, columnspan=1, pady=(40, 200))

entrada_texto = Entry(mi_frame, font=("Calibri", 20), width=30, justify="center", textvariable=txt_entry)
entrada_texto.place(y=400, x=150)

boton_empezar = Button(mi_frame, text="EMPEZAR", font=("Calibri", 14), command=lambda:new_thread())
boton_empezar.place(y=398, x=575)

minutos = Label(mi_frame, text="1", font=("Calibri", 30), bg="#a8ffff")
minutos.place(x=632, y=200)

dos_puntos = Label(mi_frame, text=":", font=("Calibri", 30), bg="#a8ffff")
dos_puntos.place(x=655, y=200)

segundos = Label(mi_frame, text="00", font=("Calibri", 30), bg="#a8ffff",)
segundos.place(x=670, y=200)

root.mainloop()