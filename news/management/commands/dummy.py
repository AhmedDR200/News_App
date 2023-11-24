import os
import django
from faker import Faker
from django.core.management.base import BaseCommand
from news.models import Journalist, Article

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating dummy data...'))

        # Create journalists
        self.create_dummy_journalists()

        # Create articles
        self.create_dummy_data()

        self.stdout.write(self.style.SUCCESS('Dummy data created successfully.'))

    def create_dummy_journalists(self, num_journalists=5):
        for _ in range(num_journalists):
            Journalist.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                biography=fake.paragraph(),
            )

    def create_dummy_data(self, num_articles=10):
        journalists = Journalist.objects.all()

        for _ in range(num_articles):
            Article.objects.create(
                author=fake.random_element(journalists),
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
