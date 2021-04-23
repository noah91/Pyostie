import os
import shutil
import datetime


def process_files(file_list, output_path, folder_name):
    try:
        if os.path.isdir(folder_name):
            x = datetime.datetime.today().strftime('%d%m%Y_%H%M') + '_azure_json_processed_files'
            os.mkdir(output_path + x)
            for i in file_list:
                shutil.move(i, output_path + x)
            shutil.make_archive(output_path + x, 'zip', output_path, x)
            shutil.rmtree(output_path + x)
        elif not os.path.isdir(folder_name):
            os.mkdir(folder_name)
            x = datetime.datetime.today().strftime('%d%m%Y_%H%M') + '_azure_json_processed_files'
            os.mkdir(output_path + x)
            for i in file_list:
                shutil.move(i, output_path + x)
            shutil.make_archive(output_path + x, 'zip', output_path, x)
            shutil.rmtree(output_path + x)
        else:
            print("Please check and try again.")
    except Exception as ex:
        raise ex


def remove_files(filename_with_path):
    if os.path.isfile(filename_with_path):
        os.remove(filename_with_path)


def type_check(input_type):
    def decorator(function):
        def wrapper(args):
            if isinstance(args, input_type):
                return function(args)
            else:
                print("Bad input type.")
        return wrapper
    return decorator