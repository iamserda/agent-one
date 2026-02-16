import os
from pathlib import Path


def get_files_info(working_directory, directory=".") -> str:
    try:
        if working_directory is None:
            return f'Error: "{working_directory}" is not a directory'

        result = "Result for current directory:"
        abs_work_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_work_dir, directory))
        is_valid_target = (
            os.path.commonpath(paths=[abs_work_dir, target_dir]) == abs_work_dir
        )

        if not is_valid_target:
            return (
                f"Result for '{directory}' directory:\n"
                + f'\tError: Cannot list "{directory}" as it is outside the permitted working directory'
            )
        if not os.path.isdir(target_dir):
            return result + f'\nError: "{directory}" is not a directory'

        result_components = []
        get_files(Path(target_dir), result_components)

        if result_components:
            for component in result_components:
                result += f"\n - {component}"
        return result
    except Exception as exeption:
        return f"Error: {exeption}"


def get_files(target_dir=Path("."), result_components: list = []):
    target_dir_path = Path(target_dir)
    for elem in Path.iterdir(target_dir_path):
        elem_stat = elem.stat()
        if elem.is_file():
            result_components.append(
                f"{elem.name}: file_size: {elem_stat.st_size}, is_dir={elem.is_dir()}"
            )
        elif elem.is_dir():
            result_components.append(
                f"{elem.name}: file_size: {elem_stat.st_size}, is_dir={elem.is_dir()}"
            )
            get_files(target_dir=elem, result_components=result_components)


if __name__ == "__main__":
    actual_result = get_files_info(working_directory="calculator", directory=".")
    print("\n", actual_result)

    actual_result = get_files_info(working_directory="calculator", directory="pkg/")
    print("\n", actual_result)

    actual_result = get_files_info(working_directory="calculator", directory="/bin")
    print(actual_result)

    actual_result = get_files_info(working_directory="calculator", directory="../")
    print(actual_result)
