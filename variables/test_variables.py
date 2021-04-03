

class TestVariables(object):
    # Github Credentials
    username = "***@gmail.com"
    password = "******"
    github_id = "*****"

    # Common Variables
    website_url = "https://www.github.com"
    repository_name = "test123"
    issue_name_01 = "issue_01"
    issue_01_desc = "this is the issue:" + issue_name_01
    issue_name_02 = "issue_02"
    issue_02_desc = "this is the issue:" + issue_name_02
    issue_comment_01 = "This Comment is part of the Challenge 3"
    issue_comment_02 = "This Comment is part of the Challenge 4"


# Following are the Element Locators
    # XPATH
    xpath_create_repository = "//*[contains(text(),'Create repository')]"
    xpath_new_repository = "//*[@href=\"/new\"]/descendant::*[@class=\"octicon octicon-repo\"]"
    xpath_repository_name = "//span[contains(.,\'{}\')]"
    xpath_repository_settings = "//span[contains(.,\'Settings\')]"
    xpath_repository_settings_title = "//h2[contains(text(),'Settings')]"
    xpath_delete_repository = "//summary[contains(text(),'Delete this repository')]"
    xpath_delete_confirmation_input = "//div[@class='Box-body overflow-auto']//input[@name='verify']"
    xpath_delete_confirmation_button = "//button[contains(.,\'I understand the consequences, delete this repository\')]"
    xpath_issues_button = "//span[contains(.,\'Issues\')]"
    xpath_new_issue_button = "//span[contains(.,\'New issue\')]"
    xpath_issue_preview = "//button[contains(.,\'Preview\')]"
    xpath_issue_body = "//textarea[@id=\'issue_body\']"
    xpath_submit_issue = "//button[contains(.,\'Submit new issue\')]"
    xpath_issue_mention = "//*[contains(@id,'suggester-issue')]"
    xpath_comment_button = "//button[contains(.,\'Comment\')]"
    xpath_select_emoji = "//div[contains(@id,'issuecomment')]//summary[contains(@class,'btn-link link-gray timeline-comment-action')]//*[local-name()='svg']"
    xpath_thumbs_up = "//*[contains(@id,\"issuecomment\")]//button[1]/g-emoji"
    xpath_thumbs_down = "//*[contains(@id,\"issuecomment\")]//button[2]/g-emoji"
    xpath_laugh = "//*[contains(@id,\"issuecomment\")]//button[3]/g-emoji"
    xpath_hooray = "//*[contains(@id,\"issuecomment\")]//button[4]/g-emoji"
    xpath_confused = "//*[contains(@id,\"issuecomment\")]//button[5]/g-emoji"
    xpath_heart = "//*[contains(@id,\"issuecomment\")]//button[6]/g-emoji"
    xpath_rocket = "//*[contains(@id,\"issuecomment\")]//button[7]/g-emoji"
    xpath_eyes = "//*[contains(@id,\"issuecomment\")]//button[8]/g-emoji"
    xpath_issue_link = "//a[contains(@class,\"issue-link\")]"


    # Link Text
    link_text_sign_in = "Sign in"
    link_text_create_repository = "Create repository"
    link_text_sign_in_verify = "Marketplace"
    link_test_new_issue = "New issue"

    # ID
    id_login_field = "login_field"
    id_password = "password"
    id_repository_name = "repository_name"
    id_issue_title = "issue_title"
    id_latest_issue = "issue_2_link"
    id_new_comment_field = "new_comment_field"

    # Name
    name_commit = "commit"


