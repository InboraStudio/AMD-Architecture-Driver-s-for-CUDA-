# Overview for ROCm.mk

This Makefile builds the various projects that makes up ROCm in the correct order.
It is expected to be run in an environment with the tooling set up. An easy way
to do this is to use Docker.

## Targets

* all (default)
* rocm-dev (a subset of all)
* clean
* list_components
* help
* T_foo
* C_foo

## Makefile Variables

* PEVAL set to 1 to enable some Makefile debugging code.
* RELEASE\_FLAG set to "" to avoid passing "-r" to builds, effect is package defined.
* NOBUILD="foo bar" to avoid adding foo and bar into the dependencies of top level targets. They still may be
  built if they are needed as dependencies of other top level targets.
* toplevel

## Makefile assumptions

### Requirements for package "foo"

#### program build\_foo.sh

* Should take option "-c" to clean
* Should take option "-r" to do a normal "RelWithDeb" build

### For package "foo" we define some targets

* T\_foo - The main build target, calls "build\_foo.sh -r"
* C\_foo - Clean target, calls "build_foo.sh -c"
