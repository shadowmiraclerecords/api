# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#   return 'Hello from Flask!'

# if __name__ == '__main__':
#   app.run()


from flask import Flask, request
from flask_restful import Resource, Api
from store import store
import sys
import os

app = Flask(__name__)
api = Api(app)
port = 5100

if sys.argv.__len__() > 1:
    port = sys.argv[1]
print("Api running on port : {} ".format(port))

class topic_tags(Resource):
    def get(self):
        print('testing')
        store()
        return {'hello': 'world world'}

api.add_resource(topic_tags, '/')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)