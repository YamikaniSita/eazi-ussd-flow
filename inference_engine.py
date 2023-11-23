# this is the inference engine for knowledge bases

import json

class InferenceEngine:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def start_inference_session(self):
        # prepare inference output
        with open(self.knowledge_base) as json_:
            kb = json.load(json_)
            sub_topics = kb['1']['topics'].keys()
            opt = ""
            for i in sub_topics:
                opt += i+". "+kb['1']['topics'][i]['title']+"\n"
            r = kb['1']['title']+"\n"+opt
        return (r, "1", "CON")

    def is_inference_input_valid(self, previous_state, input):
        with open(self.knowledge_base) as json_:
            kb = json.load(json_)
            split_state = previous_state.split('.')
            obj = kb
            for i in split_state: 
                obj = obj[i]['topics']
                if obj[input]['node_type'] == 'leaf':
                    return True
                elif obj[input]['node_type'] == 'decision':
                    # the follwowing if has an error I think points to wrong element must be fxed by removing the last el in state list if not 1
                    # if input in obj[input]['topics'].keys():
                    #     return True
                    # else: 
                    #     return True
                    return True
        return False

    def load_node(self, previous_state, key):
        with open(self.knowledge_base) as json_:
            kb = json.load(json_)
            # state looks like 1.1 with sub chapters in the kb
            split_state = previous_state.split('.')
            obj = kb
            for i in split_state: 
                obj = obj[i]['topics']
                if obj[key]['node_type'] == 'leaf':
                    # directly get advice
                    return (obj[key]['content'], previous_state, "END")
                elif obj[key]['node_type'] == 'decision':
                    sub_topics = obj[key]['topics'].keys()
                    opt = ""
                    for i in sub_topics:
                        opt += i+". "+obj[key]['topics'][i]['title']+"\n"
                    r = obj[key]['title']+"\n"+opt
                    new_state = previous_state+"."+key
                    # update state
                    return (r, new_state, "CON")
        return ('Error', 0, 'END')