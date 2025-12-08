from django.contrib import admin
from learning_logs.models import Topic, Entry
# Register your models here.

admin.site.site_header="Learning Log"
admin.site.site_title="Learning log"
admin.site.index_title="Welcome To The Learning Log"
@admin.register(Topic)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('topic_name', 'date_added')
    search_fields = ('topic_name',)
    

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = [
        'topic',
        'entry',
        'date_added'
        ]
    
    





