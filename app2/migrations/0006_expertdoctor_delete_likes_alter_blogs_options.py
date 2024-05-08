# Generated by Django 5.0.1 on 2024-03-25 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0005_likes_remove_comments_img_profile_img_medical_one_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='photo', verbose_name='img')),
                ('nameDoctor', models.CharField(max_length=40)),
                ('aboutDoctor', models.CharField(max_length=50, verbose_name='about you')),
                ('adressDoctor', models.CharField(max_length=50, verbose_name='adress')),
                ('ExpertIn', models.CharField(blank=True, choices=[('Obesity and endoscopic surgery', 'Obesity and endoscopic surgery'), ('Heart and blood vessels', 'Heart and blood vessels'), ('Blood diseases', 'Blood diseases'), ('Bones', 'Bones'), ('Gynecology and Obstetrics', 'Gynecology and Obstetrics'), ('Newborn babies', 'Newborn babies'), ('teeth', 'teeth'), ('Newborn babies', 'Newborn babies'), ('Nose, Ear and Throat', 'Nose, Ear and Throat'), ('Tumors', 'Tumors')], max_length=50, null=True, verbose_name='doctor_in?')),
                ('facebook', models.CharField(blank=True, max_length=50, null=True, verbose_name='facebook')),
                ('google', models.CharField(blank=True, max_length=50, null=True, verbose_name='google')),
                ('twitter', models.CharField(blank=True, max_length=50, null=True, verbose_name='twitter')),
            ],
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
        migrations.AlterModelOptions(
            name='blogs',
            options={'verbose_name': 'blogs', 'verbose_name_plural': 'blogs'},
        ),
    ]
