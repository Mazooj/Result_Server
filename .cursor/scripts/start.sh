#!/usr/bin/env bash
set -euo pipefail

sudo service mariadb start 2>/dev/null || sudo service mysql start
/workspace/.cursor/scripts/mysql-init.sh
