use [0107]
IF OBJECT_ID('ѡ��', 'U') IS NOT NULL
    DROP TABLE ѡ��;
IF OBJECT_ID('�γ�', 'U') IS NOT NULL
    DROP TABLE �γ�;
IF OBJECT_ID('ѧ��', 'U') IS NOT NULL
    DROP TABLE ѧ��;
    
CREATE TABLE ѧ�� (
    sno CHAR(4) PRIMARY KEY,
    sname VARCHAR(50) NOT NULL UNIQUE,
    age INT,
    sex CHAR(2) NOT NULL DEFAULT '��'
);


CREATE TABLE �γ� (
    cno CHAR(4) PRIMARY KEY,
    cname VARCHAR(3),
    cpno CHAR(4),
    ccredit INT ,
    CONSTRAINT fk_cpno FOREIGN KEY (cpno) REFERENCES �γ�(cno)
);

CREATE TABLE ѡ�� (
    sno CHAR(4),
    cno CHAR(4),
    grade INT CHECK (grade BETWEEN 0 AND 100),
    PRIMARY KEY (sno, cno),
    FOREIGN KEY (sno) REFERENCES ѧ��(sno),
    FOREIGN KEY (cno) REFERENCES �γ�(cno)
);

--([grade]>=(0) AND [grade]<=(100))