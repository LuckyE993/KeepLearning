﻿
ALTER TABLE 学生
ADD addr NVARCHAR(100);

ALTER TABLE 课程
ALTER COLUMN cname NVARCHAR(50) NOT NULL;