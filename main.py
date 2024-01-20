import os
import warnings
from typing import Dict

from openfabric_pysdk.utility import SchemaUtil

from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import Ray, State
from openfabric_pysdk.loader import ConfigClass

from llm import generate_answer, construct_chain


############################################################
# Callback function called on update config
############################################################
def config(configuration: Dict[str, ConfigClass], state: State):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: Ray, state: State) -> SimpleText:

    # Retrieving the chain.
    # The chain is only constructed once to not load the llm with each request
    try:
        chain = state.chain
    except:
        chain = construct_chain()
        state.chain = chain

    output = []
    for text in request.text:
        # generate answer
        response = generate_answer(chain, text)
        output.append(response)

    return SchemaUtil.create(SimpleText(), dict(text=output))
