from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import datetime

def get_greeting(hour):
   
    if hour < 12:
        return "Buenos días"
    elif hour < 18:
        return "Buenas tardes"
    else:
        return "Buenas noches"

def phrase_of_the_day(request):
   
    if request.method == 'POST':
        name = request.POST.get('name')  
        try:
            response = requests.get('https://frasedeldia.azurewebsites.net/api/phrase')
            if response.status_code == 200:
                data = response.json()
                print(data) 
                quote = data.get('phrase', 'Frase no encontrada')
                author = data.get('author', 'Desconocido')
                current_hour = datetime.now().hour
                greeting = get_greeting(current_hour)  
                context = {
                    'greeting': greeting,
                    'name': name,
                    'quote': quote,
                    'author': author
                }
                return render(request, 'phrase.html', context)
            else:
                return HttpResponse("Error al obtener la frase del día", status=response.status_code)
        except Exception as e:
            return HttpResponse(f"Error al procesar la solicitud: {str(e)}", status=500)
    else:
        return render(request, 'phrase.html')

