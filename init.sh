#!/bin/bash

function tab() {
  osascript 2>/dev/null <<EOF
    tell application "System Events"
      tell process "Terminal" to keystroke "t" using command down
    end
    tell application "Terminal"
      activate
      do script with command "cd \"$PWD\"; eval \$(docker-machine env); $*" in window 1
    end tell
EOF
}

virtualenv venv
venv/bin/pip install -r requirements.txt

tab docker-compose up

echo -e "Once Docker is up, you can run:\n\nsource venv/bin/activate\n\n./manage.py syncdb --noinput --migrate\n\npython populate.py\n\n./manage.py runserver"
