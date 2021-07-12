from django.contrib import admin
from .models import Resume , Feedback

# @admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    

    list_display = ('Full_name', 'date', 'Comments',)
    search_fields = ('details',)

    class Meta:
        model = Feedback


admin.site.register(Feedback, ResumeAdmin)

pass