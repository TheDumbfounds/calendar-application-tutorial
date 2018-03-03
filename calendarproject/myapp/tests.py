from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Entry


class TestEntry(TestCase):

    def setUp(self):
        self.entry = Entry(
            name='name',
            author=User.objects.create(),
            date=timezone.now(),
            description="this should be a long description..."
        )

    def test_short_description(self):
        self.assertEquals(self.entry.short_description(), 'this should be ')
