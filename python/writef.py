def writef(file_name,extention,content):
    with open(f"{file_name}.{extention}",'w',encoding='utf-8') as f:
        f.write(str(content))
        f.close()