from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from .models import Image
from .extract.prediction import predict
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import os
#from graphapp import settings
from django.conf import settings



# Create your views here.
#@login_required(login_url='login')

def index(request):
    return render(request,'index.html')

def ulogin(request):
     if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

     return render(request,'login.html')

def signupp(request):
      if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        

      return render(request,'signup.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


 
def upload(request):
   if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            uploaded_image = form.cleaned_data['image']
            image_path = os.path.join(settings.MEDIA_ROOT,'myimage', uploaded_image.name)
           # print(image_path)
            image = cv2.imread(image_path)
           # image = cv2.imread(uploaded_image.name)
            # print("................")
            # print(image)
            # print("..............")
            predict(image)
        #       # Retrieve the uploaded img
                 
           # nparr = np.fromstring(uploaded_image.read(), np.uint8)
        #     #print(nparr)
        #     image = cv2.imdecode(cv2.IMREAD_COLOR)
        #    # print(Image)
        #     if nparr is not None and len(nparr) > 0:
        #             image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        #     #         # Further processing of the image
        #     else:
        #     #      # Handle the case when the buffer is empty
        #         print("Empty buffer")

            return HttpResponse("Image uploaded and processed successfully!")
    


   else:
        form = ImageForm()

   return render(request, 'upload.html', {'form': form})