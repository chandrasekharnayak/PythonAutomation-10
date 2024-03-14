import requests
# print(dir(requests))
# HTTPError,Request,Response,Timeout,api,delete,get,exceptions,patch,post,put,request,status_codes,status_code
"""
url = 'https://jsonplaceholder.typicode.com/posts/1'
responce = requests.get(url)

if responce.status_code == 200:
    data = responce.json()
    for k,v in data.items():
        if k == 'userId':
            print(v)
    print(data)
    print('Get Request Pass')
else:
    # print('Get Request Failed')
"""


#post
'''
url = 'https://jsonplaceholder.typicode.com/posts'
data = {'title':'New Post 1','body':"it's a new post",'userId':1}

response = requests.post(url,json=data)

if response.status_code == 201:
    new_post = response.json()
    print('Post request sucessfull')
    print(new_post)
else:
    print('Request failed due to:-',response.status_code)'''

#PUT
url = 'https://jsonplaceholder.typicode.com/posts/1'
data = {'title':'modiefied data'}
responce = requests.put(url,json=data)

if responce.status_code == 200:
    update_post = responce.json()
    print('Sucessfull')
    print(update_post)
