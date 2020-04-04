from myauth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'create admin user'
    def handle(self, *args, **options):
        if User.objects.count() > 0:
            print(f'User already exists ')
            return
        print('creating new user admin.')
        user = User.objects.create_superuser(email='admin@admin.com', password='admin')
        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.save()

