# Eazi USSD Flow
USSD Flow is a Python module that allows you to write USSD application's flow as JSON files using a decision tree structure. This simplifies the development of USSD applications, especially knowledge providing systems that tend to become complex and hard to maintain as they grow.
# Features
Define USSD menus, prompts, inputs, and actions as JSON nodes. 
# Usage
To use USSD Flow, you need to create a JSON file that defines your USSD application logic. The JSON file should have a root node with the following format.
```json {
    "1": {
        "title": "Sankhani mbali yomwe mukufuna ulangizi", 
        "node_type": "decision",
        "topics": {
            "1": {
                "title": "Kusankha malo olima soya",  
                "node_type": "leaf",
                "content": "Soya amachita bwino mmalo ambiri omwe chimanga chimachitanso bwino. Pewani kubzala soya pa malo monga awa \n 1. Malo anchenga, soya amachita bwino pa nthaka yolemela. \n 2. Padambo \n 3. Pa malo pa mitengo yambiri pomwe pali nthunzi."
            }, 
            "2": {
                "title": "Kukonza malo olima soya",
                "node_type": "leaf", 
                "content": "Mutha kulima Soya pa malo a mizele kapena popanda mizele (flat). Pasakhalenso udzu"
            }, 
            "3": {
                "title": "Malangizo a mbewu",
                "node_type": "decision",
                "topics": {
                    "1": {
                        "title": "Kusankha mbewu zoyenela m'dera lanu",
                        "node_type": "decision",
                        "topics": {
                            "1": {
                                "title": "Langizo ili limatengelo Agro-Ecology la Boma lanu kuti lipeleke mbewu zoyanja m'dera lanu. ",
                                "node_type": "decision",
                                "topics": {
                                    "1": {
                                        "title": "Pitilizani",
                                        "node_type":"leaf",
                                        "content": "Feature in development"
                                    }
                                }
                            }
                        }
                    },
                    "2": {
                         "title": "Kapezedwe ka Mbewu",
                         "node_type": "leaf",
                         "content": "Mbewu yoyenela ikuyenela kugulidwa mmalo ololedwa ndi adindo, ngati ili yosunga isasungidwe kupitilila miyezi 12 (chaka chimodzi). Onesetsaninso kuti. \n 1.Isakhale yosweka. \n 2. Yophatikiza ndi ina uya mtundu wina. \n3. Yofinyika olo kunyonyoloka"
                    }, 
                    "4": {
                        "title": "Kugwilisa ntchito mankhwala a mbewu",
                        "node_type": "decision",
                        "topics": {
                            "1": {
                                "title": "Koyamba kulima Soya pa Dzaka zitatu zapita",
                                "node_type": "leaf",
                                "content": "Gwilisani ntchito mankhwala a Rhibotis kuti muonjezele Nitrogen pa munda wanu. Mankhwala wa amapangidwa ku Chitedze ku Lilongwe kapena Bvumbwe ku Thyolo. \n Satilani malangizo alembedwe pa packet, onesesani kuti mbewu yo mwaizala pasanathe maola 24."
                                }, 
                            "2": {
                                "title": "Sikoyamba kulima soya",
                                "node_type": "leaf",
                                "content": "Mutha osagwilisa ntchito mankhwala wa poti soya amatha kupanga mankhwala wa payekha akabzalidwa."
                            }   
                        } 
                    }
                }
            }
          }
        }
      
```
Saving the file as .json file and will be used as the knowledge base of your app.
```
import inference_engine
engine = inference_engine.InferenceEngine(knowledge_base='json_file_with_flow.json')
out = engine.start_inference_session()
```
To instatiate the module. Follow the cli.py example for guide.
