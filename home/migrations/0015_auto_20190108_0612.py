# Generated by Django 2.1.4 on 2019-01-08 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20190108_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapply',
            name='alt_contact_no',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='contact_no',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='endtdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='pincode',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='startdate',
            field=models.DateField(),
        ),
    ]
