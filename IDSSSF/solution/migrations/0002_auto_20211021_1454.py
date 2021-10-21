# Generated by Django 3.2.8 on 2021-10-21 14:54

from django.db import migrations, models
import solution.models


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solutionmodel',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='solutionmodel',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='solutionmodel',
            name='owner',
        ),
        migrations.AddField(
            model_name='solutionmodel',
            name='about',
            field=models.CharField(default=None, max_length=5000),
        ),
        migrations.AddField(
            model_name='solutionmodel',
            name='caution',
            field=models.JSONField(default=solution.models.SolutionModel.caution_default),
        ),
        migrations.AddField(
            model_name='solutionmodel',
            name='medicine',
            field=models.JSONField(default=solution.models.SolutionModel.medicine_default),
        ),
        migrations.AlterField(
            model_name='solutionmodel',
            name='prevent',
            field=models.JSONField(default=solution.models.SolutionModel.prevent_default),
        ),
    ]
