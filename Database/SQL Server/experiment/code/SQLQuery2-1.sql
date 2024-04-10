use [0107]
IF OBJECT_ID('选修', 'U') IS NOT NULL
    DROP TABLE 选修;
IF OBJECT_ID('课程', 'U') IS NOT NULL
    DROP TABLE 课程;
IF OBJECT_ID('学生', 'U') IS NOT NULL
    DROP TABLE 学生;
    
CREATE TABLE 学生 (
    sno CHAR(4) PRIMARY KEY,
    sname VARCHAR(50) NOT NULL UNIQUE,
    age INT,
    sex CHAR(2) NOT NULL DEFAULT '男'
);


CREATE TABLE 课程 (
    cno CHAR(4) PRIMARY KEY,
    cname VARCHAR(3),
    cpno CHAR(4),
    ccredit INT ,
    CONSTRAINT fk_cpno FOREIGN KEY (cpno) REFERENCES 课程(cno)
);

CREATE TABLE 选修 (
    sno CHAR(4),
    cno CHAR(4),
    grade INT CHECK (grade BETWEEN 0 AND 100),
    PRIMARY KEY (sno, cno),
    FOREIGN KEY (sno) REFERENCES 学生(sno),
    FOREIGN KEY (cno) REFERENCES 课程(cno)
);

--([grade]>=(0) AND [grade]<=(100))