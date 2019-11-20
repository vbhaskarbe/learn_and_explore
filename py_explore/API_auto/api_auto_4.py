import requests

class RestApiTester():
    def __init__(self):
        self.url_home = 'https://jsonplaceholder.typicode.com'

    def process_result( self, result):
        print( "The Response code is :", result.status_code)
        result = result.json()
        print( "Id is :", result['id']) if 'id' in result else None
        print( "Text is:", result['body']) if 'body' in result else None
        print( '%' * 80, '\n')
 
    ## Wrapper func handling put, patch and delete also.
    def post( self, url_tag, data, req_type = 'post'):
        full_url = self.url_home + url_tag
        print("HTTP {} => {}".format( req_type, full_url))
        http_call = getattr( requests, req_type)
        result = http_call( url = full_url, data = data)
        self.process_result( result)
    
    def get(self, url_tag):
        self.post( url_tag, None, 'get')

    def put( self, url_tag, data):
        self.post( url_tag, data, 'put')

    def patch( self, url_tag, data):
        self.post( url_tag, data, 'patch')

    def delete( self, url_tag, data = None):
        self.post( url_tag, data, 'delete')

if __name__ == '__main__':
    restapi_obj = RestApiTester()
    ## GET calls
    for url_tag in [ '/posts', '/posts/1', '/posts/1/comments', '/comments?postId=1', '/posts?userId=1' ]:
        restapi_obj.get( url_tag)
    ## POST call with fresh payload
    p_data = {  'title' : 'foo', 'body'  : 'bar', 'userId': 1 }
    restapi_obj.post('/posts', p_data)
    ## PUT call with changes to existing entity
    p_data = { 'id'    : 1, 'title' : 'new foo', 'body'  : 'new bar', 'userId': 1 }
    restapi_obj.put('/posts/1', p_data)
    ## PATCH call with partial data in payload for update
    p_data = { 'title' : 'patched new title', 'body'  : 'patched new bar' }
    restapi_obj.patch('/posts/1', p_data)
    ## Delete is entity
    restapi_obj.delete('/posts/1')

