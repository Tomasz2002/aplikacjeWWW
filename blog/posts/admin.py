from django.contrib import admin
from .models import Category, Topic, Post 

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name']


class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['name', 'category']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'topic_with_category', 'created_at', 'created_by']
    readonly_fields = ['created_at', 'updated_at']
    list_filter = ['created_by', 'topic', 'topic__category']
    prepopulated_fields = {'slug': ('title',)}

    @admin.display(description='Topic (Category)')
    def topic_with_category(self, obj):
        if obj.topic: 
            return f"{obj.topic.name} ({obj.topic.category.name})"
        return "Brak"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)