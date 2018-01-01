#!/usr/bin/env python
#####################################
# Installation module for Knockpy	
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Gareth Darby (gazcbm)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update knockpy - A  python tool designed to enumerate subdomains through a wordlist - by guelfoweb"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/guelfoweb/knock.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="knockpy"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python-dnspython"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python-dnspython"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, echo -e "Opening vim in 10 seconds- Please enter your Virus Total API key", sleep 10s, vim knockpy/config.json, python setup.py install"

# CREATE LAUNCHER
LAUNCHER="knockpy"

