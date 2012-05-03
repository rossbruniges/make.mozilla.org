# Get postgres up and running
class postgresql {
    package { "postgresql":
        ensure => installed;
    }

    package { "postgresql-client":
        ensure => installed;
    }

    package { "libpq-dev":
        ensure => installed,
        require => Package['postgresql'];
    }

    service { "postgresql":
        name => 'postgresql-8.4',
        ensure => running,
        enable => true,
        hasstatus => true,
        require => [Package['postgresql'], Package['postgresql-client']];
    }

    exec { "create_db_user":
        command => "echo \"CREATE ROLE ${::db_user} NOSUPERUSER NOCREATEDB NOCREATEROLE PASSWORD '${::db_pass}';\" | sudo -u postgres psql -f -",
        unless => "sudo -u postgres psql -tAc \"SELECT 1 FROM pg_roles WHERE rolname='${::dbuser}';\" | grep 1",
        require => Service['postgresql'];
    }
}
