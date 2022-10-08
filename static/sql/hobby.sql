USE ikigai;
CREATE TABLE hobbies_tmp(
    hobby varchar(30),
    outdoor integer,
    team integer
);
INSERT INTO hobbies_tmp VALUES
('サッカー', 1, 1),
('マラソン', 1, 0),
('ダンス', 0, 1),
('料理', 0, 0);