import os
import shutil

def flatten_directory():
    # 获取程序所在目录
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # 遍历当前目录下的所有子目录
    for root, dirs, files in os.walk(current_directory):
        # 排除当前目录
        if root != current_directory:
            # 移动子目录中的所有文件到当前目录
            for file in files:
                source_path = os.path.join(root, file)
                target_path = os.path.join(current_directory, file)

                # 如果目标文件已存在，则重命名文件
                counter = 1
                while os.path.exists(target_path):
                    filename, file_extension = os.path.splitext(file)
                    new_filename = f"{filename}_{counter}{file_extension}"
                    target_path = os.path.join(current_directory, new_filename)
                    counter += 1

                # 移动文件
                shutil.move(source_path, target_path)
                print(f"Moved: {file} from {root} to {current_directory}")

if __name__ == "__main__":
    flatten_directory()
