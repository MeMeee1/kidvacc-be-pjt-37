<<<<<<< HEAD
# Generated by Django 3.2 on 2021-07-09 06:59
=======
# Generated by Django 3.2.4 on 2021-07-05 08:14
>>>>>>> e70e3fac976cc3bdc4c71f1d3b6437393e7635d0

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_auto_20210703_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
