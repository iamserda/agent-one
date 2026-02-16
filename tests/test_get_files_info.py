from functions.get_files_info import get_files_info


class TestGetFilesInfo:
    def test_known_valid_path1(self):
        expected_answer = """Result for current directory:
 - __init__.py: file_size: 0, is_dir=False
 - tests.py: file_size: 1354, is_dir=False
 - main.py: file_size: 741, is_dir=False
 - pkg: file_size: 128, is_dir=True
 - render.py: file_size: 404, is_dir=False
 - calculator.py: file_size: 1754, is_dir=False"""
        working_dir = "calculator"
        dir = "."
        actual_answer = get_files_info(working_directory=working_dir, directory=dir)
        assert actual_answer == expected_answer

    def test_known_valid_path2(self):
        expected_answer = """Result for current directory:
 - render.py: file_size: 404, is_dir=False
 - calculator.py: file_size: 1754, is_dir=False"""
        working_dir = "calculator"
        dir = "pkg"
        actual_answer = get_files_info(working_directory=working_dir, directory=dir)
        assert actual_answer == expected_answer

    def test_known_invalid_path_raises_error(self):
        dir = "/bin"
        working_dir = "calculator"
        expected_answer = f"Result for '{dir}' directory:\n\tError: Cannot list \"{dir}\" as it is outside the permitted working directory"
        actual_answer = get_files_info(working_directory=working_dir, directory=dir)
        assert actual_answer == expected_answer

    def test_known_valid_path_raises_error(self):
        dir = "../"
        working_dir = "calculator"
        expected_answer = f"Result for '{dir}' directory:\n\tError: Cannot list \"{dir}\" as it is outside the permitted working directory"
        actual_answer = get_files_info(working_directory=working_dir, directory=dir)
        assert actual_answer == expected_answer
