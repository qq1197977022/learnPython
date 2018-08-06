from django.contrib import admin
from .models import Book, Hero

# Register your models here.

# 1.默认使用admin interface
# admin.site.register(Book) # 在默认admin interface中注册model类
# admin.site.register(Hero)

# 2.ModelAdmin类对象是model类在admin interface中的表示


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_filter = ('name', 'date')
    search_fields = ('name',)


class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'book')
    list_filter = ('gender', 'book')
    search_fields = ('gender',)  # 布尔类型字段搜索: 0 false, 1 true
    fieldsets = (['个人信息', {'fields': ('name', 'gender')}],
                 ['所属书籍', {'fields': ('book',)}],
                 )  # 分组


admin.site.register(Book, BookAdmin)    # 注册model类
admin.site.register(Hero, HeroAdmin)


# 3.注册器装饰器











