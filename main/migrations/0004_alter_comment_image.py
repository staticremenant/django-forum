# Generated by Django 4.1.3 on 2022-11-25 11:22

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_comment_content_alter_post_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='images/%Y/%m/%d/', validators=[main.validators.validate_file_size]),
        ),
    ]
