#!/bin/bash
set -e
echo "--- start"
TIMEOUT=30
COUNT=0
until psql -U postgres -c '\l'; do
    echo "--- Waiting for PostgreSQL to become available..."
    sleep 1
    ((COUNT++))
    if [ $COUNT -ge $TIMEOUT ]; then
        echo "Error: PostgreSQL not available after $TIMEOUT seconds."
        exit 1
    fi
done
echo "--- PostgreSQL is ready."
psql -U postgres -d postgres -c "CREATE EXTENSION IF NOT EXISTS pg_trgm;"
echo "--- pg_trgm extension enabled."