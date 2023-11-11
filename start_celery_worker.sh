#!/usr/bin/env bash

celery -A health_central.celery worker --loglevel=info ;
