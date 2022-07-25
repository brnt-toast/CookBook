ALTER TABLE ProductList -- targeting a table created in MySQLWorkBench using sakila
MODIFY COLUMN DateAdded DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;
