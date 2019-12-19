## 测试策略

* 使用独立的测试setting文件
```shell script
# 初始化数据库
python3 manage.py migrate --settings=exceptionhandler.test_settings
# 跑测试
python3 manage.py test --settings=exceptionhandler.test_settings
```

* 使用sqlite替代掉原有数据库
```shell script
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db-test.sqlite3'),
    }
}
```
```python
    def setUp(self) -> None:
        SampleData.objects.create(id_name="id", mark_result=False).save()

    def tearDown(self) -> None:
        SampleData.objects.all().delete()
```

* 使用mock替换掉数据
```python
    @patch('domain.rootcause.algorithm.analysis')
    def test_mock_analysis(self, mock_analysis):
        mock_analysis.return_value = True
        request = HttpRequest()
        request._body = '{"id": "id2"}'
        value = create_sample(request)
        self.assertEqual(value.getvalue(), b'{"id": "id2", "mark_result": false}')
```

* 使用stub server
```python
    def setUp(self) -> None:
        self.server = StubServer(8000)
        self.server.run()

    def tearDown(self) -> None:
        self.server.stop()

    @patch('domain.rootcause.algorithm.analysis')
    def test_mock_analysis(self, mock_analysis):
        self.server.expect(method="GET", url="/").and_return(content="id2")
       ...
```