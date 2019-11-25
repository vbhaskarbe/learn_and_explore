import requests

class RestApiTester():
    ''' This class implements 5 HTTP Requests calls '''
    def __init__(self):
        self.url_home = 'https://jsonplaceholder.typicode.com'

    def process_result( self, response):
        print( "The Response code is  :", response.status_code)
        print( "Response is           :", response.text)
        print( '%' * 80, '\n')

    def __getattr__(self, name):
        def http_caller(*args, **kwargs):
            if name in [ 'get', 'post', 'put', 'patch', 'delete'] :
                http_req = name
            else :
                print("ERROR: Undefined method %s" % name)
                raise NotImplementedError("Error: Undefined method %s" % name)
            url_tag   = args[0] if len(args) > 0 else kwargs.get('url_tag')
            data      = args[1] if len(args) > 1 else kwargs.get('data', None)
            print("HTTP {} => {}".format( http_req, self.url_home + url_tag))
            http_call = getattr( requests, http_req)
            result    = http_call( url = self.url_home + url_tag, data = data)
            self.process_result( result)
        return http_caller

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
    ## UnImplemented method call - Error
    testapi.delete_NA('/posts/1')

