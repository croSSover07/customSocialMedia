# Generated by Django 4.0.2 on 2022-03-14 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_comment_id_alter_post_id_alter_postcategory_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='posts.PostCategory'),
        ),
    ]