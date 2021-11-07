from django.contrib import admin
from django.contrib.auth import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from report.models import CostCenterCategory, Segment
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

class SegmentAdmin(admin.ModelAdmin):
  list_display = ('segmentCode', 'segmentName')

class CostCenterAdmin(admin.ModelAdmin):
  list_display = (
    'costCenterCode',
    'costCenterName',
    'segment',
    'costCenterCategory',
  )

class ReportItemAdmin(admin.ModelAdmin):
  list_display = (
    'reportItemCode',
    'reportItemName',
    'formular',
    'parent',
    'costCenterCategory',
  )

class CostCenterCategoryAdmin(admin.ModelAdmin):
  list_display = (
    'name',
    'code',
  )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Reporter)
admin.site.register(Segment, SegmentAdmin)
admin.site.register(CostCenter, CostCenterAdmin)
admin.site.register(ReportItem, ReportItemAdmin)
admin.site.register(CostCenterCategory, CostCenterCategoryAdmin)