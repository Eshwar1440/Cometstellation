"""Temporary file for smoke test, will add more and replace as the build progresses."""

import os

import pytest
from neo4j import GraphDatabase


def test_python_version() -> None:
    import sys

    assert sys.version_info >= (3, 12)


@pytest.mark.skipif("NEO4J_URI" not in os.environ, reason="no Neo4j available")
def test_neo4j_reachable() -> None:
    driver = GraphDatabase.driver(
        os.environ["NEO4J_URI"],
        auth=(os.environ.get("NEO4J_USER", "neo4j"), os.environ["NEO4J_PASSWORD"]),
    )
    with driver.session() as session:
        assert session.run("RETURN 1 AS ok").single()["ok"] == 1
    driver.close()
