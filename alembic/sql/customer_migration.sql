-- upgrade
CREATE TABLE IF NOT EXISTS customer (
    id INT,
    name STRING
) USING DELTA;

-- downgrade
DROP TABLE IF EXISTS customer;
