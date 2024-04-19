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


