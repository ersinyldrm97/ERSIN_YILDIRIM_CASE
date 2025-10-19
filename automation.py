from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constant import global_constant
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
from selenium.common.exceptions import TimeoutException

class VisitInsider:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
    
    def visit_homePage(self):
        self.driver.get(global_constant.URL)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, global_constant.CHECK_CONTROL_HOMEPAGE)))
        try:
          self.wait.until(EC.element_to_be_clickable((By.XPATH, global_constant.COOKIES_ACCEPT_BUTTON))).click()
        except TimeoutException:
           print("Cookies OR POPUP does not shown")

        try:
             self.wait.until(EC.element_to_be_clickable((By.XPATH, global_constant.POPUP_CLOSE_BUTTON))).click()
        except TimeoutException:
           print("POPUP does not shown")
    def visit_career_page(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, global_constant.COMPANY_PAGE))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, global_constant.CAREER_PAGE))).click()
     
    def blocks_are_open_or_not(self):
        sections = ["Locations", "Teams", "Life at Insider"]

        for section in sections:
            try:
                self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{section}')]")))
                print(f"'{section}' section is visible.")
            except:
                print(f"'{section}' section is found but not all!")
        
    def visit_QA_jobs(self):
      element = self.wait.until(EC.presence_of_element_located((By.XPATH, global_constant.SEE_ALL_TEAMS)))

      self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", element)
      time.sleep(1)

      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      time.sleep(1)

      clickable_for_teams = self.wait.until(EC.element_to_be_clickable((By.XPATH, global_constant.SEE_ALL_TEAMS)))
      clickable_for_teams.click()
       
      # VISIT_QA_JOBS
      element1 = self.wait.until(EC.presence_of_element_located((By.XPATH, global_constant.VISIT_QA_JOBS)))

      self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", element1)
      time.sleep(1)

      actions = ActionChains(self.driver)
      actions.move_to_element(element1).perform()
      time.sleep(1)

      clickable_for_qa_jobs = self.wait.until(EC.element_to_be_clickable((By.XPATH, global_constant.VISIT_QA_JOBS)))
      clickable_for_qa_jobs.click()

      # SEE_ALL_QA_JOBS
      element2 = self.wait.until(EC.presence_of_element_located((By.XPATH, global_constant.SEE_ALL_QA_JOBS)))

      self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", element2)
      time.sleep(1)

      actions = ActionChains(self.driver)
      actions.move_to_element(element2).perform()
      time.sleep(1)

      clickable_for_all_jobs = self.wait.until(EC.element_to_be_clickable((By.XPATH, global_constant.SEE_ALL_QA_JOBS)))
      clickable_for_all_jobs.click()

    def filter_by_location(self):
      self.driver.get("https://useinsider.com/careers/open-positions/?department=qualityassurance")
      time.sleep(10)

      location_element = self.wait.until(EC.presence_of_element_located((By.XPATH, global_constant.FILTER_BY_LOCATION)))
      self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", location_element)
      time.sleep(2)

      actions = ActionChains(self.driver)
      actions.move_to_element(location_element).click().perform()
      time.sleep(2)

      dropdown_panel = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "select2-results__options")))

      max_scroll_attempts = 20
      scroll_attempts = 0
      while scroll_attempts < max_scroll_attempts:
          try:
              istanbul_option = self.driver.find_element(By.XPATH, global_constant.LOCATION_ISTANBUL_TURKEY)
              if istanbul_option.is_displayed():
                  self.driver.execute_script("""
                    var select = document.querySelector('#filter-by-location');
                    if (select) {
                        var event = new Event('change', { bubbles: true });
                        select.dispatchEvent(event);
                    }
                """, istanbul_option)
                  actions.move_to_element(istanbul_option).click().perform()
                  print("Istanbul, Turkiye choosen.")
                  break
          except (NoSuchElementException, ElementClickInterceptedException):
              self.driver.execute_script("arguments[0].scrollTop += 100;", dropdown_panel)
              time.sleep(2)
              scroll_attempts += 1
      else:
          print("Istanbul, Turkiye does not found!")
          return

      time.sleep(5)
      job_cards = self.driver.find_elements(By.XPATH, "//div[contains(@class,'position-list-item')]")

      if len(job_cards) > 0:
          print(f"{len(job_cards)} QA job(s) found in Istanbul, Turkey.")
      else:
          print("No QA jobs found for Istanbul, Turkey!")

      for i, card in enumerate(job_cards, start=1):
          position = card.find_element(By.XPATH, "//p[contains(text(), 'Quality Assurance')]").text
          department = card.find_element(By.XPATH, ".//span[@class='position-department text-large font-weight-600 text-primary']").text
          location = card.find_element(By.XPATH, ".//div[@class='position-location text-large']").text

          print(f"Job {i}:")
          print(f" - Position: {position}")
          print(f" - Department: {department}")
          print(f" - Location: {location}")

          time.sleep(5)
          assert "Quality Assurance" in position, f"Position does not contain 'Quality Assurance' → {position}"
          assert "Quality Assurance" in department, f"Department does not contain 'Quality Assurance' → {department}"
          assert "Istanbul, Turkiye" in location, f"Location does not contain 'Istanbul, Turkiye' → {location}"
      
    def check_that_all_job(self):
        job_cards = self.driver.find_elements(By.XPATH, "//div[contains(@class,'position-list-item-wrapper')]")

        if len(job_cards) > 0:
            print(f"{len(job_cards)} QA job(s) found in Istanbul, Turkey.")
        else:
            print("No QA jobs found for Istanbul, Turkey!")

        for i, card in enumerate(job_cards, start=1):
            try:
                position = card.find_element(By.XPATH, "//p[contains(text(), 'Quality Assurance')]").text
                department = card.find_element(By.XPATH, ".//span[@class='position-department text-large font-weight-600 text-primary']").text
                location = card.find_element(By.XPATH, ".//div[@class='position-location text-large']").text

                print(f"Job {i}:")
                print(f" - Position: {position}")
                print(f" - Department: {department}")
                print(f" - Location: {location}")

                time.sleep(5)
                assert "Quality Assurance" in position, f"Position does not contain 'Quality Assurance'-> {position}"
                assert "Quality Assurance" in department, f"Department does not contain 'Quality Assurance' -> {department}"
                assert "Istanbul, Turkiye" in location, f"Location does not contain 'Istanbul, Turkiye' -> {location}"
            except AssertionError as e:
                self.driver.save_screenshot(f"screenshot_check_job_fail_{i}.png")
                print(f"[HATA] {e}")
    
    def click_view_role(self):
      actions = ActionChains(self.driver)
      click_view_button = self.driver.find_element(By.XPATH, global_constant.CLICK_VIEW_BUTTON)
      self.driver.execute_script("""
              var select = document.querySelector('#filter-by-location');
              if (select) {
                  var event = new Event('change', { bubbles: true });
                  select.dispatchEvent(event);
              }
          """, click_view_button)
      actions.move_to_element(click_view_button).click().perform()
      
      time.sleep(5)
      job_links = self.driver.find_elements(By.XPATH, "//a[text()='View Role']")

      for i, link in enumerate(job_links, start=1):
         try:
              print(f"\nJob {i} details")
              link.click()
              self.driver.switch_to.window(self.driver.window_handles[-1])
              time.sleep(3)

              position = self.driver.find_element(By.XPATH, "//div[@class='posting-headline']/h2").text
              location = self.driver.find_element(By.XPATH, "//div[contains(@class,'location')]").text
              department = self.driver.find_element(By.XPATH, "//div[contains(@class,'department')]").text
              work_type = self.driver.find_element(By.XPATH, "//div[contains(@class,'workplaceTypes')]").text

              print(f" - Position: {position}")
              print(f" - Department: {department}")
              print(f" - Location: {location}")
              print(f" - Work Type: {work_type}")

              assert "quality assurance" in position.lower(), f"[HATA] Position does not contain 'Quality Assurance' → {position}"
              assert "quality assurance" in department.lower(), f"[HATA] Department does not contain 'Quality Assurance' → {department}"
              assert "istanbul, turkiye" in location.lower(), f"[HATA] Location does not contain 'Istanbul, Turkiye' → {location}"
         except AssertionError as e:
            self.driver.save_screenshot(f"screenshot_click_view_role_{i}.png")
            print(f"[HATA] {e}")
   
    def run(self):
      self.visit_homePage()
      self.visit_career_page()
      self.blocks_are_open_or_not()
      self.visit_QA_jobs()
      self.filter_by_location()
      self.check_that_all_job()
      self.click_view_role()
if __name__ == "__main__":
  test = VisitInsider()
  test.run()