DO $$
BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_catalog.pg_database
        WHERE datname = 'mydb'
    ) THEN
        EXECUTE 'CREATE DATABASE mydb';
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_catalog.pg_roles
        WHERE  rolname = 'myuser'
    ) THEN
        EXECUTE 'CREATE ROLE myuser LOGIN PASSWORD ''mypassword''';
    END IF;
END
$$;