# Generated by Django 3.2.6 on 2022-01-11 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User_app', '0002_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='User_app.user'),
        ),
    ]