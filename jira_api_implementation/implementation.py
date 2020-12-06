import yaml
from jira_api_wrapper.jira_api import JiraApi


class JiraImplementation:
    def __init__(self):
        issue_input_stream = open('issue_input.yaml', 'r')
        self.issue_json = yaml.load(issue_input_stream, Loader=yaml.SafeLoader)
        self.jira_api = JiraApi()
        self.project = self.Project(self)
        self.issue = self.Issue(self)
        self.sprint = self.Sprint(self)

    class Project:
        def __init__(self, implementation):
            self.project_url = r'rest/api/3/project/'
            self.implementation = implementation

        def get_project(self, project_id=None):
            return self.implementation.jira_api.get_entity(self.project_url, project_id)

    class Issue:
        def __init__(self, implementation):
            self.issue_url = r'rest/api/2/issue/'
            self.implementation = implementation

        def get_issue(self, issue_id=None):
            return self.implementation.jira_api.get_entity(self.issue_url, issue_id)

        def set_story_points(self, point_value, issue_id=None):
            issue_json = self.implementation.issue_json
            issue_json['fields']['customfield_10026'] = point_value
            return self.implementation.jira_api.create_update_entity(self.issue_url, issue_json, issue_id)

        def update_summary(self, revised_summary, issue_id=None):
            issue_json = self.implementation.issue_json
            issue_json['fields']['summary'] = revised_summary
            return self.implementation.jira_api.create_update_entity(self.issue_url, issue_json, issue_id)

        def update_description(self, revised_description, issue_id=None):
            issue_json = self.implementation.issue_json
            issue_json['fields']['description'] = revised_description
            return self.implementation.jira_api.create_update_entity(self.issue_url, issue_json, issue_id)

        def update_labels(self, label_list, issue_id=None):
            issue_json = self.implementation.issue_json
            issue_json['fields']['labels'] = label_list
            return self.implementation.jira_api.create_update_entity(self.issue_url, issue_json, issue_id)

    class Sprint:
        def __init__(self, implementation):
            self.sprint_url = r'/rest/agile/1.0/board/1/sprint'
            self.implementation = implementation

        def get_sprint(self, sprint_id=None):
            return self.implementation.jira_api.get_entity(self.sprint_url, sprint_id)


jira_implementation = JiraImplementation()
sprints = jira_implementation.sprint.get_sprint()
projects = jira_implementation.project.get_project('AD')
jira_implementation.issue.set_story_points(1, 'AD-6')
jira_implementation.issue.update_labels(['LABEL1C', 'LABEL2C', 'LABEL3C'], 'AD-6')
updated_issue = jira_implementation.issue.get_issue('AD-6')
print(updated_issue)