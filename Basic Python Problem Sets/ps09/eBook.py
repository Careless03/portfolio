class eBook:
    def __init__(self, title: str, file_size: float) -> None:
        self.title = title
        self.file_size = file_size

    def __eq__(self, other: object) -> bool:
        """
        Overrides the equality comparison (==) between two eBook instances.
        Compares title and file_size attributes to determine equality.
        """
        if type(other) != eBook:
            raise ValueError(f'Cannot compare types {type(self)} with \
            {type(other)}')

        return self.title == other.title and self.file_size == other.file_size

    def __hash__(self) -> int:
        """
        Overrides the hash value computation for eBook instances.
        Necessary for using instances in hashed collections like sets or 
        dictionaries.
        """
        return hash((self.title, self.file_size))
    
    def __str__(self) -> str:
        """
        Overrides the string representation when str() is called on an eBook 
        instance.
        Returns a human-readable string including the title and file size.
        """
        return f'{self.title} - {self.file_size}'
    
    def __repr__(self) -> str:
        """
        Overrides the string representation when repr() is called on an eBook 
        instance.
        Calls __str__() to provide a representation of the eBook.
        """
        return self.__str__()
