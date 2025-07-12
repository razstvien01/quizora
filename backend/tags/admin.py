from django.contrib import admin
from tags.models.mock_quiz_tag import MockQuizTag
from tags.models.tag import Tag

admin.site.register(MockQuizTag)
admin.site.register(Tag)