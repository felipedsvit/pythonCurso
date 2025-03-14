#variables
esEstudiante = input("¿Estudiais nene? (sí/no): ").lower() =="sí"
esJubilado=input("Es jubileta? (sí/no): ").lower() =="sí"

#conndicional
if esEstudiante or esJubilado:
    print("Puedes accender al descuento.")
else:
    print("No puedes accender al descuento.")