
-- 2.10 ������������ͬ�յ�ѧ��������������
SELECT sname, age
FROM ѧ��
WHERE sname LIKE '��%';

-- 2.11 ��SC�м����ɼ�Ϊ��ֵ��ѧ��ѧ�źͿγ̺�
SELECT sno, cno
FROM ѡ��
WHERE grade IS NULL;

-- 2.12 ���������Ůͬѧƽ���������ѧ������������
SELECT sname, age
FROM ѧ��
WHERE sex = '��' AND age > (
    SELECT AVG(age)
    FROM ѧ��
    WHERE sex = 'Ů'
);