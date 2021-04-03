from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from variables.test_variables import TestVariables as var


class GithubSeleniumKeywords:

    def open_browser_with_url(self, url):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)

    def signin_to_github(self, username, password):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, var.link_text_sign_in)))
        element.click()
        element = self.driver.find_element(By.ID, var.id_login_field)
        WebDriverWait(self.driver, 10).until(EC.visibility_of(element))
        element.send_keys(username)
        element = self.driver.find_element(By.ID, var.id_password)
        WebDriverWait(self.driver, 10).until(EC.visibility_of(element))
        element.send_keys(password)
        self.driver.find_element(By.NAME, var.name_commit).click()
        element = self.driver.find_element(By.LINK_TEXT, var.link_text_sign_in_verify)
        WebDriverWait(self.driver, 10).until(EC.visibility_of(element))
        print("Signed In to Github Successfully")

    def create_repository(self, repository_name):
        self.driver.get(self.url)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_new_repository)))
        element.click()
        self.driver.find_element(By.ID, var.id_repository_name).send_keys(repository_name)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_create_repository)))
        element.click()
        print("New Repository created Successfully")

    def create_issue_and_mention_issue_in_new_issue(self, repository_name):
        self.driver.get(self.url)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_repository_name
                                                                                   .format(repository_name))))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_issues_button)))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_new_issue_button)))
        element.click()
        self.driver.find_element(By.ID, var.id_issue_title).send_keys(var.issue_name_01)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_issue_body)))
        element.click()
        element.send_keys(var.issue_01_desc)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_submit_issue)))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, var.link_test_new_issue)))
        element.click()
        self.driver.find_element(By.ID, var.id_issue_title).send_keys(var.issue_name_02)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_issue_body)))
        element.click()
        element.send_keys(var.issue_02_desc)
        element.send_keys(Keys.RETURN)
        element.send_keys("#")
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_issue_mention)))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_submit_issue)))
        element.click()

    def add_comment_and_emoji_to_an_issue(self, repository_name, emoji):
        self.driver.get(self.url)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_repository_name
                                                                                   .format(repository_name))))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_issues_button)))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_issues_button)))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, var.id_latest_issue)))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, var.id_new_comment_field)))
        element.click()
        element.send_keys(var.issue_comment_01)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_comment_button)))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_select_emoji)))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, emoji)))
        element.click()
        print("Emoji Selected")

    def add_comment_and_navigate_to_issue(self, repository_name):
        self.driver.get(self.url)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_repository_name
                                                                                   .format(repository_name))))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_issues_button)))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_issues_button)))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, var.id_latest_issue)))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, var.id_new_comment_field)))
        element.click()
        element.send_keys(var.issue_comment_02)
        element.send_keys(Keys.RETURN)
        element.send_keys("#")
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_issue_mention)))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_comment_button)))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_issue_link)))
        element.click()

    def delete_repository(self, repository_name):
        self.driver.get(self.url)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpath_repository_name
                                                                                   .format(repository_name))))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var
                                                                                   .xpath_repository_settings)))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, var
                                                                                      .xpath_delete_repository)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        delete_repository_text = var.github_id + '/' + repository_name
        element = self.driver.find_element(By.XPATH, var.xpath_delete_confirmation_input)
        WebDriverWait(self.driver, 10).until(EC.visibility_of(element))
        element.send_keys(delete_repository_text)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var
                                                                                  .xpath_delete_confirmation_button)))
        element.click()
        print("Repository Deleted")


