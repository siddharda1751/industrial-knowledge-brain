from pathlib import Path

from unstructured.partition.auto import partition
from unstructured.partition.pdf import partition_pdf
from unstructured.partition.docx import partition_docx
from unstructured.partition.html import partition_html
from unstructured.partition.image import partition_image

from unstructured.chunking.title import chunk_by_title


class DocumentParser:
    def __init__(self,strategy="fast",max_characters=1000,new_after_n_chars=800,overlap=100,):
        self.strategy = strategy
        self.max_characters = max_characters
        self.new_after_n_chars = new_after_n_chars
        self.overlap = overlap

    def partition(self, file_path):
        suffix = Path(file_path).suffix.lower()
        if suffix == ".pdf":
            return partition_pdf(filename=file_path,strategy=self.strategy,)
        elif suffix == ".docx":
            return partition_docx(filename=file_path,)
        elif suffix in [".png", ".jpg", ".jpeg"]:
            return partition_image(filename=file_path,)
        elif suffix == ".html":
            return partition_html(filename=file_path,)
        else:
            return partition(filename=file_path,)
        
    def chunk(self, elements):
        return chunk_by_title(
            elements,
            max_characters=self.max_characters,
            new_after_n_chars=self.new_after_n_chars,
            overlap=self.overlap,
        )

    def clean(self, text):
        text = text.replace("\x00", "")
        text = " ".join(text.split())
        return text.strip()

    def parse(self,file_path,chunk=True,clean=True,return_elements=False,):
        elements = self.partition(file_path)
        if return_elements:
            return elements
        if chunk:
            elements = self.chunk(elements)
        results = []
        for element in elements:
            text = str(element)
            if clean:
                text = self.clean(text)
            if text:
                results.append(text)
        return results
