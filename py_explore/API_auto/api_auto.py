import requests

## GET Call
print("##################      GET    ###################")
response = requests.get('https://jsonplaceholder.typicode.com/posts')
print( "The Response code is :", response.status_code)
print( "The Response body is :")
print( response.text)
print( '%' * 60)


response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print( "The Response code is :", response.status_code)
print( "The Response body is :")
print( response.text)
print( '%' * 60)

response = requests.get('https://jsonplaceholder.typicode.com/posts/1/comments')
print( "The Response code is :", response.status_code)
print( "The Response body is :")
print( response.text)
print( '%' * 60)

response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
print( "The Response code is :", response.status_code)
print( "The Response body is :")
print( response.text)
print( '%' * 60)

response = requests.get('https://jsonplaceholder.typicode.com/posts?userId=1')
print( "The Response code is :", response.status_code)
print( "The Response body is :")
print( response.text)
print( '%' * 60)

## Post Payload
print("##################      POST    ###################")
p_data = {
            'title' : 'foo',
            'body'  : 'bar',
            'userId': 1
         }
response = requests.post( url = 'https://jsonplaceholder.typicode.com/posts', data = p_data)
print( "The Response code is :", response.status_code)
print( "The Response body is :")
print( response.text)
response = response.json()
print( response['id'])
print( '%' * 60)

## Put Payload
print("##################      PUT    ###################")
p_data = {
            'id'    : 1, 
            'title' : 'new foo',
            'body'  : 'new bar',
            'userId': 1
         }
print( p_data)
response = requests.put( url = "https://jsonplaceholder.typicode.com/posts/{}".format(p_data['id']), data = p_data)
print( "https://jsonplaceholder.typicode.com/posts/{}".format(p_data['id']))
print( "The Response code is :", response.status_code)
print( "The Response body is :")
print( response.text)
response = response.json()
print( response['id'])

## Patch Payload
print("##################      PATCH    ###################")
p_data = {
            'title' : 'patched new title',
            'body'  : 'patched new bar',
         }
print( p_data)
response = requests.patch( url = "https://jsonplaceholder.typicode.com/posts/1", data = p_data)
print( "https://jsonplaceholder.typicode.com/posts/1")
print( "The Response code is :", response.status_code)
print( "The Response body is :")
print( response.text)
response = response.json()
print( response['id'])

## Delete 
print("##################      DELETE     ###################")
response = requests.delete("https://jsonplaceholder.typicode.com/posts/{}".format(response['id']))
print( "The Response code is :", response.status_code)
print( response.text)


