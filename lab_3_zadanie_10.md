from posts.models import Category, Topic, Post
from django.contrib.auth.models import User

# 1. wyświetl wszystkie obiekty modelu Category
Category.objects.all()

# 2. wyświetl obiekt modelu Category z id = 3
Category.objects.get(id=3)

# 3. wyświetl obiekty Category, których nazwa zaczyna się na 'F'
Category.objects.filter(name__startswith='F')

# 4. wyświetl unikalną listę nazw kategorii ze wszystkich tematów
Topic.objects.values_list('category__name', flat=True).distinct()

# 5. wyświetl tytuły postów posortowane alfabetycznie malejąco
Post.objects.order_by('-title').values_list('title', flat=True)

# 6. dodaj nową instancję obiektu klasy Category i zapisz w bazie
new_cat = Category(name="Testowa Kategoria", description="Opis z shella")
new_cat.save()