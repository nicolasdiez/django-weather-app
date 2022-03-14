# Views.py file is the one which handles http requests and drives them to the corresponding html webpage
from django.shortcuts import render

def home(request):
    import json
    import requests #needs to be installed first -> $ pip install requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=6EF830AC-9603-4B0E-954B-18C23C271DCD")

    try: 
        #load up into a JSON the content of api_request
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    #make variable 'api' available into the context of the home.html file
    return render(request, 'home.html', {'api':api}) 

def about(request):
    return render(request, 'about.html', {})