#!/usr/bin/env sh
set -eu
##################################################################
#
# Resolve the XATSHOME repository root from this script's location
# in .github/workflows.
#
workflow_dir=\
$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
myrepo_root=$(CDPATH= cd -- "$workflow_dir/../.." && pwd)
##################################################################

export XATSHOME=$myrepo_root

##################################################################

cd "$myrepo_root"
exec make -f ./Makefile_workflow "$@"

##################################################################
###################(end-of-[run-workflow.sh])#####################
##################################################################
