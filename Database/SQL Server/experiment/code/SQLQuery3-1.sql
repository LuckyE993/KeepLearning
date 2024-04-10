IF EXISTS (SELECT * FROM sys.views WHERE object_id = OBJECT_ID(N'[dbo].[v_sc]'))
    DROP VIEW [dbo].[v_sc];
GO

CREATE VIEW [dbo].[v_sc] AS
SELECT ѧ��.sno, ѧ��.sname, �γ�.cname, ѡ��.grade
FROM ѧ��
JOIN ѡ�� ON ѧ��.sno = ѡ��.sno
JOIN �γ� ON ѡ��.cno = �γ�.cno;
GO
