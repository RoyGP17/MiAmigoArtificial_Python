import pyautogui as pg, webbrowser as web, time as tm
def WhatsApp():
    mensajes = int(input("¿Cuantos mensajes desea enviar?: "))
    web.open("https://web.whatsapp.com/send?phone=+51922322343")
    for i in range(mensajes):
        pg.write("Hola buenos dias")
        pg.press('enter')
        tm.sleep(10)
