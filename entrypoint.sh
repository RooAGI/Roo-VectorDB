#!/bin/bash
DEFAULT_IFACE=$(ip route | awk '/default/ {print $5}')
CONTAINER_CIDR=$(ip -o -f inet addr show "$DEFAULT_IFACE" | awk '{print $4}')

# Append rule to pg_hba.conf
echo "host all all ${CONTAINER_CIDR} scram-sha-256" >> /etc/postgresql/16/main/pg_hba.conf
echo "host all all 172.0.0.0/8 scram-sha-256" >> /etc/postgresql/16/main/pg_hba.conf
echo "local all all trust" >> /etc/postgresql/16/main/pg_hba.conf

# Optionally ensure listen_addresses is set to '*'
sed -i "s/^#listen_addresses =.*/listen_addresses = '*'/" /etc/postgresql/16/main/postgresql.conf
sed -i "s/^port =.*/port = 8432/" /etc/postgresql/16/main/postgresql.conf

# Initialize if needed
if [ ! -f /var/lib/postgresql/16/main/PG_VERSION ]; then
    echo "Initializing data directory..."
    su - postgres -c "/usr/lib/postgresql/16/bin/initdb -D /etc/postgresql/16/main"
fi

# Start PostgreSQL
#exec su - postgres -c "/usr/lib/postgresql/16/bin/pg_ctl -D /etc/postgresql/16/main -l /var/log/postgresql/postgresql-16-main.log -t 300 start" 
su - postgres -c "nohup /usr/lib/postgresql/16/bin/postgres -D /etc/postgresql/16/main" >/tmp/nohup_pg.out 2>&1 &

tail -f /var/log/postgresql/postgresql*.log
