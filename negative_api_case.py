import requests

BASE_URL = "https://petstore.swagger.io/v2"
HEADERS = {"Content-Type": "application/json"}

def test_create_pet_negative_missing_fields():
    payload = {
        "id": 1002,
        "status": "available"
        # wrong or empty values
    }
    response = requests.post(f"{BASE_URL}/pet", json=payload, headers=HEADERS)
    print("Create Pet Negative Response:", response.text)
    assert response.status_code == 405  # "Invalid input"

def test_get_pet_negative_not_found():
    pet_id = 999999
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    print("Get Pet Not Found Response:", response.text)
    assert response.status_code == 404

def test_update_pet_negative_invalid_payload():
    payload = {
        "id": "not-a-number",  # Invalid ID format
        "name": "BrokenPet",
        "photoUrls": ["url"]
    }
    response = requests.put(f"{BASE_URL}/pet", json=payload, headers=HEADERS)
    print("Update Pet Invalid Payload Response:", response.text)
    assert response.status_code in [400, 405]

def test_delete_pet_negative_not_found():
    pet_id = 999999
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    print("Delete Pet Not Found Response:", response.text)
    assert response.status_code == 404

test_create_pet_negative_missing_fields()
test_get_pet_negative_not_found()
test_update_pet_negative_invalid_payload()
test_delete_pet_negative_not_found()