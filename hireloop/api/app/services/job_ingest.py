"""Job ingestion — fetches public JD URLs and extracts a clean job record.

Strict policy: only fetches URLs the OWNER provides; no scraping, no crawling,
no automated discovery. ToS-clean for personal use.
"""

from __future__ import annotations

from typing import Any

import httpx
from bs4 import BeautifulSoup
from readability import Document
from tenacity import retry, stop_after_attempt, wait_exponential_jitter

from app.core.logging import get_logger

log = get_logger(__name__)

USER_AGENT = "Mozilla/5.0 (compatible; hireloop-personal/0.1; +https://github.com/vallakatlaraviteja)"
TIMEOUT = httpx.Timeout(15.0, connect=5.0)


@retry(stop=stop_after_attempt(3), wait=wait_exponential_jitter(initial=0.5, max=4))
async def fetch_jd(url: str) -> dict[str, Any]:
    """Fetch a public JD URL. Returns clean extracted text + heuristics."""
    log.info("jd.fetch", url=url)
    async with httpx.AsyncClient(
        headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT, follow_redirects=True
    ) as client:
        resp = await client.get(url)
        resp.raise_for_status()
        html = resp.text

    doc = Document(html)
    title = doc.short_title()
    main_html = doc.summary(html_partial=True)
    text = BeautifulSoup(main_html, "lxml").get_text("\n", strip=True)
    soup = BeautifulSoup(html, "lxml")

    og_site = (soup.find("meta", property="og:site_name") or {}).get("content")  # type: ignore[union-attr]
    og_title = (soup.find("meta", property="og:title") or {}).get("content")  # type: ignore[union-attr]

    return {
        "title": (og_title or title or "").strip()[:300],
        "company_hint": (og_site or "").strip()[:200],
        "description_md": text,
        "raw_html": html[:200_000],
    }
