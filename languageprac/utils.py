def get_request_params(params):

    result = {}
    if 'page_size' in params:
        result['page_size'] = params['page_size']
    else:
        result['page_size'] = 20

    return result

