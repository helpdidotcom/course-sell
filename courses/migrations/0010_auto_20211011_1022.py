# Generated by Django 3.2.7 on 2021-10-11 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0009_auto_20211009_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='date',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='usercourse',
            old_name='date',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='course',
        ),
        migrations.AlterField(
            model_name='payment',
            name='order_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
