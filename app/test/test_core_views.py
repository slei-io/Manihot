from unittest import TestCase
from core.serializers import Serializer
from core.consumerView import ConsumerView


class ConsumerViewTestCase(TestCase):

    def setUp(self):
        self.consumerView = ConsumerView()

    def test_get_serializer_class(self):
        """
        Test ConsumerView.get_serializer_class returns
        a Serializer class by default
        """

        self.assertEqual(self.consumerView.get_serializer_class(), Serializer)

    def test_get_serializer(self):
        """Test ConsumerView.get_serializer returns instance of serializer"""
