productos={
    "manzana":{"precio":1.2,"stock":50}, 
    "banana":{"precio":0.8, "stock":100,}, 
    "leche":{"precio":1.50,"stock":30}
}

producto_buscado=input("Ingresa el producto dque desea consultar: ").lower()

if producto_buscado in productos:
    print(f"Precio: € {productos[producto_buscado]['precio']} \nStock disponible: {productos[producto_buscado]['stock']} unidades")
else:
    print("Producto no encontrado")