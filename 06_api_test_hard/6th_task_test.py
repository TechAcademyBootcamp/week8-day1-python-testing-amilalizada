import requests
def test_post():
    post_data = {
        "full_name": "Idris Shabanli"
    }
    response=requests.post('http://35.225.243.133/bloggers/', data=post_data)
    expected_status_code=201
    actual_s_c=response.status_code
    print(response.status_code)
    print(response.json()["full_name"])
    expected_response=post_data["full_name"]
    actual_response=response.json()["full_name"]
    assert expected_status_code==actual_s_c
    assert expected_response==actual_response
def test_post2():
    post_data= {
        "full_name": "abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd "
    }
    response=requests.post('http://35.225.243.133/bloggers/', data=post_data)
    expected_status_code=400
    actual_s_c=response.status_code
   
    excepted_resp=["Ensure this field has no more than 180 characters."]
    actual_resp=response.json()['full_name']
    
    assert expected_status_code==actual_s_c
    assert excepted_resp==actual_resp
# test_post2(
def test_post3():
    post_data={}
    response=requests.post('http://35.225.243.133/bloggers/', data=post_data)
    expected_status_code=400
    actual_s_c=response.status_code
    excepted_resp=["This field is required."]
    actual_resp=response.json()['full_name']
    
    assert expected_status_code==actual_s_c
    assert excepted_resp==actual_resp
def test_post4():
    post_data={
        "id": 1223
    }
    response=requests.post('http://35.225.243.133/bloggers/', data=post_data)
    expected_status_code=400
    actual_s_c=response.status_code
    excepted_resp=["This field is required."]
    actual_resp=response.json()['full_name']
    assert expected_status_code==actual_s_c
    assert excepted_resp==actual_resp








   