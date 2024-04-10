
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
