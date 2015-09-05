CREATE TABLE user (
    id TEXT NOT NULL UNIQUE,
    pass TEXT NOT NULL,
    salt TEXT NOT NULL,
    sign_up_time INTEGER NOT NULL,
    nickname TEXT NOT NULL,
    description TEXT NOT NULL,
    PRIMARY KEY(id)
);

INSERT INTO user (id, pass, salt, sign_up_time, nickname, description) VALUES (
    "tom", "mypass", "mysalt", 1, "tomd", "tomgreden"
);
