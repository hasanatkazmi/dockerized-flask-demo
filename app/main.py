#!/usr/bin/env python
#coding=utf-8
import os, logging

from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_message():
    if request.headers['Accept'] == "text/html":
        return "<p>Hello, World</p>"
    if request.headers['Accept'] == "application/json":
        return jsonify({"message": "Good morning"})

    return Response(status=204)


@app.route('/', methods=['POST'])
def post_message():
    if request.json and 'foo' in request.json:
        if 'SERVER_MODE' in os.environ and os.environ['SERVER_MODE'].lower() in ["1", "true"]:
            app.logger.info("Replying to server request for '{}' with '{}'".format('foo', request.json['foo']))

        # Note: its not mentioned whether response should be json or text, I am opting json
        return jsonify({"foo": request.json['foo']})

    return Response(status=204)


if __name__ == '__main__':
    logging.basicConfig(filename='plangrid.log', level=logging.INFO)
    app.run(host="0.0.0.0", port=8080)
