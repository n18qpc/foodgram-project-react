# Generated by Django 3.0.5 on 2021-08-01 13:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_auto_20210801_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Картинка')),
                ('text', models.TextField(verbose_name='Рецепт')),
                ('cooking_time', models.PositiveSmallIntegerField(default=1, verbose_name='Время приготовления')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.RenameModel(
            old_name='FollowModel',
            new_name='Follow',
        ),
        migrations.RenameModel(
            old_name='AddIngredientInRecModel',
            new_name='AddIngredientInRec',
        ),
        migrations.RenameModel(
            old_name='FavoriteRecipeModel',
            new_name='FavoriteRecipe',
        ),
        migrations.RenameModel(
            old_name='IngredientModel',
            new_name='Ingredient',
        ),
        migrations.RenameModel(
            old_name='ShoppingListModel',
            new_name='ShoppingList',
        ),
        migrations.RenameModel(
            old_name='TagModel',
            new_name='Tag',
        ),
        migrations.DeleteModel(
            name='RecipeModel',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', through='recipes.AddIngredientInRec', to='recipes.Ingredient', verbose_name='Ингредиенты'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(related_name='recipes', to='recipes.Tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='addingredientinrec',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amounts', to='recipes.Recipe', verbose_name='Сам рецепт'),
        ),
        migrations.AlterField(
            model_name='favoriterecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_favorited', to='recipes.Recipe', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_in_shopping_cart', to='recipes.Recipe', verbose_name='Рецепт для покупки'),
        ),
    ]
