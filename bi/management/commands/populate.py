from django.core.management.base import BaseCommand
from faker import Faker
from bi.models import FakeUser

class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        num_rows = 1000

        job_titles = ['analista', 'estagiário', 'gerente', 'coordenador']
        companies = ['A', 'B', 'C']
        cities = ['SP', 'RJ', 'MG']

        for _ in range(num_rows):
            FakeUser.objects.create(
                name=fake.name(),
                company=fake.random_element(elements=companies),
                city=fake.random_element(elements=cities),
                job_title=fake.random_element(elements=job_titles),
                age=fake.random_int(min=18, max=50),
                salary=round(fake.random_number(digits=4), 2)
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully populated the database with {num_rows} records'))
