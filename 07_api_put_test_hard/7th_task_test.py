import requests
def test_put():
    data_put={
        "full_name": "Idris Blogger"
    }
    response=requests.put('http://35.225.243.133/bloggers/', data=data_put)
    expected_sc=200
    actual_sc=response.status_code
    # print(response.json())
    print(data_put["full_name"])
    ex_resp=data_put["full_name"]
    ac_resp=response["full_name"]
    assert expected_sc==actual_sc
    assert ex_resp==ac_resp
test_put()