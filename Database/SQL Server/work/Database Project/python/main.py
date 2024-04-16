import dataprocess
import sys
import os

if __name__ == "__main__":
	processor = dataprocess.StudentDataProcessor("students.db")
	processor.create_tables()
	processor.import_data_from_excel("./dataset/机器人21级.xlsx", "finaltest")
	processor.import_data_from_excel("./dataset/机器人21级补考.xlsx", "resit")
	processor.process_data()