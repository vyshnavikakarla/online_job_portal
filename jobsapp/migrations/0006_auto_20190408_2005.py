from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0005_applicant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='jobsapp.Job'),
        ),
    ]