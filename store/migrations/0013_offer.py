# Generated by Django 4.0.4 on 2022-05-26 05:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='offer',
            fields=[
                ('per', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Timestamp', models.DateTimeField()),
                ('Discount', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='coustomer', to='store.customer')),
                ('leave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            options={
                'db_table': 'offer',
            },
        ),
    ]
