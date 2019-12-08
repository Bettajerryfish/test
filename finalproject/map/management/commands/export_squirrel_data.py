import csv
from django.core.management import BaseCommand
from django.utils.encoding import smart_str
from map.models import Squirrel
class Command(BaseCommand):
    help = 'Export the data'
    def add_arguments(self, parser):
        parser.add_argument('positionArg')
    def handle(self,*args,**kargs):
        path=kargs['positionArg']
        with open(path, 'w', newline='') as csvfile:
            result=csv.writer(csvfile)
            result.writerow([
                smart_str(u"Latitude"),
                smart_str(u"Longitude"),
                smart_str(u"Unique Squirrel ID"),
                smart_str(u"Shift"),
                smart_str(u"Date"),
                smart_str(u"Age"),
                smart_str(u"Primary Fur Color"),
                smart_str(u"Location"),
                smart_str(u"Specific Location"),
                smart_str(u"Running"),
                smart_str(u"Chasing"),
                smart_str(u"Climbing"),
                smart_str(u"Eating"),
                smart_str(u"Foraging"),
                smart_str(u"Other Activities"),
                smart_str(u"Kuks"),
                smart_str(u"Quaas"),
                smart_str(u"Moans"),
                smart_str(u"Tail flags"),
                smart_str(u"Tail twitches"),
                smart_str(u"Approaches"),
                smart_str(u"Indifferent"),
                smart_str(u"Runs_from"),    
                ])
            for i in Squirrel.objects.values():
                result.writerow([
                    smart_str(i["longitude"]),
                    smart_str(i["latitude"]),
                    smart_str(i['unique_squirrel_id']),
                    smart_str(i["shift"]),
                    smart_str(i["date"]),
                    smart_str(i["age"]),
                    smart_str(i["primary_fur_color"]),
                    smart_str(i["location"]),
                    smart_str(i["specific_location"]),
                    smart_str(i["running"]),
                    smart_str(i["chasing"]),
                    smart_str(i["climbing"]),
                    smart_str(i["eating"]),
                    smart_str(i["foraging"]),
                    smart_str(i["other_activities"]),
                    smart_str(i["kuks"]),
                    smart_str(i["quaas"]),
                    smart_str(i["moans"]),
                    smart_str(i["tail_flags"]),
                    smart_str(i["tail_twitches"]),
                    smart_str(i["approaches"]),
                    smart_str(i["indifferent"]),
                    smart_str(i["runs_from"]),
                    ])
