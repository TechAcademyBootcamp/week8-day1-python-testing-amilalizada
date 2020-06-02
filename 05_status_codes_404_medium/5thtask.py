import requests
def test_post(): 
    link=input('enter link')
    response=requests.get(link)
    print(response.status_code)
    if response.status_code==200:
        print('succes')
    else:
        print('404 not found')