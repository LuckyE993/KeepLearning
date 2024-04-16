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
        conn.commit()
        conn.close()

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
        df = pd.read_excel(file_path)
        conn = self.get_db_connection()
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()

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

    def run(self):
        while True:
            print("\nAvailable Commands:")
            print("1. Add Student/Score")
            print("2. Update Student/Score")
            print("3. Delete Student/Score")
            print("4. Find Student Info")
            print("5. Get Scores")
            print("6. Show GPA")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.handle_add()
            elif choice == '2':
                self.handle_update()
            elif choice == '3':
                self.handle_delete()
            elif choice == '4':
                self.handle_find()
            elif choice == '5':
                self.handle_get_scores()
            elif choice == '6':
                self.handle_show_gpa()
            elif choice == '0':
                print("Exiting program.")
                sys.exit(0)
            else:
                print("Invalid choice. Please choose a valid option.")

    def handle_add(self):
        table = input("Enter table name (finaltest or resit): ")
        data = {}
        while True:
            key = input("Enter field name (blank to finish): ")
            if not key:
                break
            value = input(f"Enter value for {key}: ")
            data[key] = value
        self.add_student_or_score(table, data)

    def handle_update(self):
        table = input("Enter table name (finaltest or resit): ")
        data = {}
        conditions = {}
        print("Enter data to update:")
        while True:
            key = input("Enter field name (blank to finish): ")
            if not key:
                break
            value = input(f"Enter value for {key}: ")
            data[key] = value
        print("Enter conditions (e.g., to identify which records to update):")
        while True:
            key = input("Enter condition field name (blank to finish): ")
            if not key:
                break
            value = input(f"Enter value for {key} (condition value): ")
            conditions[key] = value
        self.update_student_or_score(table, data, conditions)

    def handle_delete(self):
        table = input("Enter table name (finaltest or resit): ")
        conditions = {}
        print("Enter conditions to specify which records to delete:")
        while True:
            key = input("Enter condition field name (blank to finish): ")
            if not key:
                break
            value = input(f"Enter value for {key} (condition value): ")
            conditions[key] = value
        self.delete_student_or_score(table, conditions)

    def handle_find(self):
        kwargs = {}
        print("Enter search criteria:")
        while True:
            key = input("Enter field name (e.g., 学号 or 姓名, blank to finish): ")
            if not key:
                break
            value = input(f"Enter value for {key}: ")
            kwargs[key] = value
        result = self.find_student_info(**kwargs)
        print("Search Results:")
        for item in result:
            print(item)

    def handle_get_scores(self):
        student_id = input("Enter student ID: ")
        scores = self.get_scores(student_id)
        print("Scores:", scores)

    def handle_show_gpa(self):
        student_id = input("Enter student ID: ")
        gpa = self.show_gpa(student_id)
        print("GPA:", gpa)

    def add_student_or_score(self, table, data):
        conn = self.get_db_connection()
        keys = ', '.join(data.keys())
        values = tuple(data.values())
        placeholders = ', '.join('?' for _ in data)
        conn.execute(f'INSERT INTO {table} ({keys}) VALUES ({placeholders})', values)
        conn.commit()
        conn.close()
        self.process_data()

    def update_student_or_score(self, table, data, conditions):
        conn = self.get_db_connection()
        updates = ', '.join(f'{k} = ?' for k in data.keys())
        values = tuple(data.values()) + tuple(conditions.values())
        condition_str = ' AND '.join(f'{k} = ?' for k in conditions.keys())
        conn.execute(f'UPDATE {table} SET {updates} WHERE {condition_str}', values)
        conn.commit()
        conn.close()
        self.process_data()

    def delete_student_or_score(self, table, conditions):
        conn = self.get_db_connection()
        condition_str = ' AND '.join(f'{k} = ?' for k in conditions.keys())
        conn.execute(f'DELETE FROM {table} WHERE {condition_str}', tuple(conditions.values()))
        conn.commit()
        conn.close()
        self.process_data()

    def find_student_info(self, **kwargs):
        conn = self.get_db_connection()
        condition_str = ' AND '.join(f'{k} = ?' for k in kwargs.keys())
        cursor = conn.execute(f'SELECT * FROM finaltest WHERE {condition_str}', tuple(kwargs.values()))
        result = cursor.fetchall()
        conn.close()
        return [dict(row) for row in result]

    def get_scores(self, student_id):
        conn = self.get_db_connection()
        cursor = conn.execute('SELECT * FROM finaltest WHERE 学号 = ?', (student_id,))
        normal_scores = cursor.fetchall()
        cursor = conn.execute('SELECT * FROM resit WHERE 学号 = ?', (student_id,))
        resit_scores = cursor.fetchall()
        conn.close()
        return {'normal_scores': [dict(row) for row in normal_scores],
                'resit_scores': [dict(row) for row in resit_scores]}

    def show_gpa(self, student_id):
        conn = self.get_db_connection()
        cursor = conn.execute('SELECT 总绩点 FROM total_gpa WHERE 学号 = ?', (student_id,))
        result = cursor.fetchone()
        conn.close()
        return result['总绩点'] if result else 'Not available'

# Running the interactive processor
if __name__ == "__main__":
    database_path = 'students.db'
    processor = StudentDataProcessor(database_path)
    processor.create_tables()
    processor.run()



# ### 使用示例
#
# if __name__ == "__main__":
#
#
#     processor = StudentDataProcessor("students.db")
#     processor.create_tables()
#     processor.import_data_from_excel("./dataset/机器人21级.xlsx", "finaltest")
#     processor.import_data_from_excel("./dataset/机器人21级补考.xlsx", "resit")
#     processor.process_data()
