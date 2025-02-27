from socket import EAI_SERVICE
from statistics import correlation
from xml.dom.minidom import Entity


Algoritmo RedirigirAGoogleForms
    Definir urlFormulario Como Cadena
    Definir respuesta Como Cadena

    // URL del formulario de Google Forms (aquí debes poner la URL real del formulario)
    urlFormulario <- "https://forms.gle/xxxxxxxxxxxxxxxx"

    // Mensaje que invita al usuario a completar el formulario
    Escribir "Por favor, completa el siguiente formulario con tus datos."
    Escribir "El formulario solicitará lo siguiente:"
    Escribir "1. Nombre(s)"
    Escribir "2. Apellidos"
    Escribir "3. Archivos necesarios (acta de nacimiento, CURP)"
    Escribir "4. Certificado de prepatoria y/o Kardex parcial de estudios universitarios"
    

    // Simula la acción de redirigir
    Escribir "Si deseas continuar, presiona Enter para acceder al formulario."
    Leer respuesta

    Si respuesta = "" Entonces
        Escribir "Redirigiendo al formulario..."
        Escribir "Abriendo el formulario de Google Forms: " + urlFormulario
        // Simula la apertura del formulario en un navegador
    Sino
        Escribir "Operación cancelada."
        Escribir "Si deseas solicitar no cancelar el acceso a la plataforma, presiona Enter."
        Leer respuesta
        Si respuesta = "" Entonces
            Escribir "Solicitud de no cancelación de acceso enviada."
        FinSi
    FinSi

    # Creación de flujo para enviar correo a dirección
    Escribir "Por favor elige el destinatario del correo:"
    ; Definir [destinatario] Como cadena
    Destinatario[Escolar,Direccion,Coordinacion]
    Escribir "Por favor, ingresa el asunto del correo:"
    Definir [asunto]
    Escribir "Por favor, ingresa el contenido del correo:"
    Definir [Contenido]
    Escribir "Desea Enviar el correo?"
    Si respuesta = "Si" Entity
      Escribir "Enviando correo..."
      // Simula en envio del correlation
      Escribir "Correo enviado"
    Sino 
       Escribir "Operacion cancelada"
    FinSi

    # Pruebas de biométricos
    Escribir "Por favor, coloca tu dedo en el lector de huellas digitales."
    Definir huellaDigital Como Cadena
    Leer huellaDigital

    Si huellaDigital != "" Entonces
        Escribir "Huella digital capturada exitosamente."
        // Simula la verificación de la huella digital
        Escribir "Verificando huella digital..."
        Definir verificacion Como Booleano
        verificacion <- True // Simula una verificación exitosa

        Si verificacion Entonces
            Escribir "Huella digital verificada correctamente."
        Sino
            Escribir "Error en la verificación de la huella digital."
        FinSi
    Sino
        Escribir "No se pudo capturar la huella digital."
    FinSi

    # Mensaje de penalización
    Escribir "Recuerda que la penalización por retraso en el pago es del 20% del costo de la colegiatura."

FinAlgoritmo



