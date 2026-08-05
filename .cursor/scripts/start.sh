#!/usr/bin/env bash
set -euo pipefail

sudo service mysql start
/workspace/.cursor/scripts/mysql-init.sh
