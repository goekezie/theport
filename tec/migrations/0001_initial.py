# Generated by Django 3.1.6 on 2021-02-25 20:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TechPost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(blank=True, default=0)),
                ('image', models.ImageField(blank=True, upload_to='tech/images/')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=True)),
                ('image', models.ImageField(default='dev/images/tech.png', upload_to='tech/images/')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='tec.comment')),
                ('techpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tec.techpost')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
