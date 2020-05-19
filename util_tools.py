import os
import ntpath


def get_basename_from_path(path, include_ext = True):
    if include_ext:
        return ntpath.basename(path)
    else:
        return os.path.splitext(ntpath.basename(path))[0]
    
    
def read(filePath):
#     with open(filePath, 'r', 'utf-16') as textFile:  # can throw FileNotFoundError
    with open(filePath) as textFile:  # can throw FileNotFoundError
        out =  list(l.rstrip() for l in textFile.readlines())
    textFile.close()
    return out


# fread = open('input.csv', 'rb').read()
# mytext = fread.decode('utf-16')



if __name__ == '__main__':
    import production_utils as prdu
    prdu.main()
