from django.views import View
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from user.forms.profile_forms import ProfileForm

class ProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, 'myapp/profile.html', {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and request.FILES.get('profile_pic'):
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            uploaded_file_url = fs.url(filename)
            # Aquí puedes actualizar el modelo del usuario con la nueva ruta de la imagen
            # user.profile_pic = uploaded_file_url
            # user.save()
            return redirect('profile_view')  # Redirige a la misma vista para actualizar la imagen

        return render(request, 'myapp/profile.html', {'form': form})
