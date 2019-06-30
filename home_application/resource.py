# -*- coding: utf-8 -*-


def get_search_dict(query_dict):
    search_dict = query_dict.dict()
    for k, v in search_dict.items():
        if 'time' in k:
            continue

        new_key = "%s__in" % k
        search_dict[new_key] = search_dict.pop(k)

    return search_dict

