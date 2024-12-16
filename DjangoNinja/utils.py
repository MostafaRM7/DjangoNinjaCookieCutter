from ninja.files import UploadedFile


def file_format_validator(file: UploadedFile, format_tuple: tuple):
    print(file.content_type)
    return file.content_type in format_tuple
