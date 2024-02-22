
def is_response_successful(response):
    return response.status_code == 200

def is_response_not_empty(resposne):
    return len(resposne.json()) > 0

def process_response(response):
    if is_response_successful(response) and is_response_not_empty(response):
        return response
    elif not is_response_successful(response):
        print(f'Error: {response.status_code}')
    else:
        print(f'Error: response is empty!')
    return None