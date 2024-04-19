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
