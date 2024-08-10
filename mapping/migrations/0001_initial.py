# Generated by Django 4.2.5 on 2024-01-10 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('interest', models.BooleanField(default=False, verbose_name="Définir point d'interêt")),
                ('description', models.TextField(blank=True, null=True, verbose_name="Description de l'adresse")),
            ],
        ),
        migrations.CreateModel(
            name='AddressType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=40, verbose_name='Nom de la catégorie')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': "Catégorie d'adresse",
                'verbose_name_plural': "Catégories d'adresses",
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mapping.address')),
                ('name', models.CharField(max_length=100, verbose_name='Nom du batîment/bureau')),
                ('localnum', models.IntegerField(blank=True, default=0, null=True, verbose_name='Nombre de locaux')),
                ('burnum', models.IntegerField(blank=True, default=0, null=True, verbose_name='Nombre de bureaux')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Batîment',
                'verbose_name_plural': 'Batîments',
            },
            bases=('mapping.address',),
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mapping.address')),
                ('name', models.CharField(max_length=100, verbose_name="Nom de l'espace")),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Espace',
                'verbose_name_plural': 'Espaces',
            },
            bases=('mapping.address',),
        ),
        migrations.AddField(
            model_name='address',
            name='adtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.addresstype', verbose_name="Catégorie de l'adresse"),
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mapping.address')),
                ('name', models.CharField(max_length=100, verbose_name="Nom de l'office")),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('officebur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.building', verbose_name='Son bureau')),
            ],
            options={
                'verbose_name': 'Office',
                'verbose_name_plural': 'Offices',
            },
            bases=('mapping.address',),
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mapping.address')),
                ('name', models.CharField(max_length=100, verbose_name='Nom du Local')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('burbuilding', models.ForeignKey(blank=True, default='Aucun', null=True, on_delete=django.db.models.deletion.CASCADE, to='mapping.building', verbose_name='Son batîment')),
            ],
            options={
                'verbose_name': 'Local/Salle',
                'verbose_name_plural': 'Locaux/Salles',
            },
            bases=('mapping.address',),
        ),
        migrations.CreateModel(
            name='Bureau',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mapping.address')),
                ('name', models.CharField(max_length=100, verbose_name='Nom du Bureau')),
                ('hallnum', models.IntegerField(blank=True, default=0, null=True, verbose_name="Nombre d'office")),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('burbuilding', models.ForeignKey(blank=True, default='Aucun', null=True, on_delete=django.db.models.deletion.CASCADE, to='mapping.building', verbose_name='Son batîment')),
            ],
            options={
                'verbose_name': 'Bureau',
                'verbose_name_plural': 'Bureaux',
            },
            bases=('mapping.address',),
        ),
    ]
