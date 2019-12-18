import unittest

from django.http import HttpRequest, QueryDict

from application.sample_user_case import mark_sample, create_sample
from infrastructure.sample.models import SampleData


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        SampleData.objects.create(id_name="id", mark_result=False).save()

    def tearDown(self) -> None:
        SampleData.objects.all().delete()

    def test_mark_sample(self):
        request = HttpRequest()
        request.GET = QueryDict(query_string="sampleId=id", mutable=True)
        value = mark_sample(request)
        self.assertEqual(value.getvalue(), b'{"id": "id", "mark_result": true}')

    def test_create_sample(self):
        request = HttpRequest()
        request._body = '{"id": "id2"}'
        value = create_sample(request)
        self.assertEqual(value.getvalue(), b'{"id": "id2", "mark_result": false}')
        self.assertEqual(SampleData.objects.filter(id_name="id2").count(), 1)
