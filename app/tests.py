from django.test import TestCase


class Basic(TestCase):
    def test_basic(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 404)

class Lei(TestCase):
    def test_basic(self):
        from python_lei.utils import Download, RESOURCE_DIR
        print("Doing the download..")
        Download()
        print("Done with the download")
        import os
        print(os.path.abspath(os.curdir))
        print(RESOURCE_DIR)
        print(os.listdir(RESOURCE_DIR))