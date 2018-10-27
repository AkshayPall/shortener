DROP TABLE IF EXISTS surl;

CREATE TABLE surl (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL,
    user_id TEXT NOT NULL,
    long_url TEXT NOT NULL,
    short_link TEXT NOT NULL
);

CREATE INDEX user_link on surl (user_id, short_link);
