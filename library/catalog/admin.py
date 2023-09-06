from django.contrib import admin
from catalog.models import Genre, Language, Country, Book, BookInstance, Author


class BookInLine(admin.TabularInline):
    model = Book


class BookInstanceInLine(admin.TabularInline):
    model = BookInstance


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'pseudonym']
    search_fields = ["pseudonym", "first_name"]
    inlines = [BookInLine]


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_genre']
    search_fields = ['title', 'author__pseudonym', 'genre__name']
    inlines = [BookInstanceInLine]


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['book', 'isbn', 'status', 'borrower', 'due_back']
    search_fields = ['title', 'author__pseudonym', 'genre__name']
    fieldsets = (
        ("Group1", {
            'fields': ('book', 'isbn', 'status')
        }),
        (
            'Group2', {
                'fields': ('borrower', 'due_back')
            }
        )
    )


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Country)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
