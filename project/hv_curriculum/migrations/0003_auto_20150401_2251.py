# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hv_curriculum', '0002_auto_20150401_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='display_coach_welcome_video',
        ),
        migrations.AddField(
            model_name='page',
            name='display_trainer_welcome_video',
            field=models.BooleanField(default=False, help_text=b"By checking this the coach will see their trainer's welcome video if available."),
            preserve_default=True,
        ),
    ]
