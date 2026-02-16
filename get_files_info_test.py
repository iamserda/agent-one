from functions.get_files_info import get_files_info


if __name__ == "__main__":
    dir = "."
    actual_result = get_files_info(working_directory="calculator", directory=dir)
    print("\n", actual_result)

    dir = "pkg"
    actual_result = get_files_info(working_directory="calculator", directory=dir)
    print("\n", actual_result)

    dir = "/bin"
    expected_result = f"Result for '{dir}' directory:\n\tError: Cannot list \"{dir}\" as it is outside the permitted working directory"
    actual_result = get_files_info(working_directory="calculator", directory="/bin")
    print(actual_result)

    dir = "../"
    expected_result = f"Result for '{dir}' directory:\n\tError: Cannot list \"{dir}\" as it is outside the permitted working directory"
    actual_result = get_files_info(working_directory="calculator", directory="../")
    print(actual_result)
