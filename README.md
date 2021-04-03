# GithubAutomation

This Repository has been created as part of the QA Task:

**Challenge 1**: **Repository Creation**
1. Automate the creation of a repository on Github Challenge 

**Challenge 2**: **Issue Creation** 
    1. Create an issue on Github in the repository created in challenge 
    2. Create another issue on Github while mentioning previous issue in description and title Challenge
    
**Challenge 3**: **Comment to an Issue**
1. Add some comments to the issue created in challenge  
2. Add emoji in the repository created in challenge

**Challenge 4**: **Issue mention in comments link to Issue**
1. Create a new comment and mention any of the previous issue (from challenge #2)
2. Navigate to the issue from the comment Issue mention is mentioning an issue (referencing an issue) by its id with # as prefix, for eg. #456

**Challenge 5**: **Delete repository** 
1. Once all the challenges are accomplished, delete the repository.

The mentioned Challenges have been successfully executed

The github account credentials are  configurable and can be changed by editing the variables in the file: /variables/test_variables.py

**Note**: The automation has been done assuming Chromedriver executable is in the system path, If not present then following modification needs to be done in the **open_browser_with_url** keyword present in **/keywords/keywords.py** file: def open_browser_with_url(self, url): chromedriver = '/path/to/chromedriver' self.driver = webdriver.Chrome(chromedriver)
