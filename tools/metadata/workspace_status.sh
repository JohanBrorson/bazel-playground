#!/bin/bash -e

red='\033[0;31m'
no_color='\033[0m'

log_error() {
  local message=$*
  echo -e "${red}ERROR:${no_color} $message"
  exit 1
}

if ! command -v git >/dev/null 2>&1; then
  log_error "Failed to find git"
fi

commit_sha=$(git rev-parse HEAD)
echo "COMMIT_SHA $commit_sha"

git_branch=$(git rev-parse --abbrev-ref HEAD)
echo "GIT_BRANCH $git_branch"
