#!/usr/bin/env bash
set -euo pipefail

if ! sudo mysql -e "SELECT 1" >/dev/null 2>&1; then
  sudo service mysql start
fi

sudo mysql -e "
CREATE DATABASE IF NOT EXISTS student_info;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Mazooz#1';
FLUSH PRIVILEGES;
"
