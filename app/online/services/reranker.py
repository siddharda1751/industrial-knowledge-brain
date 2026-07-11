from app.online.models import (
    RankedChunk,
    RetrievalResult,
    RetrievalSource,
)


class Reranker:

    def rerank(
        self,
        retrieval: RetrievalResult
    ) -> list[RankedChunk]:

        merged: dict[str, RankedChunk] = {}

        # ----------------------------
        # Vector Results
        # ----------------------------
        for chunk in retrieval.vector_results:

            merged[chunk.chunk_id] = RankedChunk(
                chunk=chunk,
                final_score=chunk.score,
                retrieval_sources=[
                    RetrievalSource.VECTOR
                ]
            )

        # ----------------------------
        # BM25 Results
        # ----------------------------
        for chunk in retrieval.bm25_results:

            if chunk.chunk_id in merged:

                ranked_chunk = merged[
                    chunk.chunk_id
                ]

                ranked_chunk.final_score += chunk.score

                if RetrievalSource.BM25 not in ranked_chunk.retrieval_sources:

                    ranked_chunk.retrieval_sources.append(
                        RetrievalSource.BM25
                    )

            else:

                merged[chunk.chunk_id] = RankedChunk(
                    chunk=chunk,
                    final_score=chunk.score,
                    retrieval_sources=[
                        RetrievalSource.BM25
                    ]
                )

        # ----------------------------
        # Graph Boost
        # ----------------------------
        for chunk_id in retrieval.graph_result.chunk_ids:

            if chunk_id in merged:

                merged[
                    chunk_id
                ].final_score += 0.5

                if RetrievalSource.GRAPH not in merged[
                    chunk_id
                ].retrieval_sources:

                    merged[
                        chunk_id
                    ].retrieval_sources.append(
                        RetrievalSource.GRAPH
                    )

        ranked_chunks = list(
            merged.values()
        )

        ranked_chunks.sort(
            key=lambda chunk: chunk.final_score,
            reverse=True
        )

        return ranked_chunks