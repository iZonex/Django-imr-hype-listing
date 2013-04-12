from modeltranslation.translator import translator, TranslationOptions

from news.models import Post

class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)
    fallback_values = {'title': 'no data'}

translator.register(Post, PostTranslationOptions)

# import translation.py from other apps if they provide translation registry
# import app1.translation