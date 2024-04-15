import pandas as pd
import sqlite3

# 读取Excel文件
def load_data(excel_file):
	return pd.read_excel(excel_file)


# 创建数据库连接并创建表
def create_table(conn, create_table_sql):
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except Exception as e:
		print(e)


# 主函数
def import_data_from_excel():
	database = "students.db"

	# 创建数据库连接
	conn = sqlite3.connect(database)

	# 创建表格SQL语句
	create_table_finaltest = """
    CREATE TABLE IF NOT EXISTS "finaltest" (
		"班级" TEXT,
		"姓名" TEXT,
		"课程名称" TEXT,
		"成绩" TEXT,
		"学分" REAL,
		"学号" INTEGER,
		"绩点" REAL,
		"专业" TEXT,
		"考试性质" TEXT,
		"年级" INTEGER
	);

    """

	create_table_resit = """
    CREATE TABLE IF NOT EXISTS "resit" (
		"班级" TEXT,
		"姓名" TEXT,
		"课程名称" TEXT,
		"成绩" INTEGER,
		"学分" REAL,
		"学号" INTEGER,
		"绩点" REAL,
		"专业" TEXT,
		"考试性质" TEXT,
		"年级" INTEGER
	);
    """
	create_table_caltemp = """
	CREATE TABLE IF NOT EXISTS caltemp (
	        "班级" TEXT,
			"姓名" TEXT,
			"课程名称" TEXT,
			"成绩" TEXT,
			"学分" REAL,
			"学号" INTEGER,
			"绩点" REAL,
			"专业" TEXT,
			"考试性质" TEXT,
			"年级" INTEGER
	    );
	    """
	create_table_gpa = """
	CREATE TABLE IF NOT EXISTS total_gpa (
	    student_id TEXT PRIMARY KEY,
	    class TEXT,
	    name TEXT,
	    total_gpa REAL
	);
	"""


	# 创建表格
	create_table(conn, create_table_finaltest)
	create_table(conn, create_table_resit)
	create_table(conn, create_table_gpa)
	create_table(conn, create_table_caltemp)

	# 加载数据
	students_df = load_data('./dataset/机器人21级.xlsx')
	resit_df = load_data('./dataset/机器人21级补考.xlsx')

	# 导入数据到SQLite
	students_df.to_sql('finaltest', conn, if_exists='replace', index=False)
	resit_df.to_sql('resit', conn, if_exists='replace', index=False)

	print("Data imported successfully.")

	# 关闭数据库连接
	conn.close()


def process_data(database):
    # 连接到SQLite数据库
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # 复制finaltest表到caltemp表
    cursor.execute("DELETE FROM caltemp")  # 清空caltemp表
    cursor.execute("""
        INSERT INTO caltemp ("班级", "姓名", "课程名称", "成绩", "学分", "学号", "绩点", "专业", "考试性质", "年级")
        SELECT "班级", "姓名", "课程名称", "成绩", "学分", "学号", "绩点", "专业", "考试性质", "年级" FROM finaltest
    """)
    conn.commit()

    # 更新caltemp中的成绩，如果正常考试未通过且补考通过
    cursor.execute("""
        UPDATE caltemp SET "成绩" = (
            SELECT "成绩" FROM resit 
            WHERE caltemp."学号" = resit."学号" 
            AND caltemp."课程名称" = resit."课程名称" 
            AND resit."成绩" >= 60
        )
        WHERE EXISTS (
            SELECT 1 FROM resit
            WHERE caltemp."学号" = resit."学号" 
            AND caltemp."课程名称" = resit."课程名称" 
            AND resit."成绩" >= 60
        ) AND caltemp."成绩" < '60'  -- 假设成绩字段是TEXT，并且未及格的标记是小于60的数值
    """)
    conn.commit()

    # 计算总绩点并更新total_gpa表
    cursor.execute("""
        DELETE FROM total_gpa
    """)
    cursor.execute("""
        INSERT INTO total_gpa (student_id, class, name, total_gpa)
        SELECT "学号", "班级", "姓名", SUM("绩点" * "学分") / SUM("学分") AS total_gpa
        FROM caltemp
        WHERE "成绩" != '通过' AND "成绩" != '无效' 
        AND "考试性质" NOT IN ('补考一', '重修补考')
        GROUP BY "学号", "班级", "姓名"
    """)
    conn.commit()

    # 关闭数据库连接
    conn.close()
    print("Data processing completed successfully.")




def print_table_schema(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    print(f"Column details for {table_name}:")
    for col in columns:
        print(col)




# 运行程序
if __name__ == "__main__":

	database_path = "students.db"
	conn = sqlite3.connect(database_path)
	print_table_schema(conn, 'finaltest')
	print_table_schema(conn, 'caltemp')
	conn.close()

	import_data_from_excel()
	process_data('students.db')
	# data processing

