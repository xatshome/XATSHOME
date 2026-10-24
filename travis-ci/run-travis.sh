#!/usr/bin/env sh
set -eu

# Resolve the XATSHOME repository root from this script's location.
travis_dir=\
$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
myrepo_root=$(CDPATH= cd -- "$travis_dir/.." && pwd)

cd "$myrepo_root"
exec make -f ./Makefile_workflow "$@"
