# Generated by Django 3.0.5 on 2021-08-01 10:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglistmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_in_shopping_cart', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель'),
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', through='recipes.AddIngredientInRecModel', to='recipes.IngredientModel', verbose_name='Ингредиенты'),
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='tags',
            field=models.ManyToManyField(related_name='recipes', to='recipes.TagModel', verbose_name='Теги'),
        ),
        migrations.AddField(
            model_name='followmodel',
            name='author',
            field=models.ForeignKey(help_text='На кого подписываются', on_delete=django.db.models.deletion.CASCADE, related_name='subscriber', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='followmodel',
            name='user',
            field=models.ForeignKey(help_text='Кто подписывается', on_delete=django.db.models.deletion.CASCADE, related_name='subscribed_on', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favoriterecipemodel',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_favorited', to='recipes.RecipeModel', verbose_name='Рецепт'),
        ),
        migrations.AddField(
            model_name='favoriterecipemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_favorited', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='addingredientinrecmodel',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amounts', to='recipes.IngredientModel', verbose_name='Ингридиент для рецепта'),
        ),
        migrations.AddField(
            model_name='addingredientinrecmodel',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amounts', to='recipes.RecipeModel', verbose_name='Сам рецепт'),
        ),
        migrations.AddConstraint(
            model_name='shoppinglistmodel',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='cart_user_recept_unique'),
        ),
        migrations.AddConstraint(
            model_name='followmodel',
            constraint=models.UniqueConstraint(fields=('user', 'author'), name='subscribe'),
        ),
        migrations.AddConstraint(
            model_name='favoriterecipemodel',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='user_recept_unique'),
        ),
        migrations.AddConstraint(
            model_name='addingredientinrecmodel',
            constraint=models.UniqueConstraint(fields=('recipe', 'ingredient'), name='recipe_ingredient_unique'),
        ),
    ]
