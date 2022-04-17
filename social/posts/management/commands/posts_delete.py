from datetime import timedelta

from django.core.management import BaseCommand
from django.utils import timezone

from posts.models import Post


class Command(BaseCommand):
    help = "Delete posts 'datetime ago'"

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument('--days', type=int)
        parser.add_argument('--hours', type=int)
        parser.add_argument('--min', type=int)
        parser.add_argument('--sec', type=int)

    def handle(self, *args, **kwargs):
        arg_days = kwargs['days'] or 0
        arg_hours = kwargs['hours'] or 0
        arg_min = kwargs['min'] or 0
        arg_sec = kwargs['sec'] or 0

        if (arg_days == 0) and (arg_hours == 0) and (arg_min == 0) and (arg_sec == 0):
            arg_days = 50

        datetime = timezone.now() - timedelta(days=arg_days, hours=arg_hours, minutes=arg_min, seconds=arg_sec)

        posts = Post.objects.filter(created_at__lt=datetime)
        result = posts.delete()

        self.stdout.write(f'{datetime} - deleted info :{result}')
        self.stdout.write(f'd:{arg_days}-h:{arg_hours}-m:{arg_min}-s:{arg_sec} - deleted info :{result}')
