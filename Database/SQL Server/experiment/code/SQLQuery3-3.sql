
-- 2.4 ����ѡ��������2ѧ�ֿγ̵���ѧ������
SELECT sname
FROM ѧ��
WHERE sno IN (
    SELECT sno
    FROM ѡ��
    JOIN �γ� ON ѡ��.cno = �γ�.cno
    WHERE ccredit = 2
    GROUP BY sno
    HAVING COUNT(*) = (SELECT COUNT(*) FROM �γ� WHERE ccredit = 2)
) AND sex = '��';

-- 2.5 ��������ѡ�����ſγ̵�ѧ��ѧ��
SELECT sno
FROM ѡ��
GROUP BY sno
HAVING COUNT(cno) >= 2;

-- 2.6 ������û��ѡ�޿γ̵Ŀγ̺�

SELECT cno
FROM �γ�
WHERE cno NOT IN (
    SELECT cno
    FROM ѡ��
    WHERE sno = '0107'
);


