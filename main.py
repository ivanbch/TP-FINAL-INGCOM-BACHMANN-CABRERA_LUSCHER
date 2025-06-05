import random                         #
import string                         #
from datetime import date, timedelta  #estas cosas son sólo de "adorno", para generar porcentajes de descuentos vip y fechas de vencimiento realistas

def datos_basicos(nom,ap,dni,tel,dom,emp,tel_lab,dom_lab) :
    datos_basicos = {
        "nombre": nom,
        "apellido": ap,
        "dni": dni,
        "tel": tel,
        "dom": dom,
        "empr": emp,
        "tel_lab": tel_lab,
        "dom_lab": dom_lab
    }
    return datos_basicos

def turista (origen,hotel_agencia) :
    if "internacional" in origen :
        org = "internacional"
    else :
        org = "nacional"
    turista = {
        "origen": org,
        "hotel": hotel_agencia
    }
    return turista

def tipo_tarifa (n) : #esto es como el "molde" de una tarifa
    tarifas = [
        {"cod": "", "nom": "", "tipo": "diaria", "importe": 9000, "Bariloche": False},
        {"cod": "", "nom": "", "tipo": "finde", "importe": 15000, "Bariloche": False},
        {"cod": "", "nom": "", "tipo": "semana", "importe": 20000, "Bariloche": False},
        {"cod": "", "nom": "", "tipo": "mes_mas", "importe": 35000, "Bariloche": False}   
    ]
    return tarifas[n]

def crear_tarifa (tipo,vehiculo,temp_alta,cli,zona) :
    if tipo == "diaria" :
        tarifa = tipo_tarifa(0)
    elif tipo == "finde" :
        tarifa = tipo_tarifa(1)
    elif tipo == "semana" :
        tarifa = tipo_tarifa(2)
    else :
        tarifa = tipo_tarifa(3)
    tarifa["cod"] = random.randint (1000,9999)
    tarifa["nom"] = cli["datos_basicos"]["apellido"] + ", " + cli["datos_basicos"]["nombre"]
    if vehiculo["tipo"] == "convertible" :
        importe = tarifa["importe"] * 1.4
    elif vehiculo["tipo"] == "camioneta" :
        importe = tarifa["importe"] * 1.3
    else :
        importe = tarifa["importe"]
    tarifa["Bariloche"] = { "temp_alta": False,"zona": False, "recargo_temp": 0, "recargo_zona": 0}
    if vehiculo["ubicacion"] == "Bariloche" :
        if (temp_alta) :
            tarifa["Bariloche"]["recargo_temp"] = 9000
        if zona == 1 :#circuito chico
            tarifa["Bariloche"]["recargo_zona"] += 3000
        elif zona == 2: # catedral
            tarifa["Bariloche"]["recargo_zona"] += 4000
        elif zona == 3: #RN40
            tarifa["Bariloche"]["recargo_zona"] += 5000
    importe = importe + tarifa["Bariloche"]["recargo_zona"]+tarifa["Bariloche"]["recargo_temp"]
    return (tarifa)

def mostrar_tarifa (t) :
    print(f"Cód. tarifa: {t["cod"]}")
    print(f"Cliente: {t["nom"]}")
    print(f"Tipo de tarifa: {t["tipo"]}")
    print(f"Importe total: ${float(t["importe"]):.2f}")
    if t["Bariloche"]["recargo_temp"] > 0 :
        print(f"Recargo por temporada alta: ${float(t["Bariloche"]["recargo_temp"]):.2f}")
    if t["Bariloche"]["recargo_zona"] > 0 :
        print(f"Recargo por zona: ${float(t["Bariloche"]["recargo_zona"]):.2f}")

def seguro (per) :
    cod = int(str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)))
    imp = 5000
    nom = per["datos_basicos"]["apellido"] + ", " + per["datos_basicos"]["nombre"]
    seg = [cod,nom,imp]
    return seg

def mostrar_seguro (seguro) :
    print (f"Cód. seguro: {seguro[0]}\nImporte: ${float(seguro[2]):.2f}\nSeguro a nombre de: {seguro[1]}")

def factura (cliente, vehiculo ,tarifa, seguros) :
    num_factura = random.randint (10000,100000) #nro. random
    tarifa_base = tarifa["importe"]
    seguro_CNS = seguros[0][2]
    seguro_t_n = seguros[1]
    descuento = cliente["vip"]["descuento"]
    recargo_temp = tarifa["Bariloche"]["recargo_temp"]
    recargo_zona = tarifa["Bariloche"]["recargo_zona"]
    importe_total = (tarifa_base + seguro_CNS +seguro_t_n)* (1-descuento)
    cliente["deuda"] = cliente["deuda"] + importe_total
    return (num_factura,cliente["datos_basicos"]["apellido"]+ ", "+  cliente["datos_basicos"]["nombre"], vehiculo["modelo"]+ " patente " + vehiculo["patente"],tarifa_base,seguro_CNS,seguro_t_n,tarifa["tipo"],recargo_temp,recargo_zona,descuento,importe_total) #la hago inmodificable como una tupla por seguridad

def mostrar_factura (factura) :
    print (f"Nro. factura: {factura[0]}")
    print (f"Cliente: {factura[1]}")
    print (f"Vehículo alquilado: {factura[2]}")
    print (f"Tarifa base: ${float(factura[3]):.2f}")
    print (f"Seguro Comisión Nacional de seguros: ${float(factura[4]):.2f}")
    if factura[5] > 0 :
        print (f"Seguro contra tierra y nieve: ${float(factura[5]):.2f}")
    print (f"Duración del alquiler: {factura[6]}")
    if factura[7] > 0 :
        print(f"Recargo por temporada alta: ${float(factura[7]):.2f}")
    if factura[8] > 0 :
        print(f"Recargo por zona: ${float(factura[8]):.2f}")
    if factura[9] > 0 :
        print(f"Descuento VIP: {factura[9]*100}%")  # si imp_final = imp *(1-desc) -> imp = imp_final/(1-desc)
        print(f"Importe total sin descuento: ${float(factura[10]/(1-factura[9])):.2f}")
    print (f"Importe final: ${float(factura[10]):.2f}")

def crear_persona (nom,ap,dni,tel,dom,emp,tel_lab,dom_lab,orig,hot_ag,es_vip,fecha_venc,desc,forma_pago,contacto) :
    persona =  {
        "datos_basicos": datos_basicos(nom,ap,dni,tel,dom,emp,tel_lab,dom_lab),
        "turista":turista(orig,hot_ag) if "turista" in orig else False,
        "es_vip": es_vip,
        "vip": {"vencimiento": fecha_venc, "descuento": desc} if es_vip else {"descuento": desc, "contacto": contacto, "forma_pago": forma_pago},
        "deuda": 0
    }
    return persona

def atr_esp (mod,eq_inv,per_mun) :
    atr_esp = {
        "4x4":True if mod == "Renault Koleos" else False,
        "equipo":eq_inv,
        "permiso":per_mun
    }
    return atr_esp

def crear_vehiculo (mod,nro_ch,mot,ubi,eq_inv) :
    vehiculo = {
        "patente": random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+" "+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),
        "modelo": mod,
        "numero de chasis": nro_ch,
        "motor": mot,
        "tipo": "convertible" if mod == "Ford Mustang" else "auto_4_p" if mod in ["Chevrolet Cruze" ,"Peugeot 306" , "Volkswagen Gol"] else "camioneta",
        "ubicacion": ubi,
        "atributos_esp": atr_esp(mod,eq_inv,random.randint(10,100)) if ubi == "Bariloche" else False
    }
    return vehiculo

def mostrar_persona (per) :
    '''
    Muestra en pantalla los datos de una persona
    '''
    i = 0
    for c,v in per.items() :
        if i == 0 :
            for c0,v0 in v.items() :
                print (f"{c0}: {v0}")
        elif i == 1 and v != False :
             print ("turista")
             for c0,v0 in v.items() :
                print (f"{c0}: {v0}")
        else :
            print (f"{c}: {v}")
        i+=1
    return True

def mostrar_vehiculo (vh) :
    i = 0
    for c,v in vh.items () :
        if i != len(vh)-1 :
            print (f"{c}: {v}")
        else :
            if v != False :
                print ("Atributos Especiales necesarios")
                for c0,v0 in v.items() :
                    print (f"{c0}: {v0}")
        i +=1
    return True
    
def seleccionar_oficina () :
    nro_ofi = input ("Bienvenido a nuestro sistema de alquiler de autos. Seleccione la oficina de alquiler: \n1: Buenos Aires\n2: Córdoba\n3: Rosario\n4: Salta\n5: Tucumán\n6: Catamarca\n7: Bariloche\n")
    while (nro_ofi != '1' and nro_ofi != '2' and nro_ofi != '3' and nro_ofi != '4' and nro_ofi != '5' and nro_ofi != '6' and nro_ofi != '7') :
        nro_ofi = input("Opción inválida. Pruebe nuevamente: ") 
    return int(nro_ofi) - 1

def seleccionar_modelo_auto () :
    modelo = input ("Por favor, seleccione un modelo de vehículo para consultar su disponibilidad:\n1: Ford Focus\n2: Chevrolet Cruze\n3: Renault Koleos\n4: Peugeot 306\n5: Volkswagen Gol\n")
    while (modelo!= '1' and modelo != '2' and modelo != '3' and modelo != '4' and modelo != '5') :
        modelo = input("Opción inválida. Pruebe nuevamente: ") 
    return int(modelo) - 1
    
def disponibilidad_auto (oficinas, nro_ofi, nro_mod) :
    i = 0
    while i < nro_mod :
        i +=1
    dicc_cant_autos = (list(oficinas.items()))[nro_ofi][1]   # esto es la cant de autos en la oficina puntual, porque es un diccionario dentro de un diccionario. o sea, sería "cant_autos: {,,,,,}"
    cant_autos = dicc_cant_autos ["cant_autos"]              #esto es ya el diccionario dentro del diccionario dentro del diccionario principal, sería {"modelo1": cantidad1,,,,}
    lista_cant_autos = (list((cant_autos).items()))          #lo vuelvo una lista
    modelo,cantidad = lista_cant_autos[nro_mod]            # el modelo puntual y su cantidad.
    if cantidad > 0 :
        disponible = True
    else :
        disponible = False
    return disponible

def nro_valido (nro) :
    valido = True
    for x in nro :
        if x not in "0123456789" :
            valido = False
    return valido

def dinero_valido (nro) :
    cant_puntos = 0
    valido = True
    for x in nro :
        if x == "." :
            cant_puntos +=1
        if cant_puntos > 1 :
            valido = False
        else :
            if x not in "0123456789" :
                valido = False
    return valido

def palabra_valida (pal) :
    valida = True
    for x in pal :
        if not ((x >="A" and x <= "Z")  or (x >= "a" and x <= "z") or x in "ÁÉÍÓÚáéíóúÜüñÑ") :
            valida = False
    return valida

def v_o_f_input (respuesta) :
    if (respuesta == "s" or respuesta == "S") :
        v_o_f = True
    else :
        v_o_f = False
    return v_o_f

def devolucion (lista,auto,cliente) :
    lista.append((date.today(),cliente["datos_basicos"]["apellido"]+ ", " + cliente["datos_basicos"]["apellido"],auto["patente"]))

def pagar (factura,cliente) :
    monto = input ("Ingrese el monto a abonar (en $): ")
    while (not dinero_valido(monto)) :
        monto = input ("Cantidad inválida. Ingrese el monto a abonar (en $): ")
    while int(monto) > cliente["deuda"] :
        monto = input ("No puede abonar más del saldo pendiente. Ingrese el monto a abonar (en $): ")
        while (not dinero_valido(monto)) :
            monto = input ("Cantidad inválida. Ingrese el monto a abonar (en $): ")

    cliente["deuda"] = cliente["deuda"] - int(monto)
    return (cliente["datos_basicos"]["dni"],date.today(),factura[0],monto,cliente["deuda"])
    
def mostrar_pago (pago) :
    print (f"Pago realizado.\nDNI: {pago[0]}\nFecha de pago: {pago[1]}\nNro. de factura: {pago[2]}\nImporte del pago: ${float(pago[3]):.2f}")
    if pago[4] > 0 :
        print (f"Saldo pendiente: ${pago[4]}")
    else :
        print ("No registra deuda.")
    
def main () :
    oficinas = {
    "Buenos Aires": {
        "cant_autos": {
            "Ford Mustang"    : 175,
            "Chevrolet Cruze" : 131,
            "Renault Koleos"  : 27,
            "Peugeot 306"     : 0,
            "Volkswagen Gol"  : 267
        }
    },
    "Cordoba": {
        "cant_autos": {
            "Ford Mustang"    : 87,
            "Chevrolet Cruze" : 65,
            "Renault Koleos"  : 14,
            "Peugeot 306"     : 25,
            "Volkswagen Gol"  : 109
        }
    },
    "Rosario": {
        "cant_autos": {
            "Ford Mustang"    : 147,
            "Chevrolet Cruze" : 110,
            "Renault Koleos"  : 23,
            "Peugeot 306"     : 41,
            "Volkswagen Gol"  : 182
        }
    },
    "Salta": {
        "cant_autos": {
            "Ford Mustang"    : 73,
            "Chevrolet Cruze" : 55,
            "Renault Koleos"  : 12,
            "Peugeot 306"     : 22,
            "Volkswagen Gol"  : 91
        }
    },
    "Tucuman": {
        "cant_autos": {
            "Ford Mustang"    : 0,
            "Chevrolet Cruze" : 46,
            "Renault Koleos"  : 10,
            "Peugeot 306"     : 17,
            "Volkswagen Gol"  : 137
        }
    },
    "Catamarca": {
        "cant_autos": {
            "Ford Mustang"    : 24,
            "Chevrolet Cruze" : 18,
            "Renault Koleos"  : 0,
            "Peugeot 306"     : 0,
            "Volkswagen Gol"  : 41
        }
    },
    "Bariloche": {
        "cant_autos": {
            "Ford Mustang"      : 15,
            "Chevrolet Cruze" : 16,
            "Renault Koleos"  : 2,
            "Peugeot 306"     : 0,
            "Volkswagen Gol"  : 20
        }
    }
    }
    oficina = seleccionar_oficina ()
    i = 0
    zona = 0
    temp_alta = 0
    lista_devoluciones = []
    while i != oficina :
        i +=1
    print (f"Bienvenido a nuestra oficina de {list(oficinas.keys())[i]}!")  #la lista de claves del diccionario de oficinas
    modelos = ["Ford Mustang","Chevrolet Cruze" ,"Renault Koleos","Peugeot 306" ,"Volkswagen Gol"]
    modelo_a_consultar = seleccionar_modelo_auto()
    disponible = disponibilidad_auto (oficinas,oficina,modelo_a_consultar)
    modelo_a_consultar = modelos[modelo_a_consultar] #lo paso a nombre
    if disponible:
        print ("Modelo disponible!")
        edad = input ("Introduzca su edad: ")
        while not nro_valido(edad) :
            edad = input ("Edad inválida. Introduzca su edad: ")
        if int(edad) < 25 :
            print ("No cumple con la edad mínima para su reserva (25 años).")
        else :
            per_o_lic = False
            per = input ("¿Tiene permiso de conducir o licencia internacional? (S o N)")
            while (not(per == 's' or per == 'S')) and (not (per == 'n' or per == 'N')) :
                per = input ("Respuesta inválida. ¿Tiene permiso de conducir o licencia internacional? (S o N): ")
            permiso = v_o_f_input (per)
            if permiso :
                per_o_lic = True
            else :
                per_o_lic = False
            if per_o_lic :
                nombre = input ("Introduzca su nombre: ")
                while not palabra_valida(nombre) :
                    nombre = input ("Nombre inválido. Introduzca su nombre: ")
                apellido = input ("Introduzca su apellido: ")
                while not palabra_valida(apellido) :
                    apellido = input ("Apellido inválido. Introduzca su nombre: ")
                dni = input ("Introduzca su DNI/Pasaporte: ")
                while not nro_valido (dni) :
                    dni = input ("Número inválido. Introduzca su DNI/Pasaporte: ")
                tel = input ("Introduzca su teléfono: ")
                while not nro_valido (tel) :
                    tel = input ("Número inválido. Introduzca su teléfono: ")
                dom = input ("Introduzca su domicilio: ")
                empresa = ''
                tel_lab = ''
                dom_lab = ''
                hot_ag = ''
                empresa = input ("¿Para qué empresa trabaja? (dejar en blanco si corresponde): ")
                if empresa != '' :
                    tel_lab = input ("Teléfono laboral: ")
                    while not nro_valido (tel_lab) :
                        tel_lab = input ("Teléfono inválido. Introduzca su teléfono laboral: ")
                    dom_lab = input ("Domicilio laboral: ")
                tur = input ("¿Es usted un turista? (S o N): ")
                while (not(tur == 's' or tur == 'S')) and (not (tur == 'n' or tur == 'N')) :
                    tur = input ("Respuesta inválida. ¿Es usted un turista? (S o N): ")
                turista = v_o_f_input(tur)
                if turista :
                    hot_ag = input ("Ingrese el hotel donde se hospeda o su agencia asociada: ")
                    arg = input ("¿Es usted argentino? (S o N): ")
                    while (not(arg == 's' or arg == 'S')) and (not (arg == 'n' or arg == 'N')) :
                        arg = input ("Respuesta inválida. ¿Es usted argentino? (S o N): ")
                    argentino = v_o_f_input (arg)
                    if argentino :
                        origen = "turista nacional"
                    else :
                        origen = "turista internacional"
                else: 
                    origen = "local"
                v = input ("¿Es usted un cliente VIP? (S o N): ")
                while (not(v == 's' or v == 'S')) and (not (v == 'n' or v == 'N')) :
                    v = input ("Respuesta inválida. ¿Es usted un cliente VIP? (S o N): ")
                vip = v_o_f_input (v)
                contacto = ''
                forma_pago = 0
                desc = 0
                fecha_venc = 0
                if vip :
                    desc = random.randint(8,30)/100 #básicamente es el porcentaje de descuento generado al azar. de 8% a 30%
                    fecha_venc = date.today() + timedelta(days=365 * 5) #vence en 5 años desde hoy
                    print (f"\n\nLe entregamos su tarjeta VIP con descuento exclusivo! Su tarjeta tiene el siguiente beneficio:\nDescuento total: {int(desc*100)}%\nSu tarjeta vence en la fecha {fecha_venc.strftime("%d/%m/%y")}\n\n")
                else :
                    contacto = input("Si desea, infórmenos cómo conoció nuestra empresa: ")
                    forma_pago = input ("¿Cómo abonará su alquiler?\n1: Efectivo\n2: Crédito\n3: Débito")
                    while forma_pago != "1" and forma_pago != "2" and forma_pago != "3" :
                        forma_pago = input ("Opción inválida. ¿Cómo abonará su alquiler?\n1: Efectivo\n2: Crédito\n3: Débito")
                    forma_pago = int(forma_pago)
                tiempo_alq = input ("Seleccione la duración de su alquiler:\n1: Diario\n2: Fin de semana\n3: Semana\n4: Un mes o más\n")
                while tiempo_alq != "1" and tiempo_alq != "2" and tiempo_alq != "3" and tiempo_alq != "4" :
                    tiempo_alq = input ("Opción inválida. Seleccione la duración de su alquiler:\n1: Diario\n2: Fin de semana\n3: Semana\n4: Un mes o más\n")
                if oficina == 6 : #Bariloche
                    temp_alta = input ("¿Viaja en temporada alta? (S o N): ")
                    while (not(temp_alta == 's' or temp_alta == 'S')) and (not (temp_alta == 'n' or temp_alta == 'N')) :
                        temp_alta = input ("Respuesta inválida. ¿Viaja en temporada alta? (S o N): ")
                    temp_alta = v_o_f_input (temp_alta)
                    zona = input("¿Transitará por algunas de estas zonas?\n1: Circuito Chico\n2: Cerro Catedral\n3: Ruta Nacional 40\nN: No\n")
                    while zona != "1" and zona != "2" and zona != "3" and (not (zona == "n" or zona == "N")) :
                        zona = input("Opción inválida.\n¿Transitará por algunas de estas zonas?\n1: Circuito Chico\n2: Cerro Catedra;\n3: Ruta Nacional 40\nN: No")
                    if zona == "n" or zona == "N" :
                        zona = 0
                    else :
                        zona = int(zona)
                seguro_tierra_nieve = 0
                oficinas = ["Buenos Aires", "Cordoba", "Rosario", "Salta", "Tucuman", "Catamarca", "Bariloche"]
                oficina = oficinas[oficina]
                cliente = crear_persona (nombre, apellido, dni, tel, dom, empresa, tel_lab, dom_lab, origen, hot_ag,vip,fecha_venc,desc,forma_pago,contacto)
                auto1 = crear_vehiculo (modelo_a_consultar,"L298N","V4",oficina,True)
                tarifa = crear_tarifa (tiempo_alq,auto1,temp_alta,cliente,zona)
                print("=====================================================================")
                print("=====================================================================")
                mostrar_vehiculo(auto1)
                print("\n\n\n===============================================================")
                mostrar_tarifa(tarifa)
                lista_seguros = []
                seguro_CNS = seguro(cliente)
                mostrar_seguro (seguro_CNS)
                if oficina == "Bariloche" :
                    seguro_tierra_nieve = 2400 #valor cualquiera que se ocurra
                lista_seguros.append(seguro_CNS)
                lista_seguros.append(seguro_tierra_nieve)
                fact = factura(cliente, auto1 ,tarifa, lista_seguros)
                mostrar_persona(cliente)
                print("\n\n\n===============================================================")
                mostrar_factura(fact)
                devolucion (lista_devoluciones,auto1,cliente)
                pago = pagar (fact,cliente)
                print("\n\n\n===============================================================")
                mostrar_pago(pago)
            else :
                print("No puede reservar un vehículo sin permiso o licencia.")
    else :
         print ("Ese modelo no está disponible.")
    print ("\n\nGracias por visitarnos.")
main ()