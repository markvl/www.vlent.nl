#!/bin/bash
# compass/install.sh - install Compass under the "./Gem" directory

if ! which gem >/dev/null ;then
    echo 'Error: no "gem" command available'
    echo 'Please "sudo aptitude install rubygems1.8" or "ruby1.9.1"'
    exit 1
fi

BASE=$(dirname $(readlink -f $(which "$0")))
cd $BASE # the directory where this script lives

# Temporary version pins to get newer versions of sass and compass.
gem install -i Gem sass --version="3.2.1"
gem install -i Gem compass --version="0.13.alpha.0"
