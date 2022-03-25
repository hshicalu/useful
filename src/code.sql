# Create table in SQL
CREATE TABLE {db_name}.{table_name} (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    title VARCHAR(50),
    content TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

