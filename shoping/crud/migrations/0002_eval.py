# Generated by Django 3.0.5 on 2020-04-30 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
                ('lect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Lecture')),
            ],
        ),
    ]