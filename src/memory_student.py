from __future__ import annotations

from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # Zep builds the Context Block from the user graph relative to what the
        # current thread is talking about, so the thread must carry the query.
        prime_eval_thread(self.client, user_id, thread_id, query)

        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        context_block = getattr(user_context, "context", "") or ""

        # Edges are facts with validity ranges. The Context Block summarises;
        # this keeps the raw dated facts (deadlines, open loops, superseded
        # preferences) that recency cases need.
        try:
            facts = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=20,
            )
            fact_text = render_graph_search(facts)
        except Exception:
            fact_text = ""

        return join_nonempty([context_block, fact_text], sep="\n\n")

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # User-scoped: episodic memory is "what this user and I did before".
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=15,
        )
        # Cap each episode: a few long session transcripts would otherwise eat
        # the whole 3% episodic budget and push out the short reflections that
        # carry the outcome markers.
        return render_graph_search(results, episode_char_cap=180)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # Domain knowledge lives in the standalone graph, not under any user.
        capped = cap_query(query)
        try:
            # "episodes" returns the raw document text, which preserves literal
            # markers like PAYMENT-RULE-3. "auto" returns extracted facts and
            # drops them.
            results = self.client.graph.search(
                graph_id=graph_id,
                query=capped,
                scope="episodes",
                limit=8,
            )
        except Exception:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=capped,
                scope="nodes",
                limit=8,
            )
        # No char cap here: semantic documents put their markers at the end.
        return render_graph_search(results)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # 10/4/3/3 budget, priority short_term -> long_term -> episodic -> semantic.
        return self.budget.assemble(layers)
