from django.test import TestCase


class Basic(TestCase):
    def test_basic(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 404)

class Lei(TestCase):
    def test_request(self):
        """
        Just verifies that the 'requests' library works.  It probbably does, so
        maybe delete this test
        """
        import requests
        response = requests.get('https://www.yahoo.com')
        print("Len: %s" % dir(response))
        self.assertEquals(response.ok, True)

    def test_download(self):
        from python_lei.utils import Download, RESOURCE_DIR
        import zipfile
        import os
        directory_listing = os.listdir(RESOURCE_DIR)
        self.assertEquals(len(directory_listing), 0)
        print("Doing the download..")
        try:
            Download()
        except zipfile.BadZipFile as e:
            print("Got the error: %s" % e)
            raise Exception(e)
        print("Done with the download")
        print(os.path.abspath(os.curdir))
        print(RESOURCE_DIR)
        directory_listing = os.listdir(RESOURCE_DIR)
        self.assertEquals(len(directory_listing), 1)