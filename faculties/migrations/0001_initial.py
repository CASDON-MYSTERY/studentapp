# Generated by Django 3.1.5 on 2021-09-04 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        ('institutions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('grouped_events', models.ManyToManyField(related_name='faculty_events', to='events.Grouped_Events')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institution', to='institutions.institution')),
                ('single_events', models.ManyToManyField(related_name='faculty_single_events', to='events.Single_Event')),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculties',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
