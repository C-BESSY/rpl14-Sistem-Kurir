# Generated by Django 4.1.7 on 2023-04-24 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_userid_admin_id_amin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='id_Amin',
            new_name='id_admin',
        ),
    ]