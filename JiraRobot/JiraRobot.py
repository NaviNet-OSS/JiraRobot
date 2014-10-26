#!/usr/bin/env python


#  Copyright 2013-2014 NaviNet Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


from jira.client import JIRA
import sys
import getpass


class JiraRobot:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    jira = None

    def connect_to_jira(self, JIRAUsername=None,
                        JIRAPassword=None, options=None):
        """
        Connect to a JIRA server.

            Arguments:
                |  JIRAUsername (string)  	|  (Optional) A JIRA Username you wish to authenticate with, will authorise with anonymous account if left empty      				|
                |  JIRAPassword (string)  	|  (Optional) If a username was specified and a password is not the user will be prompted for password at runtime 					|
                |  options (dictionary) 	|  (Optional) A dictionary of options that the JIRA connection will be initialied with 	                                            |

            This must be called first to be able to do most JIRA actions such as creating a new issue and assigning users.
            When connecting to JIRA you may need to authenticate a user. This can be done by passing in Username and Password as parameters. However, should you wish to not have a sensitive password saved in a file,  an option is available to not pass in a Password and a prompt will appear asking for the JIRA password at runtime.


            'connect to jira' can be called on its own and will default options to:
                '{'rest_api_version': '2', 'verify': True,
                'server': 'http://localhost:2990/jira', 'headers': {'X-Atlassian-Token': 'nocheck'},
                'rest_path': 'api', 'resilient': False, 'async': False}'
            These can all be customised as needed.

            Examples:
                |  *Keyword*        |  *Parameters* | 									| 									|
                |  connect to jira  |  				|           						|                          			|
                |  connect to jira  |  asimmons	    | options= {'http://devjira01'} 	|    								|
                |  connect to jira  |  asimmond 	| MyP@ssword 						| {'server': http://devjira01'} 	|
        """

        if JIRAUsername is not None and (JIRAPassword is "" or JIRAPassword is None):
            JIRAPassword = getpass.getpass("\nJIRA Password: ")
		
        print JIRAUsername

        JIRAOptions = eval(options)
        if JIRAUsername is None:
            try:
                self.jira = JIRA(JIRAOptions)
            except:
                sys.__stdout__.write("\nAuthentication to JIRA unsuccessful. Ensure the user used has sufficient access and that Username and Password were correct\n\n")
                sys.exit(1)

        else:
            try:
                self.jira = JIRA(options=JIRAOptions, basic_auth=(str(JIRAUsername),
                                 str(JIRAPassword)))
            except:
                sys.__stdout__.write("\nAuthentication to JIRA unsuccessful. Ensure the user used has sufficient access and that Username and Password were correct\n\n")
                sys.exit(1)

    def create_issue(self, issue_field_dict, assign_current_user=False):
        """
        Creates a new JIRA issue.

            Arguments:
                |  issue_field_dict (string)  			| A dictionary in the form of a string that the user can specify the issues fields and field values 			|
                |  assign_current_user (string/bool)  	| (Optional) A flag to assign the current user to the issue once it is successfully created, defaults to False	|

            Will create a new issue and returns an Issue Key.
            The user will use the issue_field_dict variable to specify the issues field and their respective values. This must be in the form of a string written as a dictionary
                e.g. {'FieldName':'FieldValue'}

            The field value can also be another dictionary (in some field cases this is needed)
                e.g. {'FieldName1':{'key':'value'}, 'FieldName2':FieldValue, 'FieldName3':{'name':'value'}}

            This Create Issue Example page (https://developer.atlassian.com/display/JIRADEV/JIRA+REST+API+Example+-+Create+Issue) is full of useful information in what is required for creating issues, including customfields and issue field value types, it is very important to get the value type right or an error will be thrown.


            Examples:
                |  *Keyword*        	|  *Parameters*   	| 														| 		|
                |  ${issue_field_dict} 	|  {'project':{'key': 'PROJ'}, 'summary':'Create New Issue', 'description':'Creating a new issue', 'issuetype':{'name': 'Bug'}} |    |
                |  connect to jira      |  asimmons         | options= {'http://devjira01'}                         |       |
                |  ${issue}				|  create issue 	|  ${issue_field_dict}									|      	|

                |  connect to jira      |  asimmons         | options= {'http://devjira01'}                         |  		|
                |  ${issue}				|  create issue 	|  ${issue_field_dict}									|  True |
        """
        issue_field_dict = eval(str(issue_field_dict))
        print issue_field_dict

        new_issue = self.jira.create_issue(issue_field_dict)
        if assign_current_user is True:
            self.assign_user_to_issue(new_issue, self.jira.current_user())
        return new_issue

    def create_issue_link(self, link_type, inwardissue,
                          outwardissue, comment=None):
        """
        Create a link between two issues.

            Arguments:
                |  link_type (string)  	| The type of link									|
                |  inwardissue (string)  	| The issue to link from  							|
                |  outwardissue (string)  	| The issue to link to 								|
                |  comment (string)  		| (Optional) A comment to add when joining issues	|

            Example:
                |  *Keyword*        	|  *Parameters* | 									| 			|
                |  connect to jira      |  asimmons     | options= {'http://devjira01'}     |  			|
                |  ${issue}				|  create issue |  ${issue_field_dict}				|  True 	|
                |  create issue link	|  relates to   |  ${issue} 						|  PROJ-385	|
        """
        self.jira.create_issue_link(type=link_type,
                                    inwardIssue=str(inwardissue),
                                    outwardIssue=str(outwardissue))

    def assign_user_to_issue(self, issue, JIRAUsername):
    # TODO: Review docs
        """
        Adds a user to a specified issue's watcher list

        Arguments:
            |  issue (string)  		| A JIRA Issue that a user needs to be assigned to, can be an issue ID or Key		|
            |  JIRAUsername (string)  	| A JIRA Username to assign a user to an issue   									|

        Example:
           |  *Keyword*        		|  *Parameters* | 									|
           |  connect to jira       |  asimmons     | options= {'http://devjira01'}     |
           |  ${issue}				|  create issue |  ${issue_field_dict}				|
           |  assign user to issue	|  ${issue}		|  aSample 							|
        """
        self.jira.assign_issue(issue=issue, assignee=JIRAUsername)

    def get_current_user(self):
        """
        Returns the current user used in the Connect to JIRA keyword.
        """
        return self.jira.current_user()

    def add_watcher_to_issue(self, issue, JIRAUsername):
        """
        Adds a user to a specified issue's watcher list.

        Arguments:
            |  issue (string)  		| A JIRA Issue that a watcher needs added to, can be an issue ID or Key		|
            |  JIRAUsername (string)  	| A JIRA Username to add as a watcher to an issue   					|

        Example:
            |  *Keyword*        	|  *Parameters* | 								|		|
            |  connect to jira  |  asimmons     | options= {'http://devjira01'}     | 		|
            |  ${issue}				|  create issue |  ${issue_field_dict}			|  True |
            |  add watcher to issue	|  ${issue}		|  aSample 						| 		|

        """
        self.jira.add_watcher(issue=issue, watcher=JIRAUsername)

    def add_comment_to_issue(self, issue, comment, visibility=None):
        """
        Adds a comment to a specified issue from the current user.

            Arguments:
                |  issue (string)  		| A JIRA Issue that a watcher needs added to, can be an issue ID or Key	|
                |  comment (string)  		| A body of text to add as a comment to an issue   						|
                |  visibility (string)  	| (Optional)															|

            Example:
                |  *Keyword*        	|  *Parameters* | 									|		|
                |  connect to jira      |  asimmons     |  options= {'http://devjira01'}    | 		|
                |  ${issue}				|  create issue |  ${issue_field_dict}				|  True |
                |  add comment to issue	|  ${issue}		|  Starting work on this issue		| 		|
        """
        self.jira.add_comment(issue=issue, body=comment)

    def add_attachment_to_issue(self, issue, attachment, filename=None):
        """
        Uploads and attaches a file a specified issue. (Note: include the file extention when using the 'filename' option or this will change the file type.)

        Arguments:
            |   issue (string)  	| A JIRA Issue that a watcher needs added to, can be an issue ID or Key		|
            |   attachment (string) | A string pointing to a file location to upload and attach to the issue	|
            |   filename (string)  	| (Optional) A string to rename the file to upon attaching to the issue  	|

        Example:
            |  *Keyword*        		|  *Parameters* | 							         |						|
            |  connect to jira          |  asimmons     | options= {'http://devjira01'}      | 						|
            |  ${issue}					|  create issue |  ${issue_field_dict}	             |  True 			 	|
            |  add attchment to issue	|  ${issue}		|  ./logfile.text			         |  LogInformation.txt	|
        """
        self.jira.add_attachment(issue=issue, attachment=attachment,
                                 filename=filename)
