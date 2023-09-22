# Generated by Django 4.2.5 on 2023-09-13 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_category_remove_transaction_source_transaction_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('+', 'Income'), ('-', 'Expense')], default='-', max_length=1),
        ),
    ]