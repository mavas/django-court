from django.test import TestCase


class Basic(TestCase):
    def test_basic(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 404)

class Lei(TestCase):
    def test_request(self):
        import requests
        response = requests.get('https://www.yahoo.com')
        self.assertEquals(response.ok, 200)
        print("Len: %s" % dir(response))

    def test_basic(self):
        from python_lei.utils import Download, RESOURCE_DIR
        print("Doing the download..")
        import zipfile
        try:
            Download()
        except zipfile.BadZipFile as e:
            print("Got the error: %s" % e)
        print("Done with the download")
        import os
        print(os.path.abspath(os.curdir))
        print(RESOURCE_DIR)
        print(os.listdir(RESOURCE_DIR))