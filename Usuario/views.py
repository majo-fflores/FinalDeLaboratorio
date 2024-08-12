from django.views import View
from django.shortcuts import render, redirect
#from django.core.files.storage import FileSystemStorage
#from user.forms.profile_forms import ProfileForm
from django.contrib.auth import login, authenticate
from .forms import RegistroForm, LoginForm

#class ProfileView(View):
 #   def get(self, request):
  #      form = ProfileForm()
   #     return render(request, 'myapp/profile.html', {'form': form})

    #def post(self, request):
     #   form = ProfileForm(request.POST, request.FILES)
      #  if form.is_valid() and request.FILES.get('profile_pic'):
       #     profile_pic = request.FILES['profile_pic']
        #    fs = FileSystemStorage()
         #   filename = fs.save(profile_pic.name, profile_pic)
          #  uploaded_file_url = fs.url(filename)
            # Aquí puedes actualizar el modelo del usuario con la nueva ruta de la imagen
            # user.profile_pic = uploaded_file_url
            # user.save()
           # return redirect('profile_view')  # Redirige a la misma vista para actualizar la imagen

        #return render(request, 'myapp/profile.html', {'form': form})


#VIEWS LOGEO
class RegistroView(View):
    def get(self, request):
        form = RegistroForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        return render(request, 'registration/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, "Nombre de usuario o contraseña incorrectos")
        return render(request, 'registration/login.html', {'form': form})
