from locust import HttpUser, task, between
from constant import global_constant 
class N11SearchUser(HttpUser):
    wait_time = between(1, 2)
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json",
    "Referer": "https://www.n11.com/",
    "Accept-Language": "tr-TR,tr;q=0.9",
    "X-Requested-With": "XMLHttpRequest"
    }
        
    @task
    def basic_search(self):
        response = self.client.get("/arama?q=telefon", headers=self.headers)
        print("basic_search Status Code:", response.status_code)

    @task
    def no_results_search(self):
        response = self.client.get("/arama?q=asdfghjkl", headers=self.headers)
        print("no_results_search Status Code:", response.status_code)
    @task
    def special_char_search(self):
        response = self.client.get("/arama?q=çalışma+masası", headers=self.headers)
        print("special_char_search Status Code:", response.status_code)

    @task
    def long_keyword_search(self):
        long_query = "a" * 120
        response = self.client.get(f"/arama?q={long_query}", headers=self.headers)
        print("long_keyword_search Status Code:", response.status_code)

    @task
    def case_sensitive_search(self):
        response = self.client.get("/arama?q=Telefon", headers=self.headers)
        response1 = self.client.get("/arama?q=telefon", headers=self.headers)
        print("case_sensitive_search Status Code:", response.status_code)
        print("case_sensitive_search Status Code:", response1.status_code)

    @task
    def repeated_search(self):
        for _ in range(3):
            response = self.client.get("/arama?q=telefon", headers=self.headers)
        print("repeated_search Status Code:", response.status_code)

    @task
    def rapid_searches(self):
        keywords = ["laptop", "kamera", "saat", "kitap", "tablet"]
        for keyword in keywords:
            response = self.client.get(f"/arama?q={keyword}", headers=self.headers)
        print("repeated_search Status Code:", response.status_code)