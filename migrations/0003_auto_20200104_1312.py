# Generated by Django 3.0 on 2020-01-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0002_auto_20200104_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AddConstraint(
            model_name='name',
            constraint=models.UniqueConstraint(fields=('name', 'boy'), name='Name, Sex Unique Constraint'),
        ),
    ]
