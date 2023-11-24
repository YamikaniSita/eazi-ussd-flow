import inference_engine

"""
    inference_engine requires to track previous state stored as chapters 1.2.3 etc
    storage of user id, session ids is not stored by inference_engine, you pass it on load_node and check_input
    and a current state to be passed on next load_node or check_input are returned by load_node
    
    persistent storage example for implementation, the session_id will hold each users state get that when
    passing to load node, and check_node input

    _____________________
    |session_id | state |
    ---------------------
    |1          | 1.2   |
    ---------------------
    load_node return list = (output, new_state, continue_flag)
    the continue_flag holds CON for decision nodes, END for leaf nodes
    In production USSD platforms, Telecom USSDC requires this value appended for all USSD responses. As "END Error"
"""

engine = inference_engine.InferenceEngine(knowledge_base='soya.json')
out = engine.start_inference_session()
prompt = out[0]
state = out[1]
continue_flag = out[2]

while(continue_flag == 'CON'):
    print(prompt)
    input_ = input()
    is_valid = engine.is_inference_input_valid(previous_state = state, input = input_)
    if is_valid: 
        out = engine.load_node(state, input_)
        prompt = out[0]
        state = out[1]
        continue_flag = out[2]

print(prompt)
