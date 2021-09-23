from django.contrib import admin
from .models import Question,Choice
# Register your models here.
@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display=['question_text','pub_date']
@admin.register(Choice)
class ChoiceModelAdmin(admin.ModelAdmin):
    list_display=['choice_text','question','votes']
    
    def question(self, obj):
        return obj.choice.question
    question.admin_order_field  = 'choice__question'