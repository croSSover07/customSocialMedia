from django.core.management import BaseCommand
from django.utils import timezone

from posts.models import Post


class Command(BaseCommand):
    help = 'Displays current time and count of posts'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        posts = Post.objects.all()
        t = "It's now %s" % time
        count = posts.count()
        self.stdout.write(f'{t} - count of post:{count}')