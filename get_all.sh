#!/usr/bin/env bash

set -e

parent_path=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )


cd $parent_path

. ./.venv/bin/activate

. ./env.sh

./scripts/get_all
