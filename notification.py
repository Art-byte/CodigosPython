from win10toast import ToastNotifier

toaster = ToastNotifier()
tiempo = int(input("Ingresa un numero por favor"))
index = 0

while(index<=tiempo):
    #show notification 
    toaster.show_toast("Notificacion desde python", 
                        "Saludos Arturo Pedraza",
                        threaded = True,
                        icon_path = None,
                        duration = 10)
    index += 1
    break

import time 
while toaster.notification_active():
    time.sleep(0.1)
