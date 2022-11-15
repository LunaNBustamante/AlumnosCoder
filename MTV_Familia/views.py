from django.http import HttpResponse
from django.template import Template, Context

#Esto nos permite elaborar plantillas sin necesidad de tener que repetir tanto codigo(renders,etc)
from django.template import loader


def saludo(request):
    return HttpResponse('Hola Mundo')

def ingresar_usuario(request):
    return HttpResponse('Buenas Luna')

def nombre(self, nombre):
    doc = (f'Hola, {nombre}')
    return HttpResponse(doc)



def nombre_apellido(request):

    ##Abrimos el archivo
    archivo = open("C:/Users/Usuario/OneDrive/Documents/Phyton/Coder/Nuestra primera MTV/MTV_Familia/MTV_Familia/templates/templates.html")
    

    ##Creamos el template. Le pasamos para que lea el contenido del archivo
    plantilla = Template(archivo.read())

    ##Cerramos el template
    archivo.close()

    ##Creamos el diccionario de datos
    datos = {
        'nombre': 'Luna','apellido': 'Bustamante'
    }

    #Creamos el contexto donde le pasamos el diccionario con los datos que queremos mostrar en el template

    contexto = Context(datos)

    ##Ahora lo renderizamos bien bonito
    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)


def vista_listado_alumnos(request):
        # Abrimos el archivo
    archivo = open(r"C:/Users/Usuario/OneDrive/Documents/Phyton/Coder/Nuestra primera MTV/MTV_Familia/MTV_Familia/templates/templates.html")
        # Creamos el template
    plantilla = Template(archivo.read()) 
        #Cerramos el archivo para liberar recursos
    archivo.close()
        # Creamos el diccionario de datos
    
    listado_alumnos = ["Leonel Gareis", "Agustin Russo", "Cristian Garcia", "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante", "Barbara Pino"]
    
    datos = {"tecnologia": "React", "listado_alumnos": listado_alumnos}
       
        # Creamos el contexto
    
    contexto = Context(datos)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)


###ESTE ES LA POSTA PORQUE ES MUCHO MAS FACIL
##PARA ESTO FUIMOS A SETTINGS Y COPIAMOS EL URL PARA LA SECCION DE TEMPLATES
def listado_mas_rapido(request):
    plantilla = loader.get_template('templates.html')

    #Creamos el diccionario con los datos
    listado_alumnos = ["Leonel Gareis", "Agustin Russo", "Cristian Garcia", "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante", "Barbara Pino"]

    datos = {"tecnologia": "React", "listado_alumnos": listado_alumnos}
   
    documento = plantilla.render(datos)

    return HttpResponse(documento)