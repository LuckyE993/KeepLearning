-- 2.7 ͳ����ѧ��ѡ�޵Ŀγ�����
SELECT COUNT(DISTINCT cno) 
FROM ѡ��;

-- 2.8 ��ѡ�����ݿ�γ̵�ѧ����ƽ������
SELECT AVG(age) AS AvgAge
FROM ѧ��
WHERE sno IN (
    SELECT sno
    FROM ѡ��
    JOIN �γ� ON ѡ��.cno = �γ�.cno
    WHERE cname = '���ݿ�'
);

-- 2.9 ͳ��ÿ�ſγ̵�ѧ��ѡ������������10�˵Ŀγ̲�ͳ�ƣ�
SELECT cno, COUNT(*) AS NumStudents
FROM ѡ��
GROUP BY cno
HAVING COUNT(*) > 10
ORDER BY COUNT(*) DESC, cno ASC;