from flask import Flask, jsonify
from annotation_converter import convert
import json


app = Flask(__name__)

def get_openlabel_annotation():
    path_to_annotell_annotation = 'annotell_1.json'

    with open(path_to_annotell_annotation, 'r') as content:
        annotell_annotation = json.load(content)

    open_label_annotation = convert(annotell_annotation)
    return open_label_annotation


@app.route('/')
def annotel_program():
    info = "Welcome to the annotel converter!"
    return info


@app.route('/openlabel/')
def get_all_converted_data():

    open_label_annotation = get_openlabel_annotation()

    return jsonify(open_label_annotation)

@app.route('/openlabel/<id_class>', methods = ['GET'])
def get_converted_data(id_class):
    open_label_annotation = get_openlabel_annotation()
    converted_coordinate = open_label_annotation["data"]["frames"][""]["objects"][id_class]

    return jsonify(converted_coordinate)

if __name__ == '__main__':
    app.run()
