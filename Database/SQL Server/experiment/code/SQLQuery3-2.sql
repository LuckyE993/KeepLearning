-- 2.1 ��ѯ2ѧ�ֵĿγ�����ѡ�޵�ѧ�����ͳɼ�
SELECT v_sc.cname, v_sc.sname, v_sc.grade
FROM v_sc
JOIN �γ� ON v_sc.cname = �γ�.cname
WHERE �γ�.ccredit = 2;

 --2.2 ����3ѧ�ֿγ̵Ŀγ̺źͿγ���
SELECT cno, cname
FROM �γ�
WHERE ccredit = 3;

-- 2.3 �����������23�����ѧ����ѧ�ź�����
SELECT sno, sname
FROM ѧ��
WHERE age > 23 AND sex = '��';

