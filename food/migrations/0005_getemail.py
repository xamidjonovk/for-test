# Generated by Django 3.2 on 2021-06-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_alter_step_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=150)),
            ],
        ),
    ]
