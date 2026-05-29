class Path:
    """
    >>> home_path = Path(" ./home ")
    >>> print(home_path)
    ./home
    >>> sub_path1 = Path("/subdir/file.txt")
    >>> print(sub_path1)
    subdir/file.txt
    >>> merged_path = home_path / sub_path1 # merged_path = home_path.__truediv__(sub_path1)
    >>> print(merged_path)
    ./home/subdir/file.txt
    >>> type(merged_path)
    <class '04_special_method_trudiv.Path'>
    >>> print(home_path / " /file.txt")
    ./home/file.txt
    >>> len(merged_path) # SAME AS: merged_path.__len__()
    4
    """

    def __init__(self, path):
        self.path = path.strip().strip("/")

    def __str__(self):
        return self.path

    def __truediv__(self, other):
        if isinstance(other, str):
            other = Path(other)
        return Path(self.path + "/" + other.path)

    def __len__(self):
        return len(self.path.split('/'))
