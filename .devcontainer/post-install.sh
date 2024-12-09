#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y ruby-full build-essential zlib1g-dev pip
# pip install -r /workspaces/ada-2024-project-fadadudata2024/pip_requirements.txt

echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

gem install jekyll bundler
