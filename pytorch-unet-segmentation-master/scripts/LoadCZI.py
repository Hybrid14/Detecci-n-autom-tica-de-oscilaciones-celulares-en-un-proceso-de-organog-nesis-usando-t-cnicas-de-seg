from czifile import CziFile
from os.path import join
def load(path):
    with CziFile(join(path)) as czi:
        image_arrays = czi.asarray()
        meta = czi.metadata(raw=False)
        return(image_arrays)