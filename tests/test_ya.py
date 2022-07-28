import unittest
from YA_API import YaApi


class TestYaApi(unittest.TestCase):
    
    def test_cls_YaApi(self):
        ya_api = YaApi()
        result = ya_api.create_folder()
        self.assertEqual(result, 201)
        
    def tearDown(self):
        ya_api = YaApi()
        ya_api.delete_folder()

