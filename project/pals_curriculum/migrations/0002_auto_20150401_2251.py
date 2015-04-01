# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pals_curriculum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='audio',
        ),
        migrations.RemoveField(
            model_name='page',
            name='es_audio',
        ),
        migrations.RemoveField(
            model_name='page',
            name='es_image',
        ),
        migrations.RemoveField(
            model_name='page',
            name='es_video',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image',
        ),
        migrations.RemoveField(
            model_name='page',
            name='video',
        ),
    ]
