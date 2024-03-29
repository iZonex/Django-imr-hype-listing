from django.contrib import admin

from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from models import Post

class PostAdmin(TranslationAdmin):
    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    search_fields = ['title']
    list_filter = ['created']
    date_hierarchy = 'created'

admin.site.register(Post,PostAdmin)
