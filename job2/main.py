"""
This file contains the controller that accepts command via HTTP
and trigger business logic layer
"""
import os
from flask import Flask, request
from flask import typing as flask_typing

from bll.data_transformation import convert_sales_to_avro


AUTH_TOKEN = os.environ.get("API_AUTH_TOKEN")

if not AUTH_TOKEN:
    print("AUTH_TOKEN environment variable must be set")


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    """
    Controller that accepts command via HTTP and
    trigger business logic layer

    Proposed POST body in JSON:
    {   
        "raw_dir": "/path/to/my_dir/raw/sales/2022-08-09",
        "stg_dir: "/path/to/my_dir/stg/sales/2022-08-09"
    }
    """
    input_data: dict = request.json
    # TODO: implement me
    raw_dir = input_data.get('raw_dir')
    stg_dir = input_data.get('stg_dir')

    if not raw_dir:
        return {
            "message": "raw_dir parameter missed",
        }, 400
    
    if not stg_dir:
        return {
            "message": "stg_dir parameter missed",
        }, 400

    convert_sales_to_avro(raw_dir=raw_dir, stg_dir=stg_dir)

    return {
               "message": "Data converted to avro format and saved successfully",
           }, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8082)
