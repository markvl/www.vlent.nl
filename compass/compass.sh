#!/bin/bash
# compass/compass.sh - properly invoke the "Compass" program

BASE=$(dirname $(readlink -f $(which "$0")))
export GEM_HOME=$BASE/Gem
export RUBYLIB=$BASE/Gem/lib
$BASE/Gem/bin/compass "$@"
