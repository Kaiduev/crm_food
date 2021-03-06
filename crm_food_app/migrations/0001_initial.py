# Generated by Django 3.0.4 on 2020-04-09 17:05

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('surname', models.CharField(max_length=255)),
                ('login', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(max_length=255)),
                ('role', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='crm_food_app.Role')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, django.contrib.auth.models.AnonymousUser),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isitopen', models.BooleanField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('table', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='crm_food_app.Table')),
                ('waiter', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='crm_food_app.User')),
            ],
            options={
                'ordering': ['waiter'],
            },
        ),
        migrations.CreateModel(
            name='MealsToOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='crm_food_app.Order')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='MealOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('meal', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='crm_food_app.Meal')),
                ('mealstooerder', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='crm_food_app.MealsToOrder')),
                ('order', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='meal', to='crm_food_app.Order')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='MealCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm_food_app.Department', verbose_name='Department')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='meal',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm_food_app.MealCategory', verbose_name='MealCategory'),
        ),
        migrations.CreateModel(
            name='CheckOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('servicefree', models.IntegerField(default=20)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm_food_app.Order')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='CheckedMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_fk', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='checks', to='crm_food_app.CheckOrder')),
                ('meal', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='crm_food_app.Meal')),
                ('mealorder', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='crm_food_app.MealOrder')),
            ],
        ),
    ]
