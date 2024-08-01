from dal import json_to_avro_converter

def convert_sales_to_avro(raw_dir: str, stg_dir: str) -> None:
    """_summary_

    Args:
        raw_dir (str): path to the raw data folder
        stg_dir (str): path to the converted data folder
    """

    if raw_dir != "" and stg_dir != "":
        converted = json_to_avro_converter.convert_and_save(raw_dir, stg_dir)
        
        if converted == 'ok':
            msg = "Data retrieved from API and saved successfully"
            code = 201  

    else:
        msg = "Check that all parameters are set"
        code = 400

    return {
            "message": msg,
            }, code
