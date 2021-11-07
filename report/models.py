from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class Segment(models.Model):
  segmentCode = models.CharField(verbose_name="Mã cơ sở", max_length=255)
  segmentName = models.CharField(verbose_name="Tên cơ sở", max_length=255)

  def __str__(self):
    return self.segmentName


class CostCenterCategory(models.Model):
  name = models.CharField(max_length=255)
  code = models.CharField(max_length=255)

  def __str__(self) -> str:
    return self.name


class CostCenter(models.Model):
  costCenterCode = models.CharField(verbose_name="Mã phòng ban", max_length=255)
  costCenterName = models.CharField(verbose_name="Tên phòng ban", max_length=255)
  segment = models.ForeignKey(Segment, verbose_name="Cơ sở", on_delete=models.CASCADE)
  costCenterCategory = models.ForeignKey(CostCenterCategory, verbose_name="Danh mục Costcenter", on_delete=CASCADE, null=True)
  def __str__(self) -> str:
    return self.segment.segmentName + " --> " + self.costCenterName



class RoleChoices(models.IntegerChoices):
  Admin = 1
  General_Manager = 2
  Head_of_Department = 3
class Reporter(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  costCenter = models.ForeignKey(CostCenter, verbose_name="Phòng ban", on_delete=CASCADE, null=True)
  role = models.IntegerField(verbose_name="Phân quyền", choices=RoleChoices.choices)


class ReportItem(models.Model):
  reportItemCode = models.CharField(verbose_name="Mã báo cáo", max_length=255)
  reportItemName = models.CharField(verbose_name="Tên báo cáo", max_length=255)
  formular = models.CharField(verbose_name="Công thức", max_length=255, null=True, blank=True)
  parent = models.ForeignKey(
    'self',
    null=True,
    blank=True,
    related_name='children',
    on_delete=models.CASCADE,
    verbose_name="Danh mục cha"
  )
  costCenterCategory = models.ForeignKey(CostCenterCategory, on_delete=CASCADE, null=True, verbose_name="Nhóm Costcenter")

  def __str__(self) -> str:
    return self.costCenterCategory.name + "-->" + self.reportItemName


class BudgetTransaction(models.Model):
  reportItem = models.ForeignKey(ReportItem, on_delete=models.CASCADE)
  month = models.IntegerField(verbose_name="Tháng")
  year = models.IntegerField(verbose_name="Năm")
  amount = models.IntegerField(verbose_name="Số lượng")
  reporter = models.ForeignKey(Reporter, verbose_name="Reporter", on_delete=models.CASCADE)
  costCenter = models.ForeignKey(CostCenter, verbose_name="Cost Center", on_delete=models.CASCADE, null= True)

# 1. Customize thông tin user
# 2. Download file excel chứa các thông tin báo cáo về cơ sở
# 3. Import file excel đã được chỉnh sửa số liệu
# 4. Hiển thị & export dữ liệu sau khi hoàn tất nhập liệu
