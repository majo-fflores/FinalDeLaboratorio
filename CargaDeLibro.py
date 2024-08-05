import os, django, requests 
from Libro.models import Libro

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BookVerse.settings')
django.setup()


# Lista de géneros a crear
nombres_generos = [
    "Romance", "Fantasy", "Science Fiction", "Mystery",
    "Horror", "Thriller", "Historical",
]

# Función para obtener libros de Open Library
def obtener_libros(query, limit=40):
    url = f"https://openlibrary.org/search.json?subject={query}&limit={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('docs', [])
    else:
        print(f"Error al obtener libros para la consulta '{query}': {response.status_code}")
        return []

# Función para cargar libros en la base de datos
def cargar_libros(genero):
    libros = obtener_libros(genero)
    for libro in libros:
        titulo = libro.get('title', 'Título desconocido')
        autores = ", ".join(libro.get('author_name', ['Autor desconocido']))
        isbn_list = libro.get('isbn', [])
        isbn = isbn_list[0] if isbn_list else None
        if isbn is None:
            continue  # Salta libros sin ISBN
        sinopsis = libro.get('first_sentence', {}).get('value', f"Libro sobre {genero}")
        portada = f"http://covers.openlibrary.org/b/isbn/{isbn}-L.jpg" if isbn else None
        editorial = libro.get('publisher', ['Editorial desconocida'])[0]

        # Crear y guardar el libro en la base de datos
        libro_obj, created = Libro.objects.get_or_create(
            isbn=isbn,
            defaults={
                'titulo': titulo,
                'autor': autores,
                'sinopsis': sinopsis,
                'genero': genero,
                'editorial': editorial,
                'portada': portada,
            }
        )

        if created:
            print(f"Libro '{titulo}' creado.")
        else:
            print(f"Libro '{titulo}' ya existe en la base de datos.")

# Cargar al menos 1000 libros distribuidos en los géneros
libros_por_genero = 100
for genero in nombres_generos:
    cargar_libros(genero)

print("Carga de libros completada.")
