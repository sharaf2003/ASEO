from pathlib import Path


class DocumentParser:
    """
    ASEO Document Parser Algorithm v1

    Responsible for:
    - Detecting document type
    - Extracting raw text
    - Preparing document content

    Supported:
    - TXT
    - PDF (will be enhanced)
    - DOCX (will be enhanced)
    """


    def __init__(self):

        self.supported_formats = [
            ".txt",
            ".pdf",
            ".docx"
        ]



    def parse(self, file_path: str):

        path = Path(file_path)


        if not path.exists():

            raise FileNotFoundError(
                f"File not found: {file_path}"
            )


        extension = path.suffix.lower()


        if extension not in self.supported_formats:

            raise ValueError(
                f"Unsupported format: {extension}"
            )


        if extension == ".txt":

            return self.parse_txt(
                path
            )


        elif extension == ".pdf":

            return self.parse_pdf(
                path
            )


        elif extension == ".docx":

            return self.parse_docx(
                path
            )



    # ===============================
    # TXT Parser
    # ===============================

    def parse_txt(self, path):

        text = path.read_text(
            encoding="utf-8"
        )


        return {

            "type": "txt",

            "text": text,

            "length": len(text)

        }



    # ===============================
    # PDF Parser
    # ===============================

    def parse_pdf(self, path):

        """
        Placeholder.

        Later:

        PyMuPDF
        pdfplumber

        """

        return {

            "type": "pdf",

            "text": "",

            "length": 0

        }



    # ===============================
    # DOCX Parser
    # ===============================

    def parse_docx(self, path):

        """
        Placeholder.

        Later:

        python-docx

        """

        return {

            "type": "docx",

            "text": "",

            "length": 0

        }