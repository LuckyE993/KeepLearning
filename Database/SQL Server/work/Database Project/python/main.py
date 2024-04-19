from pywebio import start_server
import dataprocess
import web_package

if __name__ == '__main__':

	processor = dataprocess.StudentDataProcessor("students.db")
	processor.create_tables()

	processor.import_data_from_excel("./dataset/机器人21级.xlsx", "finaltest")
	processor.import_data_from_excel("./dataset/机器人21级补考.xlsx", "resit")

	processor.import_data_from_excel("./dataset/物联网.xlsx", "finaltest")
	processor.import_data_from_excel("./dataset/物联网补考.xlsx", "resit")

	processor.import_data_from_excel("./dataset/人工智能21级.xlsx", "finaltest")
	processor.import_data_from_excel("./dataset/人工智能21级补考.xlsx", "resit")

	processor.import_data_from_excel("./dataset/数据21级.xlsx", "finaltest")
	processor.import_data_from_excel("./dataset/数据21级补考.xlsx", "resit")

	processor.process_data()

	processor.add_user('admin', 'admin', 'admin')
	processor.add_user('teacher', 'teacher', 'teacher')
	processor.add_user('student', 'student', 'student')

	app = web_package.StudentManagementSystem()
	start_server(app.main, port=8080)
