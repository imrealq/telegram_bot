#!/usr/bin/bash

# 0 7-22/4 * * * # set time
cd ~/Workspace/QNewsFeedBot
source .venv/bin/activate
source .env
.venv/bin/python send_message.py
