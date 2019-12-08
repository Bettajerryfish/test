from django.db import models

from django.utils.translation import gettext as _

# Create your models here.
class Squirrel(models.Model):

	latitude = models.FloatField(
		help_text='latitude',
		)

	longitude = models.FloatField(
		help_text='longitude',
		)

	unique_squirrel_id = models.CharField(
		help_text='unique_squirrel_id',
		max_length=32,
		)
	AM='Am'
	PM='Pm'
	shift = models.CharField(
		help_text='shift',
		max_length=16,
		choices=(
			(AM,'AM'),
			(PM,'PM'),
			),
		)

	date = models.DateField(
		help_text='date',
		)
	Adult='Adult'
	Juvenile='Juvenile'
	age_choice=(
		(Adult,"Adult"),
		(Juvenile,"Juvenile"),
		)
	age = models.CharField(
		help_text='age',
		max_length=16,
		choices=age_choice,
		)

	Gray='Gray'
	Black='Black'
	Cinnamon='Cinnamon'
	primary_fur_color_choice=(
		(Gray,'Gray'),
		(Black,'Black'),
		(Cinnamon,'Cinnamon'),
		)
	primary_fur_color=models.CharField(
		help_text='primary fur color',
		max_length=30,
		choices=primary_fur_color_choice,
		)

	Ground_Plane='Ground Plane'
	Above_Ground='Above Ground'
	location_choice=(
		(Ground_Plane,'Ground Plan'),
		(Above_Ground,'Above Ground'),
		)
	location=models.CharField(
		help_text='location',
		max_length=100,
		choices=location_choice,
		)

	specific_location=models.CharField(
                max_length=100,
		help_text='specific_location',
		)

	running=models.BooleanField(
		help_text='running',
                blank=True, null=True,
                )

	chasing=models.BooleanField(
		help_text='chasing',
                blank=True, null=True,
		)

	climbing=models.BooleanField(
		help_text='climbing',
                blank=True, null=True,
		)

	eating=models.BooleanField(
		help_text='eating',
                blank=True, null=True,
		)

	foraging=models.BooleanField(
		help_text='foraging',
                blank=True, null=True,
		)

	other_activities=models.CharField(
		max_length=100,
                help_text='other_activities',
		)

	kuks=models.BooleanField(
		help_text='kuks',
                blank=True, null=True,
		)

	quaas=models.BooleanField(
		help_text='quaas',
                blank=True, null=True,
		)

	moans=models.BooleanField(
		help_text='moans',
                blank=True, null=True,
		)

	tail_flags=models.BooleanField(
		help_text='tail_flags',
                blank=True, null=True,
		)

	tail_twitches=models.BooleanField(
		help_text='tail_twitches',
                blank=True, null=True,
		)

	approaches=models.BooleanField(
		help_text='approaches',
                blank=True, null=True
		)

	indifferent=models.BooleanField(
		help_text='indifferent',
                blank=True, null=True
		)

	runs_from=models.BooleanField(
		help_text='runs from',
                blank=True, null=True,
		)

	def __str__(self):
		return self.unique_squirrel_id

# Create your models here.
