#!/bin/bash

i=0
while ! nc postgres 5432 >/dev/null 2>&1 < /dev/null; do
    i=`expr $i + 1`

    if [ $i -ge 50 ]; then
        echo "$(date) - PostgreSQL still not reachable, giving up"
        exit 1
    fi

    echo "$(date) - waiting for PostgreSQL..."
    sleep 1
done

echo "PostgreSQL connection established"
