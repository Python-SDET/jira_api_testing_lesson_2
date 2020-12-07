"# jira_api_testing_lesson_2" 

1) Make a package for the API wrapper layer  
  a. Add code to __init__.py to locate jira_info file.  This helps prevent file not found errors.  
  b. Pass json instead of getting it from file  
  c. Remove testing code at end of jira_api.py  
  d. Rename functions to handle other entities besides issues  
 
2) Make a package for implementation layer  
  a. Add code to __init__.py to locate jira_info file.  This helps prevent file not found errors.  
  b. Place the issue_input.yaml in this package to load for needed json to pass.  
  c. Make a class to organize transactions by entity:  Project, Issue, Sprint, etc. 
  d. The constructor of each inner class will contain the url that points to each entity
  e. Notice that the parent class needs to be passed to the inner class to bind them together  
  
