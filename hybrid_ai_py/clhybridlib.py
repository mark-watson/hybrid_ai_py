##### Semantic Web and Linked Data #####

import rdflib
from SPARQLWrapper import SPARQLWrapper
from pprint import pprint

def query(sparql_query, endpoint):
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(sparql_query)
    sparql.setReturnFormat('json')
    r = sparql.query().convert()
    vars = r['head']['vars']
    results = r['results']['bindings']
    rr = [vars]
    for r1 in results:
        rr.append([r1[v]['value'] for v in vars])
    return rr

def query_dbpedia(sparql_query):
    return query(sparql_query, 'http://dbpedia.org/sparql')

##### OpenAI GPT-3 APIs #####

import os
import openai

# Load API key from an environment variable
openai.api_key = os.getenv("OPENAI_KEY")

def generate_text(prompt, temperature=0.7, top_p=0.9, max_tokens=50):
  response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=temperature,
    top_p=top_p,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"])
  return response

def QA(text, max_tokens=50):
  prompt = "\n\nQ: " + text + " A:\n\n"
  print(f"prompt = {prompt}")
  response = openai.Completion.create(
    engine="text-davinci-001",
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=0,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n", "<|endoftext|>"])
  return response # .choices # [0]['text']
