# blog/blog/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),       
    path('', include('posts.urls_html')),      
    path('api-auth/', include('rest_framework.urls')),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]