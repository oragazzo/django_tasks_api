DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'basic_api') THEN
        CREATE DATABASE basic_api;
    END IF;
END
$$;