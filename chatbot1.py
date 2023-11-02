import re
from datetime import datetime

def es_saludo(mensaje):
    return re.search(r"\b(hola|holaa|buen[oa]s?\s(tardes|días|noches))\b", mensaje, re.IGNORECASE)

def es_despedida(mensaje):
    return re.search(r"\b(adios|chao|hasta (luego|pronto)|nos vemos|me voy|me tengo que ir)\b", mensaje, re.IGNORECASE)

def es_pregunta_hora(mensaje):
    return re.search(r"\b(qué hora (es|tienes)|que horas son|tienes la hora|sabes la hora)\b", mensaje, re.IGNORECASE)

def es_pregunta_estado(mensaje):
    return re.search(r"\b(como estas|como va|qué tal|todo bien|estás bien)\b", mensaje, re.IGNORECASE)

def es_pregunta_odio(mensaje):
    return re.search(r"\b(quien te cae mal|a quien odias|a quien no soportas)\b", mensaje, re.IGNORECASE)
def es_pregunta_hacer(mensaje):
    return re.search(r"\b(que puedes hacer|cuales son tus posobilidades)\b", mensaje, re.IGNORECASE)

def es_pregunta_fecha(mensaje):
    return re.search(r"\b(cuál es la fecha|qué fecha es|que dia es hoy?|cual es la fecha del dia de hoy)\b", mensaje, re.IGNORECASE)

def es_agradecimiento(mensaje):
    return re.search(r"\b(gracias|te agradezco|aprecio|agradecido)\b", mensaje, re.IGNORECASE)

def es_estado_animo(mensaje):
    patrones_estado_animo = [
        r"estoy (bien|mal|feliz|triste|cansado|emocionado|decepcionado|enfadado)",
        r"me siento (bien|mal|genial|deprimido|animado|angustiado)",
        r"todo (va bien|está mal|está complicado)"
    ]
    for patron in patrones_estado_animo:
        if re.search(r"\b({})\b".format(patron), mensaje, re.IGNORECASE):
            return True
    return False

def es_operacion_matematica(mensaje):
    return re.search(r"\b(\d+[\+\-\*\/]\d+)\b", mensaje)

def realizar_operacion_matematica(operacion):
    try:
        resultado = eval(operacion)
        return f"El resultado de {operacion} es {resultado}."
    except Exception as e:
        return "Lo siento, parece que hubo un error con esa operación."

# Diccionario de configuraciones basadas en el rango de presupuesto
configuraciones_pc = {
    
    (50000, 100000): {
        'Procesador': 'AMD Ryzen 9 5950X o Intel Core i9-11900K',
        'Tarjeta Gráfica': 'RTX 3080 o similar',
        'RAM': '32-64GB DDR4 3600MHz o superior',
        'Almacenamiento': 'SSD NVMe Gen4 de 2TB + HDD 4TB',
        'Fuente de Poder': '1000 80 Plus Platinum',
        'Placa Base': 'X570 (AMD) o Z590 (Intel) de alta gama',
        'Gabinete': 'Premium con excelente flujo de aire y acústica',
        'info':'Esto es un rango de precios no es exacto pero sirve como basepara darte una idea',
        
        
    },
    (0, 5000): {
      'Procesador': 'AMD Athlon 3000G',
        'Tarjeta Gráfica': 'Integrada Vega 3',
        'RAM': '8GB DDR4',
        'Almacenamiento': 'SSD de 240GB',
        'Fuente de Poder': 'Genérica de 300-350W',
        'Placa Base': 'A320',
        'Gabinete': 'Genérico',
      'info':'Esto es un rango de precios no es exacto pero sirve como basepara darte una idea',
        

    },
    (5000, 10000): {
        'Procesador': 'Intel Core i3-10100 o AMD Ryzen 3 3200G',
        'Tarjeta Gráfica': 'Integrada o GTX 1050 Ti',
        'RAM': '8GB DDR4',
        'Almacenamiento': 'SSD de 480GB o combinación SSD 240GB + HDD 1TB',
        'Fuente de Poder': '450W 80 Plus',
        'Placa Base': 'B450 (AMD) o B460 (Intel)',
        'Gabinete': 'Genérico con buena ventilación',
        'info':'Esto es un rango de precios no es exacto pero sirve como basepara darte una idea',
        
    },
    (10000, 15000): {
        'Procesador': 'AMD Ryzen 5 3400G o Intel Core i5-10400',
        'Tarjeta Gráfica': 'GTX 1650 o similar',
        'RAM': '16GB DDR4',
        'Almacenamiento': 'SSD de 480GB + HDD 1TB',
        'Fuente de Poder': '500W 80 Plus',
        'Placa Base': 'B450 (AMD) o B460 (Intel)',
        'Gabinete': 'Con buen flujo de aire',
        'info':'Esto es un rango de precios no es exacto pero sirve como basepara darte una idea'
    },
     (15000, 20000): {
        'Procesador': 'AMD Ryzen 5 3600 o Intel Core i5-11400F',
        'Tarjeta Gráfica': 'GTX 1660 o similar',
        'RAM': '16GB DDR4 3200MHz',
        'Almacenamiento': 'SSD NVMe de 500GB + HDD 1TB',
        'Fuente de Poder': '550W 80 Plus Bronze',
        'Placa Base': 'B550 (AMD) o B560 (Intel)',
        'Gabinete': 'Calidad media',
        'info':'Esto es un rango de precios no es exacto pero sirve como basepara darte una idea'
    },
    (20000, 30000): {
        'Procesador': 'AMD Ryzen 5 5600X o Intel Core i5-11600K',
        'Tarjeta Gráfica': 'RTX 3060 o similar',
        'RAM': '16GB DDR4 3600MHz',
        'Almacenamiento': 'SSD NVMe de 1TB',
        'Fuente de Poder': '650W 80 Plus Gold',
        'Placa Base': 'B550 (AMD) o Z590 (Intel)',
        'Gabinete': 'Calidad alta',
        'info':'Esto es un rango de precios no es exacto pero sirve como basepara darte una idea'

    },
    (30000, 50000): {
        'Procesador': 'AMD Ryzen 7 5800X o Intel Core i7-11700K',
        'Tarjeta Gráfica': 'RTX 3070 o similar',
        'RAM': '32GB DDR4 3600MHz',
        'Almacenamiento': 'SSD NVMe de 1TB + HDD 2TB',
        'Fuente de Poder': '750W 80 Plus Gold',
        'Placa Base': 'X570 (AMD) o Z590 (Intel)',
        'Gabinete': 'Alta calidad',
        'info':'Esto es un rango de precios no es exacto pero sirve como basepara darte una idea'
    },
    # Añadir más rangos según sea necesario
}

# Función para obtener la configuración basada en el presupuesto
def obtener_configuracion_presupuesto(presupuesto):
    for rango, configuracion in configuraciones_pc.items():
        if rango[0] <= presupuesto <= rango[1]:
            return configuracion
    return "Lo siento, no tengo una recomendación para ese presupuesto."

def es_pregunta_presupuesto(mensaje):
    return re.search(r"\b(tengo 0000|cuánto cuesta|tengo|presupuesto|cuánto debería gastar|pc|cuánto dinero|cuánto me costaría/mi pre)\b", mensaje, re.IGNORECASE)

# Función principal para obtener la respuesta
def obtener_respuesta(mensaje):
    if es_saludo(mensaje):
        return "¡Hola! ¿En qué puedo asistirte?", None
    elif es_pregunta_estado(mensaje):
        return "Estoy bien, ¡gracias por preguntar! ¿Y tú cómo estás?", None
    elif es_despedida(mensaje):
        return "¡Adiós! Espero hablar contigo pronto.", None
    elif es_pregunta_hora(mensaje):
        return "Son exactamente las " + datetime.now().strftime("%H:%M") + ". ¿Te puedo ayudar en algo más?", None
    elif es_pregunta_fecha(mensaje):
        return "Hoy es " + datetime.now().strftime("%d de %B de %Y") + ".", None
    elif es_agradecimiento(mensaje):
        return "No hay de qué, ¡siempre es un placer ayudar!", None
    elif es_pregunta_hacer(mensaje):
        return "configuraion de pc conforme a tu presupuesto,despedida,saluda,estado de animo,operaciones,hora y dia", None
    elif es_estado_animo(mensaje):
        return "Espero que las cosas mejoren para ti. ¿Hay algo en lo que pueda asistirte?", None
    elif es_operacion_matematica(mensaje):
        operacion = re.search(r"\b(\d+[\+\-\*\/]\d+)\b", mensaje).group()
        return realizar_operacion_matematica(operacion), None
    elif es_pregunta_presupuesto(mensaje):
        return "Claro, puedo ayudarte con eso. ¿Cuál es tu presupuesto para la nueva PC?", 'solicitud_presupuesto'
    elif es_pregunta_odio(mensaje):
        return "Prefiero no fomentar pensamientos negativos. ¿En qué más puedo asistirte?", None
    else:
        return "Interesante. A veces no entiendo todo, pero estoy aprendiendo. ¿Puedes contarme más?", None


estado_actual = 'saludo'
print("Bot: ¡Hola! Soy un asistente virtual. ¿Cómo puedo ayudarte?")
while True:
    entrada_usuario = input("Tú: ").strip()
    if entrada_usuario == "":
        print("Bot: No detecté tu mensaje. ¿Intentas decirme algo más?")
        continue
    respuesta, estado_proximo = obtener_respuesta(entrada_usuario)
    print("Bot: " + respuesta)
    if estado_proximo == 'solicitud_presupuesto':
        presupuesto_usuario = input("Tú: ").strip()
        presupuesto = re.search(r'\d+', presupuesto_usuario)
        if presupuesto:
            presupuesto = int(presupuesto.group())
            configuracion = obtener_configuracion_presupuesto(presupuesto)
            if isinstance(configuracion, str):  # No se encontró una configuración adecuada
                print("Bot: " + configuracion)
            else:
                respuesta_configuracion = "Con base en tu presupuesto, te recomiendo estas especificaciones:\n"
                for componente, especificacion in configuracion.items():
                    respuesta_configuracion += f"{componente}: {especificacion}\n"
                print("Bot: " + respuesta_configuracion)
        else:
            print("Bot: No entendí eso, ¿me puedes decir tu presupuesto en números por favor?")
    if es_despedida(entrada_usuario):
        break
    estado_actual = estado_proximo