from itertools import product
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from quiz.models import Pattern, LeitnerBox


class Command(BaseCommand):
    help = 'Initialize leitner box db with all patterns in box zero'
    
    
    def handle(self, *args, **kwargs):
        users = list(User.objects.all())
        patterns = list(Pattern.objects.all())
        zipped = list(product(users, patterns))
        boxes = [
            LeitnerBox(
                user=z[0],
                pattern=z[1],
                box_number=0
            ) for z in zipped
        ]
        LeitnerBox.objects.bulk_create(boxes, ignore_conflicts=True)
