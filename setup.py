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

import sys
from distutils.core import setup
from os.path import join, dirname

sys.path.append(join(dirname(__file__), 'JiraRobot'))

execfile(join(dirname(__file__), 'JiraRobot', 'version.py'))

DESCRIPTION = """
JiraRobot is a robot library for interacting with
JIRA through the use of jirapython and JIRA REST API
"""[1:-1]

setup(name              = 'JiraRobot',
      version           = VERSION,
      description       = 'Robot library for interacting with JIRA',
      long_description  = DESCRIPTION,
      author            = 'Adam Simmons',
      author_email      = '<tarmstrong@navinet.net>, <smcmorran@navinet.net>, <gnixon@navinet.net>, <asimmons@navinet.net>',
      url               = 'https://github.com/NaviNet/JiraRobot',
      license           = 'Apache License 2.0',
      keywords          = 'robotframework robot testing testautomation jira restapi jirarobot',
      platforms         = 'any',
      classifiers       = [
                              "License :: OSI Approved :: Apache Software License",
                              "Programming Language :: Python",
                              "Development Status :: 4 - Beta",
                              "Intended Audience :: Developers",
                              "Programming Language :: Python :: 3.6",
                              "Topic :: Software Development :: Testing",
                              "Topic :: Software Development :: Quality Assurance"
                        ],
      install_requires  = [
							'robotframework >= 3.2.2',
							'jira >= 0.25'
				],
      packages          = ['JiraRobot'],
      data_files        = [('JiraRobotTests', ['Tests/acceptance/JiraRobotTest.txt', 'Tests/acceptance/FILE.txt', 'Docs/JiraRobot-KeywordDocumentation.html'])],
      download_url      = 'https://github.com/NaviNet/JiraRobot/tarball/1.1',
      )