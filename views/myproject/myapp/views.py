from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def home(request):
    return HttpResponse('Welcome to Little Lemon restaurant!')

def homepage(request):
    return HttpResponse("Welcome to Little Lemon!")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def index(request): 
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content)

def response(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info
    
    result = HttpResponse()
    result.headers ["Age"] = 20
    
    msg = f"""<br>
    <br>Path {path}
    <br>Scheme {scheme}
    <br>Method {method}
    <br>Address {address}
    <br>User Agent {user_agent}
    <br>Path Info {path_info}
    <br>Response Headers {result.headers}
    """
    return HttpResponse(msg, content_type='text/html', charset='utf-8')

def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def showform(request): 
    return render(request, "myapp/form.html") 

def getform(request): 
    if request.method == "POST": 
        name=request.POST['name'] 
        id=request.POST['id']         
    return HttpResponse("Name:{} UserID:{}".format(id, name)) 

def menuitems(request, dish):
    items = {
        'pasta' : 'Pasta with red sauce',
        'pizza' : 'Pizza with extra cheese',
        'burger' : 'Veg burger with fries', 
    }
    
    description = items[dish]
    
    return HttpResponse(f"<h2>{dish}<h2>" + description)

def drinks(request, drink_name):
    items = {
        'mocha' : 'type of coffee',
        'tea' : 'type of hot beverage',
        'lemonade' : 'type of refreshment',
    }
    
    choice_of_drink = items[drink_name]
    
    return HttpResponse(f"<h2>{drink_name}<h2>" + choice_of_drink)

def about(request):
    return HttpResponse("About us")

def menu(request):
    return HttpResponse("Menu for Little Lemon")

def book(request):
    return HttpResponse("Make a booking")


