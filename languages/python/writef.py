def writef(file_name,extension,content):
    with open(f"{file_name}.{extension}",'w',encoding='utf-8') as f:
        f.write(str(content))
        f.close()