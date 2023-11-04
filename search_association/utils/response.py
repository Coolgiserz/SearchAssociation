def make_response_data(**kwargs):
    return dict(**kwargs)

def make_empty_response(msg="no data returned"):
    return make_response_data(status=200, msg=msg)

def make_success_response(data, msg="success"):
    return make_response_data(status=200, data=data, msg=msg)