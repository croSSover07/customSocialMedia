from django.utils import timezone

from posts.models import Post


def my_cron_job():
    time = timezone.now().strftime('%X')
    posts = Post.objects.all()
    t = "It's now %s" % time
    count = posts.count()
    print(f'{t} - count of post:{count} - my_cron_job')