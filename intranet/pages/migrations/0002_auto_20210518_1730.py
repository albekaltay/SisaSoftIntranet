# Generated by Django 3.1.7 on 2021-05-18 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdocuments3',
            name='userId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='userdocuments2',
            name='documentNumber',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pages.checklist2', verbose_name='İşlem'),
        ),
        migrations.AddField(
            model_name='userdocuments2',
            name='userId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='userdocuments',
            name='documentNumber',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pages.checklist', verbose_name='İşlem'),
        ),
        migrations.AddField(
            model_name='userdocuments',
            name='userId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Email'),
        ),
    ]
