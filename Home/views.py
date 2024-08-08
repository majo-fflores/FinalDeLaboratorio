from msilib.schema import ListView
from django.db.models import Q
from Libro.models import Libro

# Create your views here.
#VIEW HOME
class HomeView(ListView):
    model = Libro
    template_name = 'Home/templates/home.html'
    context_object_name = 'libros'
    paginate_by = 20

    #Agarra todos los forms del html de tipo get
    def get_queryset(self):
        queryset = Libro.objects.all()
        search_query = self.request.GET.get('buscar')

        if search_query:
            queryset = queryset.filter(
                Q(titulo__icontains=search_query) |
                Q(autor__icontains=search_query) |
                Q(isbn__icontains=search_query)
            )

        return queryset