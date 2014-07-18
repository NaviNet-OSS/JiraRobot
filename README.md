JiraRobot library for Robot Framework
==================================================


Introduction
------------

JiraRobot is a Robot Framework Library to interact with JIRA through JIRA's REST API. JiraRobot uses a python library called [jira-python](https://pypi.python.org/pypi/jira/0.25).

- Information about JiraRobot keywords can be found on the [JiraRobot Keyword Documentation](http://navinet.github.io/JiraRobot/JiraRobot-KeywordDocumentation.html) page.
- The API documentaton for jira-python can be found [here](https://jira-python.readthedocs.org/en/latest/index.html)
- So far this library has been tested and fuctions with JIRA versions 5 and 6

Requirements
------------
* Python 2.7.4 (Newer versions not tested)
* Robot Framework 2.8.4 (Newer versions not tested)
* jira 0.25 (python library) (Newer versions not tested)

Installation
------------
#### Using pip ####

The recommended installation tool is [pip](http://pip-installer.org).

Install pip.
Enter the following:

    pip install JiraRobot

Append ``--upgrade`` to update both the library and all 
its dependencies to the latest version:

    pip install --upgrade JiraRobot

To install a specific version enter:

    pip install JiraRobot==(DesiredVersion)

#### Manual Installation ####

To install JiraRobot manually, install all dependency libraries before installing JiraRobot.

1) Install [Robot Framework installed](http://code.google.com/p/robotframework/wiki/Installation).

2) Download source distributions (``*.tar.gz`` / ``*.zip``) for the library and its
   dependencies.

  Jira-Python dependencies:

   - [https://pypi.python.org/pypi/requests](https://pypi.python.org/pypi/requests/2.2.1)
   - [https://pypi.python.org/pypi/oauthlib](https://pypi.python.org/pypi/oauthlib/0.6.3)
   - [https://pypi.python.org/pypi/ipython](https://pypi.python.org/pypi/ipython/2.1.0)
   - [https://pypi.python.org/pypi/tlslite](https://pypi.python.org/pypi/tlslite/0.4.6)

  JiraRobot and dependencies:

   - [https://pypi.python.org/pypi/jirarobot](https://pypi.python.org/pypi/jirarobot)
   - [https://pypi.python.org/pypi/jira](https://pypi.python.org/pypi/jira/0.25)

3) Extract each source distribution to a temporary location using 7zip (or your preferred zip program).

4) Open command line and go to each directory that was created from extraction and install each project using:

       python setup.py install

#### Uninstall ####

To uninstall JiraRobot use the following pip command: 

    pip uninstall JiraRobot

However, if the package was installed manually it will need to be uninstalled manually:

1) Navigate to ``C:\Python27`` and delete JiraRobotTests

2) Navigate to ``C:\Python27\Lib\site-packages`` and delete JiraRobot-1.0-py2.7.egg-info and the folder ``JiraRobot``

Directory Layout
----------------

*JiraRobot/JiraRobot.py* :
    The Robot Python Library that makes use of Jira-Python.

*Tests/Acceptance/JiraRobotTest.txt* :
    Example test file to display what various keywords from JiraRobot Library accomplish

*doc/JiraRobot-KeywordDocumentation.html* :
    Keyword documentation for the JiraRobot library.


Usage
-----

To write tests with Robot Framework and JiraRobot, 
JiraRobot must be imported into your Robot test suite.
See [Robot Framework User Guide](http://code.google.com/p/robotframework/wiki/UserGuide) for more information.

Running the Demo
----------------

The test file *JiraRobotTest.txt*, is an easily executable test for Robot Framework using JiraRobot Library. 
For in depth detail on how the keywords function, read the Keyword documentation found here: [Keyword Documentation](http://navinet.github.io/JiraRobot/JiraRobot-KeywordDocumentation.html)

Before running the tests, certain variables must be changed to make a successful test run; 

- jirausername - The user you wish to authenticate with 
- jirapassword - If a username is given this can be set as that users password. Optional, but if username is given it will prompt for password at test execution but won't save the password
- jiraserver - The url of the JIRA server to connect to
- usertoassign - The second user to assign to the second issue created (should be different from the orignal user but can be the same if you desire)

In the create issue keywords the variables below may need changed to match yoru JIRA server

- project
- issue type
- priority 

To run the test after installing, navigate to ``C:\Python\JiraRobotTests`` directory. Open a command prompt withing this folder and run:

    pybot JiraRobotTest.txt

Things To Note When Creating Issues
-----------------------------------
The [Create Issues Example](https://developer.atlassian.com/display/JIRADEV/JIRA+REST+API+Example+-+Create+Issue) page is full of useful information in what is required for creating issues, including customfields and issue field value types which are  explained in simple terms below.

When using the *Create Issue* keyword a dictionary must be passed in, in the form of a string (see the [Keyword Documentation](http://navinet.github.io/JiraRobot/JiraRobot-KeywordDocumentation.html) for more information). 

In this dictionary/string issue field names must be stated along with their respective values. Some field types my only accept certain types of values or patterns e.g. Date Fields must be input in the format 'YYYY-MM-DD' and MultiSelect fields will only accept an array of dictionaries ("customfield_10008": [ {"value": "red" }, {"value": "blue" }, {"value": "green" }]). It is very important to get the value type right or an error will be thrown so check [here](https://developer.atlassian.com/display/JIRADEV/JIRA+REST+API+Example+-+Create+Issue#JIRARESTAPIExample-CreateIssue-Examplesofhowtosetcustomfielddataforotherfieldtypes:) for more information on field and their value types.

Some issues may have custom fields the names of these fields is the ID of the field itself generally in the form 'customfield_(NUM)'. The ID of the field can be found by inspecting the element in an internet browser and getting the element ID. More information can be found [here](https://developer.atlassian.com/display/JIRADEV/JIRA+REST+API+Example+-+Create+Issue#JIRARESTAPIExample-CreateIssue-Exampleofcreatinganissueusingcustomfields).

It may be of use to follow the example issue creation in the *JiraRobotTest.txt* file.

Getting Help
------------
The [user group for Robot Framework](http://groups.google.com/group/robotframework-users) is the best place to get help. Include in the post:

- Full description of what you are trying to do and expected outcome
- Version number of JiraRobot, Robot Framework, and Jira-Python
- Traceback or other debug output containing error information