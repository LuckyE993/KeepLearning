import os


def add_prefix_to_filenames(folder_path, prefix):
	# 检查文件夹是否存在
	if not os.path.exists(folder_path):
		print(f"文件夹 {folder_path} 不存在")
		return

	# 获取文件夹中的所有文件
	files = os.listdir(folder_path)

	# 遍历文件并添加前缀
	for file_name in files:
		old_file_path = os.path.join(folder_path, file_name)
		# 确保只处理文件，不处理子文件夹
		if os.path.isfile(old_file_path):
			new_file_name = prefix + file_name
			new_file_path = os.path.join(folder_path, new_file_name)
			os.rename(old_file_path, new_file_path)
			print(f"已将文件 {file_name} 重命名为 {new_file_name}")


# 使用示例
folder_path = r'C:\Users\LuckyE\Downloads\WSN'  # 将your_folder_path替换为目标文件夹路径
prefix = 'WSN实验报告-'  # 将your_prefix_替换为要添加的前缀
add_prefix_to_filenames(folder_path, prefix)
