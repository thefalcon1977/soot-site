FROM postgres:16-alpine

# Copy custom PostgreSQL configuration
COPY ./configs/postgresql.conf /etc/postgresql/postgresql.conf

# Set correct ownership for the config file
RUN chown postgres:postgres /etc/postgresql/postgresql.conf

# Copy initialization script
COPY ./command.sh /docker-entrypoint-initdb.d/command.sh

# Make the initialization script executable
RUN chmod +x /docker-entrypoint-initdb.d/command.sh

# Tell PostgreSQL to use the custom config file
CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]