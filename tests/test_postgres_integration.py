from __future__ import annotations

import time

import psycopg


def _wait_for_db(dsn: str, timeout_s: int = 30) -> None:
    deadline = time.time() + timeout_s
    last_err: Exception | None = None

    while time.time() < deadline:
        try:
            with psycopg.connect(dsn) as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT 1;")
                    cur.fetchone()
            return
        except Exception as e:  # noqa: BLE001 (fine in test wait loop)
            last_err = e
            time.sleep(1)

    raise AssertionError(f"DB did not become ready within {timeout_s}s. Last error: {last_err}")


def test_postgres_is_reachable() -> None:
    dsn = "host=localhost port=5432 dbname=playground user=playground password=playground"
    _wait_for_db(dsn, timeout_s=45)
