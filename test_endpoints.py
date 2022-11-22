"""test user endpoint"""
import requests


def test_get_user():
    """test user endpoint"""
    url = 'http://localhost:5000/user/'
    response = requests.get(url+'eloi')
    assert response.status_code == 200
    assert response.json() == 'eloi@ub.edu'

def test_add_user():
    """test add user endpoint"""
    url = 'http://localhost:5000/user/'
    response = requests.post(url+"joan",{"email":"joan@ub.edu"})
    assert response.status_code == 200
    assert response.json() == 'Hello joan! Your email is joan@ub.edu'
