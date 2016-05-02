from datetime import timedelta
import os
import random
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_perf.settings'

from django.contrib.auth.models import User
from django.utils import timezone
from core.models import Store, Product, Category, Image, Order, OrderLine

LOCATIONS = ['London', 'Paris', 'Berlin', 'Munich', 'Stockholm']
CATEGORIES = ['Electronics', 'Toys', 'Food', 'Misc']

def run():
    User.objects.all().delete()
    Store.objects.all().delete()
    Order.objects.all().delete()

    users = []
    print 'Creating users...'
    for u in range(0, 100):
        user = 'user{0}'.format(u)
        users.append(User(username=user,
                          email='{0}@test.com'.format(user),
                          first_name=user,
                          last_name=user))

    User.objects.bulk_create(users)

    print 'Creating stores...'

    for i in range(0, 40):
        store = Store.objects.create(name='My Store {0}'.format(i+1),
                                     location=random.choice(LOCATIONS))

        cats = []
        for c in CATEGORIES:
            cats.append(Category(name=c, store=store))

        Category.objects.bulk_create(cats)

        products = []
        for j in range(0, 100):
            products.append(Product(
                name='Product SKU: {0}{1}'.format(i,j),
                description='A description',
                price=random.uniform(1, 3000),
                store=store
            ))

        Product.objects.bulk_create(products)
        store_categories = list(Category.objects.filter(store=store))
        for p in Product.objects.filter(store=store):
            number_of_cats = random.randint(0, len(CATEGORIES))
            p.categories.add(*random.sample(store_categories, number_of_cats))

            Image.objects.create(url='http://loremflickr.com/200/200/{0}'.format(random.choice(LOCATIONS).lower()),
                                 product=p)

    print 'Creating orders...'

    start_date = timezone.now() - timedelta(days=5)

    all_users = User.objects.all()
    for store in Store.objects.all():
        products = list(Product.objects.filter(store_id=store.id))
        for user in all_users:
            order = Order.objects.create(
                total=random.uniform(10, 300),
                order_date=start_date,
                store=store,
                customer=user
            )
            lines = []
            for i in range(0, random.randint(2, 8)):
                lines.append(OrderLine(order=order,
                                       quantity=1,
                                       product=random.choice(products)))

            OrderLine.objects.bulk_create(lines)
            start_date += timedelta(minutes=1)

if __name__ == '__main__':
    run()
