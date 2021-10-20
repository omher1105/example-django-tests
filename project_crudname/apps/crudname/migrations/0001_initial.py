# Generated by Django 3.1.13 on 2021-10-20 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crudname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this record should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('creation_date', models.DateTimeField(auto_now_add=True, help_text='record creation date', verbose_name='creation date')),
                ('created_by', models.CharField(help_text='username that created the record', max_length=100, verbose_name='username created')),
                ('update_date', models.DateTimeField(auto_now=True, help_text='record update date', verbose_name='update date')),
                ('update_by', models.CharField(help_text='username that updated the record', max_length=100, verbose_name='username updated')),
                ('name', models.CharField(blank=True, default=None, help_text='Name of the choice.', max_length=200, null=True, verbose_name='name')),
                ('code', models.CharField(blank=True, default=None, help_text='Code.', max_length=20, null=True, verbose_name='code')),
            ],
            options={
                'verbose_name': 'crudname',
                'verbose_name_plural': 'crudnames',
                'db_table': 'crudname',
                'ordering': ['id'],
            },
        ),
    ]