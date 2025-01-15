USE testdb;

CREATE TABLE IF NOT EXISTS chat_table (
    room INT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    message VARCHAR(1000)  NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX room_index ON chat_table;