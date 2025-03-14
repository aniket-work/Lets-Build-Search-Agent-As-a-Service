#!/bin/bash

# Create directories
mkdir -p ./{backend/{api,core,utils},config,scripts}

# Create files
touch ./{app.py,requirements.txt,README.md,.env}
touch ./config/{config.json,settings.yaml}
touch ./backend/{main.py}
touch ./backend/api/{search.py,health.py,info.py}
touch ./backend/core/{agent.py,config.py}
touch ./backend/utils/helpers.py

echo "Project structure created successfully!"
