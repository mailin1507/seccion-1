#Cree un programa que lea el monto de un préstamo y el plazo en meses,
#  y muestre al usuario el valor las cuotas mensuales pagando un interés fijo del 2.7% mensual. 
prestamo=int(input("ingrese el monto del prestamo"))
mesesdeplazo=int(input("ingrese el plazo en meses"))
cuotaconinteres=(prestamo*0.027)
cuotasmensuales=prestamo+cuotaconinteres
print("su cuota mensual es "+str(cuotasmensuales))