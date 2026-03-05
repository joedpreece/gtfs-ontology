import subprocess
import unittest

import requests


class MyTestCase(unittest.TestCase):

    def setUp(self):
        subprocess.run(["RDFox", "sandbox"], check=True)

        requests.post(
            "http://localhost:12110/datastores",
            json={"name": "transit"},
        )

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
