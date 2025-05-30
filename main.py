

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

def crear_persona (nom,ap,dni,tel,dom,emp,tel_lab,dom_lab,orig,hot_ag,es_vip) :
    persona =  {
        "datos_basicos": datos_basicos(nom,ap,dni,tel,dom,emp,tel_lab,dom_lab),
        "turista":turista(orig,hot_ag) if "turista" in orig else False,
        "prestigio":es_vip

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
    

    
    
    

def main () :
    p = intr_datos()
    mostrar_persona(p)
    chata = crear_vehiculo ("ABC 123","Ford Focus","L298N","V4","sedan","bariloche",False,True,"C12E4")
    oficinas = {
    "buenos_aires": {
        "cant_autos": {
            "Ford Focus"      : 175,
            "Chevrolet Cruze" : 131,
            "Renault Koleos"  : 27,
            "Peugeot 306"     : 49,
            "Volkswagen Gol"  : 218
        }
    },
    "cordoba": {
        "cant_autos": {
            "Ford Focus"      : 87,
            "Chevrolet Cruze" : 65,
            "Renault Koleos"  : 14,
            "Peugeot 306"     : 25,
            "Volkswagen Gol"  : 109
        }
    },
    "rosario": {
        "cant_autos": {
            "Ford Focus"      : 147,
            "Chevrolet Cruze" : 110,
            "Renault Koleos"  : 23,
            "Peugeot 306"     : 41,
            "Volkswagen Gol"  : 182
        }
    },
    "salta": {
        "cant_autos": {
            "Ford Focus"      : 73,
            "Chevrolet Cruze" : 55,
            "Renault Koleos"  : 12,
            "Peugeot 306"     : 22,
            "Volkswagen Gol"  : 91
        }
    },
    "tucuman": {
        "cant_autos": {
            "Ford Focus"      : 61,
            "Chevrolet Cruze" : 46,
            "Renault Koleos"  : 10,
            "Peugeot 306"     : 17,
            "Volkswagen Gol"  : 76
        }
    },
    "catamarca": {
        "cant_autos": {
            "Ford Focus"      : 24,
            "Chevrolet Cruze" : 18,
            "Renault Koleos"  : 4,
            "Peugeot 306"     : 7,
            "Volkswagen Gol"  : 30
        }
    },
    "bariloche": {
        "cant_autos": {
            "Ford Focus"      : 15,
            "Chevrolet Cruze" : 12,
            "Renault Koleos"  : 2,
            "Peugeot 306"     : 4,
            "Volkswagen Gol"  : 20
        }
    }
}
main ()