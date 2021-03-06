# Generated by Django 3.2.4 on 2021-10-25 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CostCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costCenterCode', models.CharField(max_length=255, verbose_name='Mã phòng ban')),
                ('costCenterName', models.CharField(max_length=255, verbose_name='Tên phòng ban')),
            ],
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField(verbose_name='Phân quyền')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segmentCode', models.CharField(max_length=255, verbose_name='Mã cơ sở')),
                ('segmentName', models.CharField(max_length=255, verbose_name='Tên cơ sở')),
            ],
        ),
        migrations.CreateModel(
            name='ReportItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportItemCode', models.CharField(max_length=255, verbose_name='Mã báo cáo')),
                ('reportItemName', models.CharField(max_length=255, verbose_name='Tên báo cáo')),
                ('amount', models.IntegerField(verbose_name='Số lượng')),
                ('formular', models.CharField(max_length=255, verbose_name='Công thức')),
                ('isParent', models.BooleanField(verbose_name='Là parent?')),
                ('month', models.IntegerField(verbose_name='Tháng')),
                ('year', models.IntegerField(verbose_name='Năm')),
                ('costCenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.costcenter', verbose_name='Cost Center')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.reporter', verbose_name='Reporter')),
            ],
        ),
        migrations.AddField(
            model_name='costcenter',
            name='segment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.segment', verbose_name='Cơ sở'),
        ),
    ]
