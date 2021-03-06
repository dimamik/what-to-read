import json

from elasticsearch import helpers

from elastic.instance import es


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def parse_array_of_json(path):
    """
    Parses json with respect to book_points double value
    """
    input_file = open(path)
    json_array = json.load(input_file)
    store_list = []
    for item in json_array:
        store_details = item.copy()
        if 'book_points' in store_details:
            if not isfloat(store_details['book_points']):
                store_details['book_points'] = store_details['book_points'].replace("(", "")
                store_details['book_points'] = store_details['book_points'].replace(")", "")
            if not isfloat(store_details['book_points']):
                raise Exception("Problem with format")
        store_list.append(store_details)
    return store_list


def create_index_and_bulk_add_json(index_name, json_path):
    array_of_json = parse_array_of_json(json_path)
    helpers.bulk(es, array_of_json, index=index_name, chunk_size=400, request_timeout=60)
