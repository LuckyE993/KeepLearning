import sqlite3
import pandas as pd
import sys


class StudentDataProcessor:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_db_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def create_tables(self):
        tables_sql = {
            "finaltest": """
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
            """,
            "resit": """
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
            """,
            "caltemp": """
                CREATE TABLE IF NOT EXISTS "caltemp" (
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
            """,
            "total_gpa": """
                CREATE TABLE IF NOT EXISTS "total_gpa" (
                    "学号" TEXT PRIMARY KEY,
                    "班级" TEXT,
                    "姓名" TEXT,
                    "总绩点" REAL
                );
            """
        }
        conn = self.get_db_connection()

        cursor = conn.cursor()
        for table_sql in tables_sql.values():
            cursor.execute(table_sql)
        self.create_ifaward_table()
        self.create_users_table()
        conn.commit()

        conn.close()

        print("Tables created successfully.")

    def drop_tables(self):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE finaltest")
        cursor.execute("DROP TABLE resit")
        cursor.execute("DROP TABLE caltemp")
        cursor.execute("DROP TABLE total_gpa")
        cursor.execute("DROP TABLE ifaward")
        cursor.execute("DROP TABLE users")
        conn.commit()
        conn.close()

    def create_users_table(self):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL CHECK (role IN ('student', 'teacher', 'admin'))
                    );
                """)
        conn.commit()
        conn.close()

    def add_user(self, username, password, role):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
        conn.commit()
        conn.close()
        print("Add User: User name = ", username, "password = ", password, " role = ", role)

    def get_user(self, username):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        return dict(user) if user else None

    def create_ifaward_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS "ifaward" (
            "学号" INTEGER PRIMARY KEY,
            "班级" TEXT,
            "姓名" TEXT,
            "是否可评奖" TEXT,
            "原因" TEXT DEFAULT NULL  
        );
        """
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()

    def import_data_from_excel(self, file_path, table_name):
        try:
            df = pd.read_excel(file_path)
            conn = self.get_db_connection()
            df.to_sql(table_name, conn, if_exists='append', index=False)
            conn.close()
            print(f"Data imported successfully into {table_name} from {file_path}")
        except Exception as e:
            print(f"Failed to import data from {file_path} to {table_name}: {e}")

    def process_data(self):
        conn = self.get_db_connection()
        cursor = conn.cursor()

        # 复制finaltest表到caltemp表
        cursor.execute("DELETE FROM caltemp")  # 清空caltemp表
        cursor.execute("""
                INSERT INTO caltemp ("班级", "姓名", "课程名称", "成绩", "学分", "学号", "绩点", "专业", "考试性质", "年级")
                SELECT "班级", "姓名", "课程名称", "成绩", "学分", "学号", "绩点", "专业", "考试性质", "年级" FROM finaltest
            """)
        conn.commit()

        # 更新不及格的成绩
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
            ) AND caltemp."成绩" < '60'
        """)
        conn.commit()

        cursor.execute("DELETE FROM total_gpa")
        conn.commit()
        # 计算总绩点
        cursor.execute("""
                    INSERT INTO total_gpa ("学号", "班级", "姓名", "总绩点")
                    SELECT "学号", "班级", "姓名", ROUND(SUM("绩点" * "学分") / SUM("学分"), 2)
                    FROM caltemp
                    WHERE "成绩" NOT IN ('通过', '无效') AND "考试性质" NOT IN ('补考一', '重修补考')
                    GROUP BY "学号", "班级", "姓名"
                """)
        conn.commit()

        # #删除暂存表
        # cursor.execute("DROP TABLE caltemp")

        cursor.execute("""
                    DELETE FROM ifaward
                """)
        cursor.execute("""
                    INSERT INTO ifaward ("学号", "班级", "姓名", "是否可评奖", "原因")
                    SELECT "学号", "班级", "姓名", 
                           CASE 
                               WHEN MIN("成绩") < '60' THEN '否'
                               WHEN ROUND(SUM("绩点" * "学分") / SUM("学分"), 2) < 5.95 THEN '否'
                               ELSE '是'
                           END,
                           CASE
                               WHEN MIN("成绩") < '60' AND ROUND(SUM("绩点" * "学分") / SUM("学分"), 2) < 5.95 THEN '一考挂科且绩点未过5.95'
                               WHEN MIN("成绩") < '60' THEN '一考挂科'
                               WHEN ROUND(SUM("绩点" * "学分") / SUM("学分"), 2) < 5.95 THEN '绩点未过5.95'
                               ELSE NULL
                           END
                    FROM caltemp
                    GROUP BY "学号", "班级", "姓名"
                """)
        conn.commit()
        conn.close()

        print("Data processing completed successfully.")


if __name__ == "__main__":
    processor = StudentDataProcessor("Unittest.db")

    # processor.create_tables()
    #
    # processor.import_data_from_excel("./dataset/机器人21级.xlsx", "finaltest")
    # processor.import_data_from_excel("./dataset/机器人21级补考.xlsx", "resit")
    #
    #
    # processor.add_user('admin', 'admin', 'admin')
    # processor.add_user('teacher', 'teacher', 'teacher')
    # processor.add_user('student', 'student', 'student')
    # user_info = processor.get_user('admin')
    # print(user_info)
    # user_info = processor.get_user('teacher')
    # print(user_info)
    # user_info = processor.get_user('student')
    # print(user_info)
    #
    # processor.process_data()
    processor.drop_tables()
    #
    # processor.add_user('john_doe', 'securepassword123', 'teacher')


