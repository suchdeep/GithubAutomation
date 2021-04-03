import pytest
from variables.test_variables import TestVariables as var
from keywords.keywords import GithubSeleniumKeywords as keywords


class TestGithubSelenium(object):
    @pytest.mark.qachallenge
    def test_QAChallenge(self):
        keywords.open_browser_with_url(self, var.website_url)
        keywords.signin_to_github(self, var.username, var.password)
        keywords.create_repository(self, var.repository_name)
        keywords.create_issue_and_mention_issue_in_new_issue(self, var.repository_name)
        keywords.add_comment_and_emoji_to_an_issue(self, var.repository_name,
                                                                 var.xpath_heart)
        keywords.add_comment_and_navigate_to_issue(self, var.repository_name)
        keywords.delete_repository(self, var.repository_name)