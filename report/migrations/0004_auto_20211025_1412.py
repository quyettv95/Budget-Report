# Generated by Django 3.2.4 on 2021-10-25 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_remove_reportitem_isparent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportitem',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='reportitem',
            name='month',
        ),
        migrations.RemoveField(
            model_name='reportitem',
            name='reporter',
        ),
        migrations.RemoveField(
            model_name='reportitem',
            name='year',
        ),
        migrations.CreateModel(
            name='BudgetTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(verbose_name='Tháng')),
                ('year', models.IntegerField(verbose_name='Năm')),
                ('amount', models.IntegerField(verbose_name='Số lượng')),
                ('reportItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.reportitem')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.reporter', verbose_name='Reporter')),
            ],
        ),
    ]
