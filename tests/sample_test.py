import unittest
from unittest.mock import patch

from django.http import HttpRequest, QueryDict
from stubserver import StubServer

from application.sample_user_case import mark_sample, create_sample
from infrastructure.sample.models import SampleData


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        SampleData.objects.create(id_name="id", mark_result=False).save()
        self.server = StubServer(8000)
        self.server.run()

    def tearDown(self) -> None:
        SampleData.objects.all().delete()
        self.server.stop()

    def test_mark_sample(self):
        request = HttpRequest()
        request.GET = QueryDict(query_string="sampleId=id", mutable=True)
        value = mark_sample(request)
        self.assertEqual(value.getvalue(), b'{"id": "id", "mark_result": true}')

    @patch('domain.rootcause.algorithm.analysis')
    def test_mock_analysis(self, mock_analysis):
        self.server.expect(method="GET", url="/").and_return(content="id2")
        mock_analysis.return_value = True
        request = HttpRequest()
        request._body = '{"id": "id2"}'
        value = create_sample(request)
        self.assertEqual(value.getvalue(), b'{"id": "id2", "mark_result": false}')
