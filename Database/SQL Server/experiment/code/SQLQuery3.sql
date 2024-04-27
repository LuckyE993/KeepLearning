use [0107]

IF EXISTS (SELECT * FROM sys.views WHERE object_id = OBJECT_ID(N'[dbo].[v_sc]'))
    DROP VIEW [dbo].[v_sc];
GO

CREATE VIEW [dbo].[v_sc] AS
SELECT 学生.sno, 学生.sname, 课程.cname, 选修.grade
FROM 学生
JOIN 选修 ON 学生.sno = 选修.sno
JOIN 课程 ON 选修.cno = 课程.cno;
GO

use [0107]
 --2.1 查询2学分的课程名及选修的学生名和成绩
SELECT DISTINCT v_sc.sname
FROM v_sc
WHERE NOT EXISTS (
    
    SELECT 1
    FROM 课程 c
    WHERE c.ccredit = 2
    AND NOT EXISTS (
        
        SELECT 1
        FROM v_sc v2
        WHERE v2.sname = v_sc.sname AND v2.cname = c.cname
    )
);


-- --2.2 检索3学分课程的课程号和课程名
SELECT cno, cname
FROM 课程
WHERE ccredit = 3;

---- 2.3 检索年龄大于23岁的男学生的学号和姓名
SELECT sno, sname
FROM 学生
WHERE age > 23 AND sex = '男';
use [0107]
-- 2.4 检索选修了所有2学分课程的男学生姓名
SELECT sname
FROM 学生
WHERE sno IN (
    SELECT sno
    FROM 选修
    JOIN 课程 ON 选修.cno = 课程.cno
    WHERE ccredit = 2
    GROUP BY sno
    HAVING COUNT(*) = (SELECT COUNT(*) FROM 课程 WHERE ccredit = 2)
) AND sex = '男';

-- 2.5 检索至少选修两门课程的学生学号
SELECT sno
FROM 选修
GROUP BY sno
HAVING COUNT(cno) >= 2;

-- 2.6 检索你没有选修课程的课程号

SELECT cno
FROM 课程
WHERE cno NOT IN (
    SELECT cno
    FROM 选修
    WHERE sno = '0107'
);


use [0107]
-- 2.7 统计有学生选修的课程门数
SELECT COUNT(DISTINCT cno) 
FROM 选修;

-- 2.8 求选修数据库课程的学生的平均年龄
SELECT AVG(age) AS AvgAge
FROM 学生
WHERE sno IN (
    SELECT sno
    FROM 选修
    JOIN 课程 ON 选修.cno = 课程.cno
    WHERE cname = '数据库'
);

-- 2.9 统计每门课程的学生选修人数（超过10人的课程才统计）
SELECT cno, COUNT(*) AS NumStudents
FROM 选修
GROUP BY cno
HAVING COUNT(*) > 10
ORDER BY COUNT(*) DESC, cno ASC;

use [0107]
-- 2.10 检索所有与你同姓的学生的姓名和年龄
SELECT sname, age
FROM 学生
WHERE sname LIKE '孙%';

-- 2.11 在SC中检索成绩为空值的学生学号和课程号
SELECT sno, cno
FROM 选修
WHERE grade IS NULL;

-- 2.12 求年龄大于女同学平均年龄的男学生姓名和年龄
SELECT sname, age
FROM 学生
WHERE sex = '男' AND age > (
    SELECT AVG(age)
    FROM 学生
    WHERE sex = '女'
);
