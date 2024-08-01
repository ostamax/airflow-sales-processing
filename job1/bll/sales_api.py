from dal import local_disk, sales_api


def save_sales_to_local_disk(date: str, raw_dir: str) -> None:
    """
    Get data from the API and save it to disk.

    Args:
        date (str): data retrieve the data from
        raw_dir (str): path to the raw data folder
    """
    print("\tI'm in get_sales(...) function!")
    msg = ""
    if date != "" and raw_dir != "":
        result_list = sales_api.get_sales(date=date)
        print(result_list)
        code = int(result_list[1])

        stored = local_disk.save_to_disk(
                        result_list[0]['data'],
                        raw_dir+"/sales_"+date
        )
        print(stored)
        if result_list[1] == 200 and stored == 'ok':
                msg = "Data retrieved from API and saved successfully"
                code = 201
        elif not result_list:
                msg = "Nothing found for the date"
                code = 201

    else:
        msg = "Check that all parameters are set"
        code = 400

    return {
            "message": msg,
            }, code
