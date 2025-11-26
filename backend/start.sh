#!/bin/bash
cd /home/xsolai/hdd/Projects/cameleon-poc-showcase/backend
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000






