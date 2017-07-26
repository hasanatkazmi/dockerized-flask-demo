#!/usr/bin/env python
#coding=utf-8
import os
import flask
import unittest
import json

from main import app


class BasicTests(unittest.TestCase):
    def setUp(self):
        flask.app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_get_plain(self):
        result = self.app.get('/', environ_base={'HTTP_ACCEPT': 'text/html'})
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, "<p>Hello, World</p>")

    def test_get_json(self):
        result = self.app.get('/', environ_base={'HTTP_ACCEPT': 'application/json'})
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), {"message": "Good morning"})

    def test_post_json(self):
        result = self.app.post('/', data=json.dumps(dict(foo='xyz')), content_type="application/json", environ_base={'HTTP_ACCEPT': 'application/json'})
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), {"foo": "xyz"})


if __name__ == '__main__':
    unittest.main()