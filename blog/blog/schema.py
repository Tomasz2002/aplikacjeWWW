import graphene
from graphene_django import DjangoObjectType
from posts.models import Category, Topic, Post
from django.contrib.auth.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email")

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "description")

class TopicType(DjangoObjectType):
    class Meta:
        model = Topic
        fields = ("id", "name", "category", "created")

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("id", "title", "text", "topic", "slug", "created_at", "created_by")

class CreatePostMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        text = graphene.String(required=True)
        slug = graphene.String(required=True)
        topic_id = graphene.ID(required=True)
        user_id = graphene.ID(required=True)

    post = graphene.Field(PostType)

    def mutate(self, info, title, text, slug, topic_id, user_id):
        topic = Topic.objects.get(pk=topic_id)
        user = User.objects.get(pk=user_id)
        post = Post.objects.create(
            title=title, 
            text=text, 
            slug=slug, 
            topic=topic, 
            created_by=user
        )
        return CreatePostMutation(post=post)

class UpdatePostMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        text = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info, id, title=None, text=None):
        try:
            post = Post.objects.get(pk=id)
            if title:
                post.title = title
            if text:
                post.text = text
            post.save()
            return UpdatePostMutation(post=post)
        except Post.DoesNotExist:
            return None

class DeletePostMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    message = graphene.String()

    def mutate(self, info, id):
        try:
            post = Post.objects.get(pk=id)
            post.delete()
            return DeletePostMutation(message="Post usunięty")
        except Post.DoesNotExist:
            return DeletePostMutation(message="Post nie istnieje")

class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    all_topics = graphene.List(TopicType)
    all_posts = graphene.List(PostType)
    posts_by_title_search = graphene.List(PostType, search=graphene.String(required=True))
    count_posts_by_user = graphene.Int(user_id=graphene.ID(required=True))
    posts_by_topic = graphene.List(PostType, topic_id=graphene.ID(required=True))

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_all_topics(root, info):
        return Topic.objects.all()

    def resolve_all_posts(root, info):
        return Post.objects.select_related("topic", "created_by").all()

    def resolve_posts_by_title_search(root, info, search):
        return Post.objects.filter(title__icontains=search)

    def resolve_count_posts_by_user(root, info, user_id):
        return Post.objects.filter(created_by__id=user_id).count()

    def resolve_posts_by_topic(root, info, topic_id):
        return Post.objects.filter(topic__id=topic_id)

class Mutation(graphene.ObjectType):
    create_post = CreatePostMutation.Field()
    update_post = UpdatePostMutation.Field()
    delete_post = DeletePostMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)