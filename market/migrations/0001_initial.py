# Generated by Django 3.2.8 on 2022-01-01 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalMarketData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open', models.FloatField()),
                ('close', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('volume', models.IntegerField()),
                ('trading_date', models.DateField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.company')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentMarketData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('updated_at', models.DateTimeField(verbose_name='Last updated at')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.company')),
            ],
        ),
        migrations.AddConstraint(
            model_name='company',
            constraint=models.UniqueConstraint(fields=('symbol',), name='unique_symbol'),
        ),
        migrations.AlterUniqueTogether(
            name='historicalmarketdata',
            unique_together={('stock', 'trading_date')},
        ),
        migrations.AddConstraint(
            model_name='currentmarketdata',
            constraint=models.UniqueConstraint(fields=('stock',), name='unique_stock'),
        ),
    ]
