import time 
from datetime import date
from datetime import datetime
#podia usar una definicion de variables pero preferi hacerlo manualmente
#tambien no pude configurar manualmente lo de las fiestas sorry

print("""  _     _                           _     _                                         
| |   (_)                         (_)   | |                                        
| |__  _  ___ _ ____   _____ _ __  _  __| | ___                                    
| '_ \| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \                                   
| |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) |                                  
|_.__/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/                                   
         __ _                                                                      
        / _` |                                                                     
       | (_| |                                                                     
        \__,_|                                                                     
______     _ _                                             _                       
| ___ \   | | |                                           | |                      
| |_/ /__ | | | ___  ___    ___ ___  _ __   __ _  ___ __ _| |__   __ _ _ __   __ _ 
|  __/ _ \| | |/ _ \/ __|  / __/ _ \| '_ \ / _` |/ __/ _` | '_ \ / _` | '_ \ / _` |
| | | (_) | | | (_) \__ \ | (_| (_) | |_) | (_| | (_| (_| | |_) | (_| | | | | (_| |
\_|  \___/|_|_|\___/|___/  \___\___/| .__/ \__,_|\___\__,_|_.__/ \__,_|_| |_|\__,_|
                                    | |                                            
                                    |_|                                                   """)

print(""" 
         (o o)   (o o)               
        (  V  ) (  V  ) 
       /--m-m- /--m-m-  """)

print ("la contrasena es [seguro23] es solo para comprobara que eres humano :3")
time.sleep(3)

incresa= "seguro23"
entra=input("incresa la contrasena por default para comprobar que eres humano : ")

while entra!=incresa:
     print("fallaste :c")
     entra=input("incresa la contrasena por default para comprobar que eres humano : ")
else:
	print(" --------- bienvenido disfruta tu compra ---------")

antojito_pie = 7
antojito_helado = 6
combo_antojito =21.5
hamburguesa_doble=26.5
combo_casa= 29.5
hamburguesa_normal = 38





yj="si"
np="no"
hg= input("quieres comprar algo ? :  ")
while hg != yj:
	hg = input("quieres comprar algo ?:   ")
if  hg == np:
	print(" :c okey ")
else:
	(" nuuu eso no esta en el programa ")









print("le explicamos como funciona el programa  usted simplemente incresa la candidad de lo que quiere y si no quiere de ese articulo pone un 0 :3 ")
time.sleep(3)
print("disfrute :3")
time.sleep(4)
print ("""           -------------------------------------------------------------------
           -         ------en nuestro menu tenemos----                       -
           -                                                                 -
           -  pie = 7bs          antojito = 21.5bs   copalito =38.bs         -
           -  combo queso= 26.5bs combo fiesta= 29.6.bs mousse=6.bs          -
           -                                                                 -
           ------------------------------------------------------------------- """) 




pie_b= int(input("cuantos pie's quiere?:   "))
helado = int(input("cuantos mousse quiere?:  "))
comBO= int(input("cuantos antojitos quiere?:"))
hamburguesa_p= int(input(" y como coplitos cuantos? :  "))
casa= int(input ("combo fiesta quieres? :   "))
doble =int(input (" un combo queso quizas?:   "))


tpotal=hamburguesa_p* hamburguesa_normal
jdjdjd=pie_b * antojito_pie 
hjh=helado * antojito_helado
hdhdhd=comBO * combo_antojito 
fff=casa * combo_casa 
jpg= doble * hamburguesa_doble 
total=hamburguesa_p* hamburguesa_normal + pie_b * antojito_pie+comBO * combo_antojito+casa * combo_casa+doble * hamburguesa_doble -15.47
grantotal=hamburguesa_p* hamburguesa_normal + pie_b * antojito_pie+comBO * combo_antojito+casa * combo_casa+doble * hamburguesa_doble




if tpotal <= -1 :
	print("entrada invalida ")
	print("monto",tpotal,"no es valido")
elif jdjdjd <= -1:
	print("entrada invalida ")
	print("monto",jdjdjd,"no es valido")
elif hjh <= -1 :
	print("entrada invalida")
	print("monto",hjh,"no es valido")
elif hdhdhd <= -1 :
	print("entrada invalida ")
	print("monto",hdhdhd,"no es valido")
elif jpg  <= -1 :
	print("entrada invalida ")
	print("monto",jpg ,"no es valido")
elif fff <= -1 :
	print("entrada invalida ")
	print("monto",fff,"no es valido")
elif total <= -1:
	print("tu total es invalido ",total,"vuelve al menu ")
else:
	print("okey algunos items estan bien o todos estan bien ")

print("tu monto a pagar de los copalitos es de ",tpotal,"bs")
print("tu monto a pagar por los antojitos es de ",hdhdhd,"bs")
print("tu monto a pagar por los pies es de",jdjdjd,"bs")
print("tu monto a pagar por los es  mousse de ",hjh,"bs")
print("tu monto a pagar por el combo queso",jpg,"bs")
print("tu monto a pagar por el combo fiesta",fff,"bs")
print ("tu monto TOTAL es de:",total,"bs")

print("_____________________FACTURA___________________________________")
print("-codigo_____________= detalle_____________=debe_____=haber   __-")
print("10001______________= CAJA________________=",grantotal,"     __")
print("20001_______________= debito fiscal_______=______=   15.47   __")
print("40001_______________= ventas______________=_______",total,"   _")
print("____________________________________________",total,"__",total,"-")





today = date.today()
now = datetime.now()
print (today)
print (now)
print ("su compra se esta reguistrando en {}".format(today.day))
print("el mes de la compra es en {}".format(today.month))
print("el año actual de tu compra es {}".format(today.year))
print("la hora actual es {}".format(now.hour))
print("el minuto actual es {}".format(now.minute))
print("el segundo actual es {}".format(now.second))


print("lo hice con mi mayor esfuerzo espero que sirva de algo :')   ")
print("hecho por  kerne34")




