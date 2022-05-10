# Generated by Django 4.0.2 on 2022-05-04 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_club_account_number_club_discount'),
        ('films', '0004_remove_bookedtickets_booking_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_title', models.CharField(max_length=50)),
                ('account_discount', models.BigIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_cost', models.IntegerField()),
                ('number_of_tickets', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CardDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.BigIntegerField()),
                ('expiry_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LoginTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_payment', models.DateTimeField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookings.account')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookings.booking')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.club')),
            ],
        ),
        migrations.CreateModel(
            name='GuessTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_payment', models.DateTimeField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookings.booking')),
                ('card_details', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='bookings.carddetails')),
            ],
        ),
        migrations.CreateModel(
            name='BookedTickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.booking')),
                ('screen_showing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.showing')),
                ('ticket_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.tickettype')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='card_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookings.carddetails'),
        ),
    ]
