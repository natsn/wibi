# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import utils.mixins


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=1000)),
                ('feedback', models.CharField(max_length=1000, blank=True)),
                ('correct', models.BooleanField(default=False, help_text=b'Is this a correct answer?')),
                ('position', models.IntegerField()),
                ('es_text', models.CharField(max_length=1000)),
                ('es_feedback', models.CharField(max_length=1000, blank=True)),
            ],
            options={
                'ordering': ['position'],
            },
            bases=(models.Model, utils.mixins.TranslatedModelMixin),
        ),
        migrations.CreateModel(
            name='CustomPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('html', models.TextField()),
                ('es_html', models.TextField()),
            ],
            options={
            },
            bases=(models.Model, utils.mixins.TranslatedModelMixin),
        ),
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('es_title', models.CharField(max_length=255)),
                ('position', models.IntegerField(default=1, help_text=b'What level/session is this?')),
            ],
            options={
                'ordering': ('position',),
            },
            bases=(models.Model, utils.mixins.TranslatedModelMixin),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('html', models.TextField()),
                ('image', models.FileField(upload_to=b'page_images')),
                ('video', models.FileField(upload_to=b'page_videos')),
                ('audio', models.FileField(upload_to=b'page_audio')),
                ('display_coach_welcome_video', models.BooleanField(default=False, help_text=b"By checking this the participant will see their coach's welcome video if available.")),
                ('es_title', models.CharField(max_length=255)),
                ('es_html', models.TextField()),
                ('es_image', models.FileField(upload_to=b'page_images')),
                ('es_video', models.FileField(upload_to=b'page_videos')),
                ('es_audio', models.FileField(upload_to=b'page_audio')),
                ('level', models.ForeignKey(to='pals_curriculum.Level')),
            ],
            options={
            },
            bases=(models.Model, utils.mixins.TranslatedModelMixin),
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('page', models.ForeignKey(to='pals_curriculum.Page')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=1000)),
                ('type', models.CharField(max_length=2, choices=[(b'ra', b'radio'), (b'ch', b'checkbox'), (b'tx', b'text')])),
                ('is_scoreable', models.BooleanField(default=True, help_text=b'Will the answer to this question be scored?')),
                ('position', models.IntegerField()),
                ('es_text', models.CharField(max_length=1000)),
                ('page', models.ForeignKey(to='pals_curriculum.Page')),
            ],
            options={
                'ordering': ['position'],
            },
            bases=(models.Model, utils.mixins.TranslatedModelMixin),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choices', models.CommaSeparatedIntegerField(max_length=255)),
                ('free', models.TextField()),
                ('attempt', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(to='pals_curriculum.Question')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('es_title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model, utils.mixins.TranslatedModelMixin),
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255)),
                ('es_text', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model, utils.mixins.TranslatedModelMixin),
        ),
        migrations.AddField(
            model_name='page',
            name='section',
            field=models.ForeignKey(to='pals_curriculum.Section'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='edge',
            name='u',
            field=models.ForeignKey(related_name='from_page', to='pals_curriculum.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='edge',
            name='v',
            field=models.ForeignKey(related_name='to_page', to='pals_curriculum.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='pals_curriculum.Question'),
            preserve_default=True,
        ),
    ]
