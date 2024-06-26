# Generated by Django 5.0.4 on 2024-04-08 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fichaname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exercparametros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('serie', models.IntegerField(default=3, null=True)),
                ('repetmin', models.IntegerField(blank=True, default=10, null=True)),
                ('repetmax', models.IntegerField(blank=True, default=12, null=True)),
                ('pesomin', models.IntegerField(blank=True, null=True)),
                ('pesomax', models.IntegerField(blank=True, null=True)),
                ('ficha', models.ManyToManyField(to='api.fichaname')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True, null=True)),
                ('peso', models.IntegerField(blank=True, null=True)),
                ('exerc', models.ManyToManyField(to='api.exercparametros')),
            ],
        ),
    ]
