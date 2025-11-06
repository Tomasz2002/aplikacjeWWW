from posts.models import Category, Topic, Post
from django.contrib.auth.models import User
from posts.serializers import CategorySerializer, PostSerializer

print("--- Test 1: CategorySerializer ---")

cat = Category.objects.create(name="Test Kat", description="Test Opis")
serializer_cat = CategorySerializer(cat)
print("Serializacja Cat OK:", serializer_cat.data)

cat_data = {'name': 'Nowa Kat', 'description': 'Nowy Opis'}
deserializer_cat = CategorySerializer(data=cat_data)
if deserializer_cat.is_valid():
    new_cat = deserializer_cat.save()
    print(f"Deserializacja Cat OK, dodano: {new_cat.name} (id: {new_cat.id})")
else:
    print("Blad Cat:", deserializer_cat.errors)

print("\n--- Test 2: PostSerializer ---")

try:
    # Zakladamy, ze user o id=1 (superuser) istnieje
    user = User.objects.get(id=1) 
    # Uzywamy kategorii 'cat' stworzonej wyzej
    topic = Topic.objects.create(name="Test Topic", category=cat)
    print(f"\nSetup OK (user: {user.username}, topic: {topic.name})")

    post = Post.objects.create(
        title="Test Post", text="Test text...",
        topic=topic, slug="test-post", created_by=user
    )
    serializer_post = PostSerializer(post)
    print("Serializacja Post OK:", serializer_post.data)

    post_data = {
        'title': 'Nowy Post', 'text': 'Nowy text...',
        'slug': 'nowy-post',
        'topic': topic.id, # Dla klucza obcego podajemy samo ID
        'created_by': user.id # Dla klucza obcego podajemy samo ID
    }
    deserializer_post = PostSerializer(data=post_data)
    if deserializer_post.is_valid():
        new_post = deserializer_post.save()
        print(f"Deserializacja Post OK, dodano: {new_post.title} (id: {new_post.id})")
    else:
        print("Blad Posta:", deserializer_post.errors)

except User.DoesNotExist:
    print("\nBLAD: User o id=1 nie istnieje. Stworz go przez 'createsuperuser'.")
except Exception as e:
    print(f"\nBLAD: {e}")

print("\n--- KONIEC TESTOW ---")