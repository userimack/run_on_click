from django.shortcuts import render, redirect

# Create your views here.
def click(request):
    print "Function Click called"
    return redirect('/')

def index(request):
    if request.method == 'POST':
        click()
    return render(request, 'app/index.html', {})

