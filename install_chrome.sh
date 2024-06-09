# assuming you won't have any dependency issue

#!/bin/bash

# chrome Deb Package
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# install dpkg
sudo dpkg -i google-chrome-stable_current_amd64.deb

# check installation
google-chrome --version

