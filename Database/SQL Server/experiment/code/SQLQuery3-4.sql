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