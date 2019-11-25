import requests
import sys

class RestApiTester():
    def __init__(self):
        self.url_home = 'https://jsonplaceholder.typicode.com'

    def process_result( self, result):
        print( "The Response code is  :", result.status_code)
        result = result.json()
        print( "Id is                 :", result['id']) if 'id' in result else None
        print( "Response is           :", result)
        print( '%' * 80, '\n')

    def http_caller( self, *args, **kwargs):
        http_req = sys._getframe().f_back.f_code.co_name
        url_tag  = args[0] if len(args) > 0 else kwargs.get('url_tag')
        data     = argv[1] if len(args) > 1 else kwargs.get('data', None)
        print("HTTP {} => {}".format( http_req, self.url_home + url_tag))
        http_call = getattr( requests, http_req)
        result = http_call( url = self.url_home + url_tag, data = data)
        self.process_result( result)
        
    ## Wrapper func handling put, patch and delete also.
    def post( self, url_tag, data):
        self.http_caller( url_tag = url_tag, data = data)
    
    def get(self, url_tag):
        self.http_caller( url_tag)

    def put( self, url_tag, data):
        self.http_caller( url_tag = url_tag, data = data)

    def patch( self, url_tag, data):
        self.http_caller( url_tag = url_tag, data = data)

    def delete( self, url_tag):
        self.http_caller( url_tag)

if __name__ == '__main__':
    testapi = RestApiTester()
    ## GET calls
    for url_tag in [ '/posts', '/posts/1', '/posts/1/comments', '/comments?postId=1', '/posts?userId=1' ]:
        testapi.get( url_tag)
    
    ## POST call with fresh payload
    p_data = {  'title' : 'foo', 'body'  : 'bar', 'userId': 1 }
    testapi.post('/posts', p_data)
    ## PUT call with changes to existing entity
    p_data = { 'id'    : 1, 'title' : 'new foo', 'body'  : 'new bar', 'userId': 1 }
    testapi.put('/posts/1', p_data)
    ## PATCH call with partial data in payload for update
    p_data = { 'title' : 'patched new title', 'body'  : 'patched new bar' }
    testapi.patch('/posts/1', p_data)
    ## Delete an entity
    testapi.delete('/posts/1')

