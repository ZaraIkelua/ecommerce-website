import csv
import os
import random
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from general.models import Product, Category

class Command(BaseCommand):
    help = 'Import products from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='The filename of the CSV to import')

    def handle(self, *args, **options):
        filename = options['filename']

        # Check if file exists in the project root directory
        if not os.path.exists(os.path.join('general', 'product_data', filename)):
            raise CommandError('File "{}" does not exist'.format(filename))

        try:
            with open(os.path.join('general', 'product_data', filename), newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        category_name = row['category']
                        category, created = Category.objects.get_or_create(name=category_name)

                        discount = random.uniform(0, 0.1) * float(row['price'])  # up to 10% discount

                        Product.objects.create(
                            name=row['name'],
                            category=category,
                            price=float(row['price']),
                            discount=discount,
                            description=row['description'],
                            image=eval(row['images'])[0]
                        )
                    except Exception as error:
                        print(error)
                        continue

        except Exception as e:
            raise CommandError('Failed to import products: {}'.format(str(e)))

        self.stdout.write(self.style.SUCCESS('Successfully imported products.'))
