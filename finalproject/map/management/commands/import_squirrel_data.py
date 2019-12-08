from django.core.management.base import BaseCommand, CommandError
from map.models import Squirrel

class Command(BaseCommand):
    help = 'import the squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        for path in options['path']:
            f = open('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv', 'r')
            for line in f:
                args = line.split(',')
                if args[0] != 'X':
                    longitude = args[0]
                    latitude = args[1]
                    unique_id = args[2]
                    shift=args[4]
                    date=args[5][4:]+'-'+args[5][:2]+'-'+args[5][2:4]
                    age =args[7]
                    primary_fur_color=args[8]
                    location=args[12]
                    specific_location=args[14]



                    running = True if args[15].lower()=='true' else False
                    chasing = True if args[16].lower()=='true' else False
                    climbing = True if args[17].lower()=='true' else False
                    eating = True if args[18].lower()=='true' else False
                    foraging = True if args[19].lower()=='true' else False
                    other_activities = args[20]
                    kuks = True if args[21].lower()=='true' else False
                    quaas = True if args[22].lower()=='true' else False
                    moans = True if args[23].lower()=='true' else False
                    tail_flags = True if args[24].lower()=='true' else False
                    tail_twitches = True if args[25].lower()=='true' else False
                    approaches = True if args[26].lower()=='true' else False
                    indifferent = True if args[27].lower()=='true' else False
                    runs_from = True if args[28].lower()=='true' else False
                    Squirrel.objects.create(
                        latitude=latitude, 
                        longitude=longitude,
                        unique_squirrel_id=unique_id,
                        shift=shift,
                        date=date,
                        age=age,
                        primary_fur_color=primary_fur_color,
                        location=location,
                        specific_location=specific_location,
                        running=running,
                        chasing=chasing,
                        climbing=climbing,
                        eating=eating,
                        foraging=foraging,
                        other_activities=other_activities,
                        kuks=kuks,
                        quaas=quaas,
                        moans=moans,
                        tail_twitches=tail_twitches,
                        tail_flags=tail_flags,
                        approaches=approaches,
                        indifferent=indifferent,
                        runs_from=runs_from
                        )

