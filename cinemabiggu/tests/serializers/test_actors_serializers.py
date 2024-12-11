from django.test import TestCase
from cinemabiggu.models import Actor
from cinemabiggu.serializers import ActorSerializer


class ActorSerializerTestCase(TestCase):
    def setUp(self):
        self.actor = Actor(
            name='Actor Test',
            description='This actor is a test',
            birth_date='2000-01-01',
            awards=[]
        )
        self.actor_serializer = ActorSerializer(instance=self.actor)

    def test_actor_keys(self):
        data = self.actor_serializer.data
        actor_fields = set([
            'id', 'name', 'description',
            'birth_date', 'awards'
        ])
        self.assertEqual(
            set(data.keys()),
            actor_fields
        )

    def test_actor_values(self):
        data = self.actor_serializer.data
        self.assertEqual(data['name'], self.actor.name)
        self.assertEqual(data['description'], self.actor.description)
        self.assertEqual(data['birth_date'], self.actor.birth_date)
        self.assertEqual(data['awards'], self.actor.awards)
