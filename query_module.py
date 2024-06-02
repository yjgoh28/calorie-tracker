from llama_index.core import SQLDatabase
from llama_index.llms.openai import OpenAI
from database import engine
from llama_index.core.query_engine import NLSQLTableQueryEngine
from llama_index.core.retrievers import NLSQLRetriever
from llama_index.core.query_engine import RetrieverQueryEngine

def setup_query_engine():
    """
    Set up the query engine with the specified configurations.
    """
    llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo")
    sql_database = SQLDatabase(engine, include_tables=["nutritioninfo"])
    nl_sql_retriever = NLSQLRetriever(
        sql_database, tables=["nutritioninfo"], return_raw=True
    )
    query_engine = RetrieverQueryEngine.from_args(nl_sql_retriever)
    
    return query_engine

def query_database(query):
    """
    Query the database using the provided query string.
    """
    query_engine = setup_query_engine()
    response = query_engine.query(query)
    return str(response)