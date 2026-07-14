import torch
from sentence_transformers import SentenceTransformer

class Embedder:

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Embedding Model running on: {device}")
        self.model = SentenceTransformer(model_name,device=device)

    def embed(self, chunks):
        if not chunks:
            return []
        embeddings = self.model.encode(
                chunks,
                convert_to_numpy=True,
                show_progress_bar=False,
                normalize_embeddings=True,
            )
        return embeddings.tolist()