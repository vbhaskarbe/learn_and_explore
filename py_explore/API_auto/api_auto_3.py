import requests

URL_HOME = 'https://jsonplaceholder.typicode.com'

def smart_http_caller( http_call, url_tag, payload = None):
    full_url = URL_HOME + url_tag
    print("HTTP {} => {}".format( http_call, full_url))
    resp_api_call = getattr( requests, http_call)
    if payload == None:
        response    = resp_api_call( full_url)
    else:
        response    = resp_api_call( url = full_url, data = payload)
    print( "The Response code is :", response.status_code)
    response = response.json()
    if 'id' in response:
        print( "Id is :",response['id'])
    if (not http_call == 'get') and ('body' in response):
        print( "Text is:", response)
    print( '%' * 80, '\n')

if __name__ == '__main__':
    smart_http_caller('get', '/posts')
    smart_http_caller('get', '/posts/1')
    smart_http_caller('get', '/posts/1/comments')
    smart_http_caller('get', '/comments?postId=1')
    smart_http_caller('get', '/posts?userId=1')
    p_data = {
                'title' : 'foo',
                'body'  : 'bar',
                'userId': 1
             }
    smart_http_caller('post', '/posts', p_data)
    p_data = {
                'id'    : 1, 
                'title' : 'new foo',
                'body'  : 'new bar',
                'userId': 1
             }
    smart_http_caller('put', '/posts/1', p_data)
    p_data = {
                'title' : 'patched new title',
                'body'  : 'patched new bar',
             }
    smart_http_caller('patch', '/posts/1', p_data)
    smart_http_caller('delete', '/posts/1')

