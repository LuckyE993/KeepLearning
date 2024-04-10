-- 2.1 查询2学分的课程名及选修的学生名和成绩
SELECT v_sc.cname, v_sc.sname, v_sc.grade
FROM v_sc
JOIN 课程 ON v_sc.cname = 课程.cname
WHERE 课程.ccredit = 2;

 --2.2 检索3学分课程的课程号和课程名
SELECT cno, cname
FROM 课程
WHERE ccredit = 3;

-- 2.3 检索年龄大于23岁的男学生的学号和姓名
SELECT sno, sname
FROM 学生
WHERE age > 23 AND sex = '男';

