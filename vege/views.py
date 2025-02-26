from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse

# Create your views here.

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        
            # If all fields are provided, create the recipe
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
             )
        return redirect('/receipes')
    queryset = Receipe.objects.all()
    context = {'receipes': queryset}

    return render(request , "receipes.html" ,  context)


def update_receipes(request, id):
    receipe = Receipe.objects.get(id=id)

    if request.method == "POST":
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        # Update name and description
        receipe.receipe_name = receipe_name
        receipe.receipe_description = receipe_description

        # Only update image if a new one is provided
        if receipe_image:
            receipe.receipe_image = receipe_image
        
        # Save the updated recipe
        receipe.save()
        return redirect('/receipes')

    # If GET request, render the update form with existing recipe data
    context = {'receipe': receipe}
    return render(request, "update_receipes.html", context)
def delete_receipes(request, id):

    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    
    return redirect('/receipes')