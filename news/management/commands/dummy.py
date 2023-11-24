import os
import django
from faker import Faker
from django.core.management.base import BaseCommand
from news.models import Article

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating dummy data...'))

        self.create_dummy_data()

        self.stdout.write(self.style.SUCCESS('Dummy data created successfully.'))

    def create_dummy_data(self, num_articles=10):
        for _ in range(num_articles):
            Article.objects.create(
                author=fake.name(),
                title=fake.sentence(),
                description=fake.text(200),
                body=fake.paragraphs(5),
                location=fake.city(),
                publication_date=fake.date_this_decade(),
                active=fake.boolean(),
            )

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    django.setup()
    command = Command()
    command.handle()
