#!/bin/sh

fpm \
  -s deb \
  -t rpm \
  --no-auto-depends \
  --conflicts cosmic-edit \
  $@
