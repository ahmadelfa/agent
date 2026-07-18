import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        file_info = []
        contents = os.listdir(target_dir)
        for file in contents:
            info = [file]
            target_file = os.path.normpath(os.path.join(target_dir, file))
            info.append(str(os.path.getsize(target_file)))
            info.append(str(os.path.isdir(target_file)))
            file_info.append(info)
        output_strings = []
        for file in file_info:
            output_strings.append(f"- {file[0]}: file_size={file[1]} bytes, is_dir={file[2]}")
        return "\n".join(output_strings)
            
    except Exception as e:
        return f"Error: {e}"