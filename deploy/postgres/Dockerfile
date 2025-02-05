FROM postgres:15

# Copy initialization scripts
COPY init.sql /docker-entrypoint-initdb.d/

# The official Postgres image automatically runs scripts in /docker-entrypoint-initdb.d/
# when the container starts for the first time and creates the default database 