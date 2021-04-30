from django.shortcuts import render
from .models import AjaxModel
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.

# @csrf_exempt
def CreateAjax(request):
  ajaxlist = AjaxModel.objects.all()
  if request.is_ajax():
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if request.POST.get("identifier") != '':
              editItem = AjaxModel.objects.get(id = request.POST.get("identifier"))
              editItem.name = name
              editItem.email = email
              editItem.password = password
              editItem.save()
              return JsonResponse({"response": "updated successfully!",
              "name": name,
              "email": email,
              "password": password,
              "allRecords": list(AjaxModel.objects.values())
              })
        AjaxModel.objects.create(name = name, email = email, password = password)
        return JsonResponse({"result": "reponse successfully got!",
          'name': name,
          'email': email,
          'password': password,
          'allRecords': list(AjaxModel.objects.values())
        })
  return render(request, "ajax.html", {"ajaxlist": ajaxlist} )

def Delete(request):
  ajaxlist = AjaxModel.objects.all()
  if request.is_ajax():
    ajazItem = AjaxModel.objects.get(id = request.POST.get('deleteData'))    
    ajazItem.delete()
    return JsonResponse({"response": "request to delete the entry!"})
  return render(request, "ajax.html",  {"ajaxlist": ajaxlist}) 