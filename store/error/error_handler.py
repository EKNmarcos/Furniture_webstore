class ObjectNotFoundException(Exception):
      
      def __init__(self, sprocname, err_number, err_description) -> None:
            super().__init__(f"{sprocname} - Error {err_number}: {err_description}")
            self.sprocname = sprocname
            self.err_number = err_number
            self.err_description = err_description
            


class EmptyRequestException(Exception):
      
      def __init__(self, sprocname, err_number, err_description) -> None:
            super().__init__(f"{sprocname} - {err_number}: {err_description}")
            self.sprocname = sprocname
            self.err_number = err_number
            self.err_description = err_description
