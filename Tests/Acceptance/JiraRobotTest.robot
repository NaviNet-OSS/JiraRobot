*** Settings ***
Library         JiraRobot

*** Variables *** 
${jirausername}         YOURUSERNAME   # optional, but will auth with anon account if left empty
${jirapassword}         YOURPASSWORD   # optional, If a username was specified in ${jirausername} and ${jirapassword} is empty, user will be prompted for password at runtime 

${jiraserver}           YOURJIRASERVER   # e.g. http://devjira01
${project}              PROJECT

${usertoassign}         ANOTHERUSER

*** Test Cases ***

JIRARobot Test
    Connect To Jira 	     ${jirausername}       ${jirapassword}        options={'server': '${jiraserver}'}
    Log 	get current user

    ${issue1}=     Create New Issue         ${project}        Test Jira Robot             Testing Jira Robot issue creation          Task            Medium      True   # The project, issue type and priority may need changed
    ${issue2}=     Create new Issue         ${project}        New JiraRobot Issue         Look into jirarobot issue                  Bug             Blocker            # to match your JIRA

    Create Issue Link           relates to             ${issue2}                ${issue1} 
    Add Watcher To Issue		${issue2} 		       ${jirausername}
    Add Comment To Issue 		${issue2} 		       Testing add comments to issue
    Assign User To Issue	 	${issue2} 	           ${usertoassign}
    Add Attachment To Issue     ${issue2}              ./FILE.txt               AttachmentFile.txt


*** Keywords ***

Create New Issue          
    [arguments]         ${project}          ${summary}          ${description}      ${issuetype}        ${priority}       ${assigntouser}=False
    ${issuestring}=      Set Variable        {'project': {'key': '${project}'}, 'summary': '${summary}', 'description': '${description}', 'issuetype': {'name': '${issuetype}'}}
    ${issue}=           Create Issue        ${issuestring}      ${assigntouser}
    Log     ${issue}
    [return]    ${issue} 