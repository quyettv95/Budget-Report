from django.db import models

# Create your models here.

class Segment(models.Model):
  segmentCode = models.CharField(verbose_name="Mã cơ sở")
  segmentName = models.CharField(verbose_name="Tên cơ sở")

class CostCenter(models.Model):
  costCenterCode = models.CharField(verbose_name="Mã phòng ban")
  costCenterName = models.CharField(verbose_name="Tên phòng ban")
  segment = models.ForeignKey(Segment, verbose_name="Cơ sở")

class Reporter(models.Model):
  role = models.IntegerField(verbose_name="Phân quyền")

class ReportItem(models.Model):
  reportItemCode = models.CharField(verbose_name="Mã báo cáo")
  reportItemName = models.CharField(verbose_name="Tên báo cáo")
  amount = models.IntegerField(verbose_name="Số lượng")
  formular = models.CharField(verbose_name="Công thức")
  isParent = models.BooleanField(verbose_name="Là parent?")
  month = models.IntegerField(verbose_name="Tháng")
  year = models.IntegerField(verbose_name="Năm")
  costCenter = models.ForeignKey(CostCenter, verbose_name="Cost Center")
  reporter = models.ForeignKey(CostCenter, verbose_name="Cost Center")


# 1. Customize thông tin user
# 2. Download file excel chứa các thông tin báo cáo về cơ sở
# 3. Import file excel đã được chỉnh sửa số liệu
# 4. Hiển thị & export dữ liệu sau khi hoàn tất nhập liệu
