CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year VARCHAR(45),
    make VARCHAR(45),
    model TEXT,
    active BOOLEAN DEFAULT 1
);



INSERT INTO vehicle  (
    year,
    make,
    model
    ) VALUES (
        "2014",
        "Subaru",
        "Impreza"
    );

INSERT INTO vehicle  (
    year,
    make,
    model
    ) VALUES (
        "2015",
        "Chevy",
        "Malibu"
    );    

INSERT INTO vehicle  (
    year,
    make,
    model
    ) VALUES (
        "2021",
        "GMC",
        "Sierra"
    );

INSERT INTO vehicle  (
    year,
    make,
    model
    ) VALUES (
        "1991",
        "Nissan",
        "240sx"
    );    