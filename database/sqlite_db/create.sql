CREATE TABLE IF NOT EXISTS tests (
    url TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS reports (
    id              INTEGER PRIMARY KEY,
    tool            TEXT    not null,
    score           INTEGER,
    score_weight    INTEGER,
    notes           TEXT,
    timestamp       TEXT    not null,
    test_id         INTEGER not null,

    FOREIGN KEY(test_id) REFERENCES tests(id)
);

CREATE TABLE IF NOT EXISTS documents (
    id          INTEGER PRIMARY KEY,
    file_name   TEXT,
    file        BLOB,
    report_id   INTEGER not null,

    FOREIGN KEY(report_id) REFERENCES reports(id)
);