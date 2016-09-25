# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:14:02 2016

@author: Sean
"""

import os

scopes = ['identity', 'submit', 'read']

app_key = os.getenv('MY_KEY')
app_secret = os.getenv('MY_SECRET_KEY')
access_token = os.getenv('access_token')
refresh_token = os.getenv('refresh_token')
