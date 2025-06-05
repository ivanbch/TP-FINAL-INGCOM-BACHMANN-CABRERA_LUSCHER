import random
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

def tipo_tarifa (n) :
    tarifas = [
        {"cod": "", "nom": "", "tipo": "diaria", "importe": 0, "bariloche": False},
        {"cod": "", "nom": "", "tipo": "finde", "importe": 0, "bariloche": False},
        {"cod": "", "nom": "", "tipo": "semana", "importe": 0, "bariloche": False},
        {"cod": "", "nom": "", "tipo": "mes_mas", "importe": 0, "bariloche": False}   
    ]
    return tarifas[n]

def crear_tarifa (tipo,vehiculo,mes) :
    if tipo == "diaria" :
        tarifa = tipo_tarifa(0)
    elif tipo == "finde" :
        tarifa = tipo_tarifa(1)
    elif tipo == "semana" :
        tarifa = tipo_tarifa(2)
    else :
        tarifa = tipo_tarifa(3)
    if vehiculo["ubicacion"] == "bariloche" :
        tarifa["bariloche"] = { "temp_alta": False,"zona": False, "recargo": False}
        if (mes >= 6 and mes <= 9) or (mes == 12 or mes == 1 or mes == 2) :
            tarifa["bariloche"]["recargo"] = 9000
    return tarifa

def seguro (veh,per,num_cod) :
    cod = f"{num_cod:04}" 
    imp = 5000
    nom = per["datos_basicos"]["apellido"] + ", " + per["datos_basicos"]["nombre"]
    if veh["ubicacion"] == "bariloche" :
        importe = importe * 1.5
    seg = [cod,nom,imp]
    return seg

def crear_persona (nom,ap,dni,tel,dom,emp,tel_lab,dom_lab,orig,hot_ag,es_vip,fecha_venc,desc) :
    persona =  {
        "datos_basicos": datos_basicos(nom,ap,dni,tel,dom,emp,tel_lab,dom_lab),
        "turista":turista(orig,hot_ag) if "turista" in orig else False,
        "vip": {"vencimiento": fecha_venc, "descuento": desc} if es_vip else False
    }
    return persona

def atr_esp (cuat_x_cuat,eq_inv,per_mun) :
    atr_esp = {
        "4x4":cuat_x_cuat,
        "equipo":eq_inv,
        "permiso":per_mun
    }
    return atr_esp

def crear_vehiculo (pat,mod,nro_ch,mot,tipo,ubi,cuat_x_cuat,eq_inv,per_mun) :
    vehiculo = {
        "patente": pat,
        "modelo": mod,
        "numero de chasis": nro_ch,
        "motor": mot,
        "tipo": tipo,
        "ubicacion": ubi,
        "atributos": atr_esp(cuat_x_cuat,eq_inv,per_mun) if ubi == "bariloche" else False
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

def intr_datos () :
    edad = input ("Introduzca su edad: ")
    if int(edad) >= 25:
        nom = input ("Introduzca su nombre: ")
        ap = input ("Introduzca su apellido: ")
        dni = input ("Introduzca su DNI: ")
        tel = input ("Introduzca su teléfono: ")
        dom = input ("Introduzca su domicilio: ")
        empr = input ("¿Para qué empresa trabaja? ")
        tel_lab = input ("Introduzca su teléfono laboral: ")
        dom_lab = input ("Introduzca su domicilio laboral: ")
        es_vip =  input ("¿Es cliente VIP? (S o N): ")
        while (es_vip != "s" and es_vip != "n") :
            print("Opción inválida.")
            es_vip = input ("¿Es cliente VIP? (S o N): ")
        if es_vip == "s" :
            vip = True
        else :
            vip = False
        vtur = input ("¿Es usted turista? (S o N): ")
        while (vtur != "s" and vtur != "n") :
            print("Opción inválida.")
            vtur = input ("¿Es usted turista? (S o N): ")
        if vtur == "n" :
            tur = "local"
            hot = False
        else :
            vint = input ("¿Es usted extranjero? (S o N): ")
            hot = input("¿En qué hotel se aloja? ")
            while (vint != "s" and vint != "n") :
                print("Opción inválida.")
                vint = input ("¿Es usted extranjero? (S o N): ")
            if vint == "s" :
                tur = "turista internacional"
            else :
                tur = "turista nacional"
        return crear_persona (nom,ap,dni,tel,dom,empr,tel_lab,dom_lab,tur,hot,vip)
    else :
        return False
    
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

def main () :
    auto1 = crear_vehiculo ("ABC 123","Ford Focus","L298N","V4","sedan","bariloche",False,True,"C12E4")
    oficinas = {
    "Buenos Aires": {
        "cant_autos": {
            "Ford Focus"      : 175,
            "Chevrolet Cruze" : 131,
            "Renault Koleos"  : 27,
            "Peugeot 306"     : 49,
            "Volkswagen Gol"  : 218
        }
    },
    "Cordoba": {
        "cant_autos": {
            "Ford Focus"      : 87,
            "Chevrolet Cruze" : 65,
            "Renault Koleos"  : 14,
            "Peugeot 306"     : 25,
            "Volkswagen Gol"  : 109
        }
    },
    "Rosario": {
        "cant_autos": {
            "Ford Focus"      : 147,
            "Chevrolet Cruze" : 110,
            "Renault Koleos"  : 23,
            "Peugeot 306"     : 41,
            "Volkswagen Gol"  : 182
        }
    },
    "Salta": {
        "cant_autos": {
            "Ford Focus"      : 73,
            "Chevrolet Cruze" : 55,
            "Renault Koleos"  : 12,
            "Peugeot 306"     : 22,
            "Volkswagen Gol"  : 91
        }
    },
    "Tucuman": {
        "cant_autos": {
            "Ford Focus"      : 61,
            "Chevrolet Cruze" : 46,
            "Renault Koleos"  : 10,
            "Peugeot 306"     : 17,
            "Volkswagen Gol"  : 76
        }
    },
    "Catamarca": {
        "cant_autos": {
            "Ford Focus"      : 24,
            "Chevrolet Cruze" : 18,
            "Renault Koleos"  : 4,
            "Peugeot 306"     : 7,
            "Volkswagen Gol"  : 30
        }
    },
    "Bariloche": {
        "cant_autos": {
            "Ford Focus"      : 15,
            "Chevrolet Cruze" : 16,
            "Renault Koleos"  : 2,
            "Peugeot 306"     : 0,
            "Volkswagen Gol"  : 20
        }
    }
    }
    oficina = seleccionar_oficina ()
    i = 0
    while i != oficina :
        i +=1
    print (f"Bienvenido a nuestra oficina de {list(oficinas.keys())[i]}!")  #la lista de claves del diccionario de oficinas
    modelo_a_consultar = seleccionar_modelo_auto()
    disponible = disponibilidad_auto (oficinas,oficina,modelo_a_consultar)
    if disponible:
        print ("Modelo disponible!")
        edad = input ("Introduzca su edad: ")
        while not nro_valido(edad) :
            edad = input ("Edad inválida. Introduzca su edad: ")
        if int(edad) < 25 :
            print ("No cumple con la edad mínima para su reserva (25 años).")
        else :
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
            permiso_o_lic = False
            if turista :
                hot_ag = input ("Ingrese el hotel donde se hospeda o su agencia asociada: ")
                arg = input ("¿Es usted argentino? (S o N): ")
                while (not(arg == 's' or arg == 'S')) and (not (arg == 'n' or arg == 'N')) :
                    arg = input ("Respuesta inválida. ¿Es usted argentino? (S o N): ")
                argentino = v_o_f_input (arg)
                if argentino :
                    origen = "turista nacional"
                    per = input ("¿Tiene permiso de conducir? (S o N)")
                    while (not(per == 's' or per == 'S')) and (not (per == 'n' or per == 'N')) :
                        per = input ("Respuesta inválida. ¿Tiene permiso de conducir? (S o N): ")
                    permiso = v_o_f_input (per)
                    if permiso :
                        permiso_o_lic = True
                    else :
                        permiso_o_lic = False

                else :
                    origen = "turista internacional"
                    lic = input ("¿Tiene licencia internacional de conducir? (S o N)")
                    while (not(lic == 's' or lic == 'S')) and (not (lic == 'n' or lic == 'N')) :
                        lic = input ("Respuesta inválida. ¿Tiene licencia internacional de conducir? (S o N): ")
                    licencia_int = v_o_f_input (lic)
                    if  licencia_int :
                        permiso_o_lic = True
                    else :
                        permiso_o_lic = False
            else: 
                origen = "local"
                per = input ("¿Tiene permiso de conducir? (S o N)")
                while (not(per == 's' or per == 'S')) and (not (per == 'n' or per == 'N')) :
                    per = input ("Respuesta inválida. ¿Tiene permiso de conducir? (S o N): ")
                permiso = v_o_f_input (per)
                if permiso :
                    permiso_o_lic = True
                else :
                    permiso_o_lic = False
            if permiso_o_lic :
                v = input ("¿Es usted un cliente VIP? (S o N)")
                while (not(v == 's' or v == 'S')) and (not (v == 'n' or v == 'N')) :
                    v = input ("Respuesta inválida. ¿Es usted un cliente VIP? (S o N): ")
                vip = v_o_f_input (v)
                if vip :
                    desc = random.randint(0,31)/100 #básicamente es el porcentaje de descuento generado al azar. máximo un 30% o sea 0.3
                    fecha_venc = date.today() + timedelta(days=365 * 5) #vence en 5 años desde hoy
                    print (f"Le entregamos su tarjeta VIP con descuento exclusivo! Su tarjeta tiene el siguiente beneficio:\nDescuento total: {int(desc*100)}%\nSu tarjeta vence en la fecha {fecha_venc.strftime("%d/%m/%y")}")
                else :
                    desc = 0
                    fecha_venc = 0
                cliente = crear_persona (nombre, apellido, dni, tel, dom, empresa, tel_lab, dom_lab, origen, hot_ag,vip,fecha_venc,desc)
                print (cliente)
            else :
                print("No puede reservar un vehículo sin permiso o licencia.")        
    else :
         print ("Ese modelo no está disponible.")
        
main ()