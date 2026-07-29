from pathlib import Path



class DocumentExtractor:
    """
    Responsible for extracting raw content
    from documents.
    """



    def extract_text(
        self,
        file_path:str
    ):


        path = Path(file_path)


        if not path.exists():

            raise FileNotFoundError(
                "Document not found"
            )


        extension = path.suffix.lower()


        if extension == ".txt":

            return path.read_text(
                encoding="utf-8"
            )


        elif extension == ".pdf":

            return self.extract_pdf(
                file_path
            )


        elif extension == ".docx":

            return self.extract_docx(
                file_path
            )


        else:

            raise Exception(
                "Unsupported file type"
            )



    def extract_pdf(
        self,
        file_path
    ):

        # سيتم استبداله لاحقاً بـ PyMuPDF

        return "PDF CONTENT"



    def extract_docx(
        self,
        file_path
    ):

        # سيتم استبداله لاحقاً بـ python-docx

        return "DOCX CONTENT"