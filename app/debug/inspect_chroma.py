from pathlib import Path
import chromadb

CHROMA_DB_PATH = "data/chroma_db"
COLLECTION_NAME = "industrial_knowledge"

OUTPUT_FILE = Path("debug/outputs/chroma_dump.txt")


client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
collection = client.get_collection(COLLECTION_NAME)

results = collection.get()

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

    f.write("=" * 80 + "\n")
    f.write("CHROMADB COLLECTION DUMP\n")
    f.write("=" * 80 + "\n\n")

    ids = results["ids"]
    docs = results["documents"]
    metas = results["metadatas"]

    for i in range(len(ids)):

        f.write(f"Chunk #{i+1}\n")
        f.write("-" * 80 + "\n")

        f.write(f"Chunk ID : {ids[i]}\n")
        f.write(f"Metadata : {metas[i]}\n\n")

        f.write("Text\n")
        f.write(docs[i])
        f.write("\n\n")
        f.write("=" * 80 + "\n\n")

print(f"Wrote {len(ids)} chunks to {OUTPUT_FILE}")