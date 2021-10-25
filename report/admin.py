from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from report.models import Segment
from report.models import CostCenter
from report.models import ReportItem
from report.models import Reporter
from django.contrib.auth.models import User

# Register your models here.
class ReporterInline(admin.StackedInline):
  model = Reporter
  can_delete = False
  verbose_name_plural = 'Reporters'

class UserAdmin(BaseUserAdmin):
  inlines = (ReporterInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Reporter)
admin.site.register(Segment)
admin.site.register(CostCenter)
admin.site.register(ReportItem)