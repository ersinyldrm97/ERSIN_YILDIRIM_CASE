import requests

BASE_URL = "https://petstore.swagger.io/v2"
HEADERS = {"Content-Type": "application/json"}

def test_create_pet_positive():
    payload = {
        "id": 1,
        "name": "Maviş",
        "photoUrls": ["https://example.com/photo1.jpg"],
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=payload, headers=HEADERS)
    print("Create Pet Response:", response.json())
    assert response.json()["name"] == "Maviş"
    assert response.status_code == 200

def test_get_pet_positive():
    pet_id = 1
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    print("Get Pet Response:", response.json())
    assert response.json()["id"] == 1
    assert response.status_code == 200

def test_delete_pet_positive():
    pet_id = 1
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    print("Delete Pet Response:", response.text)
    assert response.status_code == 200

def test_update_pet_positive():
    payload = {
        "id": 1,
        "name": "Updated",
        "photoUrls": ["https://example.com/photo1.jpg"],
        "status": "rent"
    }
    response = requests.put(f"{BASE_URL}/pet", json=payload, headers=HEADERS)
    print("Update Pet:", response.json())
    assert response.json()["name"] == "Updated"
    assert response.status_code == 200
    


test_create_pet_positive()
test_get_pet_positive()
test_update_pet_positive()
test_delete_pet_positive()