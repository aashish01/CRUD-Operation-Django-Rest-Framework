from django.shortcuts import render, redirect
from .forms import product
from .models import item
from django.shortcuts import render
from .models import item
from .serializers import itemSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# API Framework for get and push
class itemList(APIView):
    def get(self, request, format=None):
        items= item.objects.all()
        serializer = itemSerializer(items, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
            serializer = itemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class itemDetail(APIView):
    pass


def all(request):
    items= item.objects.all()
    if request.method =='GET':
        form = product()
    else:
        form = product(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')   
    return render(request,'product.html',{'form':form,'items':items})

def edit(request, id):
    if request.method =='GET':
        if id!=0:
            items = item.objects.get(pk=id)
            form =(product(instance=items))
        return render(request,'edit.html',{'form':form})
    else:
        if id!=0:
            items = item.objects.get(pk=id)
            form = product(request.POST, instance=items)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form})

def delt(request, id):
    items = item.objects.get(pk=id)
    items.delete()
    return redirect('/')
