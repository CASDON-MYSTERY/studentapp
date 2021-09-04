# Generated by Django 3.1.5 on 2021-09-04 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('associations', '0001_initial'),
        ('faculties', '0001_initial'),
        ('departments', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('institutions', '0001_initial'),
        ('sets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('rating', models.FloatField(blank=True, default=0.0, verbose_name='rating')),
                ('is_institution_admin', models.BooleanField(default=False)),
                ('is_faculty_admin', models.BooleanField(default=False)),
                ('is_department_admin', models.BooleanField(default=False)),
                ('is_set_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('staff', models.BooleanField(default=False)),
                ('association_admin', models.ManyToManyField(related_name='association_admin', to='associations.Association')),
                ('associations', models.ManyToManyField(related_name='user_associations', to='associations.Association')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_department', to='departments.department')),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_faculty', to='faculties.faculty')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_institution', to='institutions.institution')),
                ('set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='set', to='sets.set')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
