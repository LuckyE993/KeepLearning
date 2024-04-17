import sqlite3
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import local


class StudentManagementSystem:
	def __init__(self):
		self.db_path = 'students.db'

	def get_db_connection(self):
		conn = sqlite3.connect(self.db_path)
		conn.row_factory = sqlite3.Row
		return conn

	def login(self):
		while True:
			user_info = input_group("登录", [
				input('用户名', name='username'),
				input('密码', type=PASSWORD, name='password')
			])
			conn = self.get_db_connection()
			cursor = conn.cursor()
			cursor.execute("SELECT * FROM users WHERE username = ?", (user_info['username'],))
			user = cursor.fetchone()
			conn.close()

			if user and user['password'] == user_info['password']:
				local.user = user['username']
				local.role = user['role']
				return user['role']
			else:
				toast('用户名或密码错误，请重新输入！', color='error')

	def register(self):
		while True:
			user_info = input_group("注册", [
				input('用户名', name='username'),
				input('密码', type=PASSWORD, name='password'),
				input('确认密码', type=PASSWORD, name='confirm_password')
			])

			if user_info['password'] != user_info['confirm_password']:
				toast('两次输入的密码不一致，请重新输入！', color='error')
				continue

			conn = self.get_db_connection()
			cursor = conn.cursor()
			try:
				cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, 'student')",
				               (user_info['username'], user_info['password']))
				conn.commit()
				toast('注册成功！', color='success')
				break
			except sqlite3.IntegrityError:
				toast('用户名已存在，请重新选择用户名！', color='error')
			finally:
				conn.close()

	def student_page(self):
		student_id = int(local.user)  # 将用户名作为查询的学号
		results = self.query_student_info(student_id)
		for key, value in results.items():
			if value:
				put_text(f"{key}的数据：")
				put_table([dict(row) for row in value])
			else:
				put_text(f"{key}中未查询到相关成绩")

	def teacher_page(self):
		""" 教师的主页面添加修改学生成绩的选项 """
		put_buttons(['查询班级信息', '修改学生成绩'],
		            onclick=[lambda: self.query_class_info(), lambda: self.modify_student_scores()])

	def admin_page(self):
		tab = radio("选择操作：", options=['执行SQL', '创建用户'])
		if tab == '执行SQL':
			self.admin_sql_query()
		elif tab == '创建用户':
			self.admin_create_user()

	def query_student_info(self, student_id):
		conn = self.get_db_connection()
		cursor = conn.cursor()
		results = {}
		cursor.execute("SELECT * FROM finaltest WHERE 学号 = ?", (student_id,))
		results['finaltest'] = cursor.fetchall()
		cursor.execute("SELECT * FROM resit WHERE 学号 = ?", (student_id,))
		results['resit'] = cursor.fetchall()
		cursor.execute("SELECT * FROM total_gpa WHERE 学号 = ?", (student_id,))
		results['total_gpa'] = cursor.fetchall()
		cursor.execute("SELECT * FROM ifaward WHERE 学号 = ?", (student_id,))
		results['ifaward'] = cursor.fetchall()
		cursor.close()
		return results

	def query_class_info(self):
		class_id = input("请输入班级号：")
		conn = self.get_db_connection()
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM finaltest WHERE 班级 = ?", (class_id,))
		results = cursor.fetchall()
		cursor.close()
		put_table([dict(row) for row in results])

	def admin_sql_query(self):
		sql = textarea("请输入SQL语句：", rows=6, code={'mode': 'sql', 'theme': 'shadowfox'})
		conn = self.get_db_connection()
		cursor = conn.cursor()
		try:
			results = cursor.execute(sql).fetchall()
			conn.commit()
			put_table(results)
		except Exception as e:
			put_text('SQL错误: ', str(e))
		finally:
			conn.close()

	def admin_create_user(self):
		user_info = input_group("创建新用户", [
			input("请输入用户名：", name="username"),
			input("请输入密码：", type=PASSWORD, name="password"),
			select("请选择用户角色：", options=['student', 'teacher', 'admin'], name="role")
		])
		conn = self.get_db_connection()
		cursor = conn.cursor()
		try:
			cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
			               (user_info['username'], user_info['password'], user_info['role']))
			conn.commit()
			toast('用户创建成功！', color='success')
		except sqlite3.IntegrityError:
			toast('用户名已存在，请重新输入！', color='error')
		finally:
			conn.close()

	def modify_student_scores(self):
		""" 查询学生成绩并允许教师进行修改 """
		student_id = input("请输入学生学号：", type=NUMBER)
		conn = self.get_db_connection()
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM finaltest WHERE 学号 = ?", (student_id,))
		finaltest_scores = cursor.fetchall()
		cursor.execute("SELECT * FROM resit WHERE 学号 = ?", (student_id,))
		resit_scores = cursor.fetchall()
		conn.close()

		if not finaltest_scores and not resit_scores:
			put_text("未找到该学生的成绩信息。")
			return

		finaltest_scores = [dict(score) for score in finaltest_scores]
		resit_scores = [dict(score) for score in resit_scores]

		# 显示成绩信息并允许编辑
		for score in finaltest_scores:
			score['成绩'] = input(f"{score['课程名称']} - 最终考试成绩", type='text', value=score['成绩'])
		for score in resit_scores:
			score['成绩'] = input(f"{score['课程名称']} - 补考成绩", type='text', value=score['成绩'])

		if actions("确认修改", ['保存修改', '取消']) == '保存修改':
			self.save_modified_scores(student_id, finaltest_scores, resit_scores)

	def save_modified_scores(self, student_id, finaltest_scores, resit_scores):
		""" 保存修改后的成绩到数据库 """
		conn = self.get_db_connection()
		cursor = conn.cursor()
		try:
			for score in finaltest_scores:
				cursor.execute("UPDATE finaltest SET 成绩 = ? WHERE 学号 = ? AND 课程名称 = ?",
				               (score['成绩'], student_id, score['课程名称']))
			for score in resit_scores:
				cursor.execute("UPDATE resit SET 成绩 = ? WHERE 学号 = ? AND 课程名称 = ?",
				               (score['成绩'], student_id, score['课程名称']))
			conn.commit()
			toast('成绩更新成功！', color='success')
		except Exception as e:
			toast('成绩更新失败：' + str(e), color='error')
		finally:
			conn.close()

	def main(self):
		while True:
			option = radio("请选择登录或注册", options=['登录', '注册'])
			if option == '登录':
				role = self.login()
				if role:
					break
			else:
				self.register()

		if local.role == 'student':
			print(111)
			self.student_page()
		elif local.role == 'teacher':
			self.teacher_page()
		elif local.role == 'admin':
			self.admin_page()


if __name__ == '__main__':
	app = StudentManagementSystem()
	start_server(app.main, port=8080)
