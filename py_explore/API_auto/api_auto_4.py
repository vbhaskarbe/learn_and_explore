import requests

class RestApiTester():
    def __init__(self):
        self.url_home = 'https://jsonplaceholder.typicode.com'

    def process_result( self, result):
        print( "The Response code is :", result.status_code)
        result = result.json()
        if 'id' in result:
            print( "Id is :",result['id'])
        if 'body' in result:
            print( "Text is:", result['body'])
        print( '%' * 80, '\n')
 
    def get(self, url_tag):
        full_url = self.url_home + url_tag
        print("HTTP GET => {}".format( full_url))
        result = requests.get( full_url)
        self.process_result( result)

    def post( self, url_tag, data, req_type = 'post'):
        full_url = self.url_home + url_tag
        print("HTTP {} => {}".format( req_type, full_url))
        http_call = getattr( requests, req_type)
        result = http_call( url = full_url, data = data)
        self.process_result( result)
    
    def put( self, url_tag, data):
        self.post( url_tag, data, 'put')

    def patch( self, url_tag, data):
        self.post( url_tag, data, 'patch')

    def delete( self, url_tag, data = None):
        self.post( url_tag, data, 'delete')

if __name__ == '__main__':
    restapi_obj = RestApiTester()

    for url_tag in [ '/posts', '/posts/1', '/posts/1/comments', '/comments?postId=1', '/posts?userId=1' ]:
        restapi_obj.get( url_tag)

    p_data = {  'title' : 'foo', 'body'  : 'bar', 'userId': 1 }
    restapi_obj.post('/posts', p_data)

    p_data = { 'id'    : 1, 'title' : 'new foo', 'body'  : 'new bar', 'userId': 1 }
    restapi_obj.put('/posts/1', p_data)

    p_data = { 'title' : 'patched new title', 'body'  : 'patched new bar' }
    restapi_obj.patch('/posts/1', p_data)

    restapi_obj.delete('/posts/1')

