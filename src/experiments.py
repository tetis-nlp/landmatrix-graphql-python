import configparser
import ast
import subprocess

credential_file = "credentials.ini"
credential_config = configparser.ConfigParser()
credential_config.read(credential_file)

ISDM_API_KEY = credential_config['ISDM']["ISDM_API_KEY"]
ISDM_JWT = credential_config['ISDM']["ISDM_JWT"]
list_of_models = ast.literal_eval(credential_config['ISDM']["MODEL_LIST"])

list_of_expe = ["agent_graphql", "rag_graphql", "in_context_learning_graphql"]

for expe in list_of_expe:
    print(expe)
    for model in list_of_models:
        print(model)
        try:
            # Start the script with the given model in a new process
            process = subprocess.Popen(['python', f'src/{expe}.py', '--api_key', ISDM_API_KEY, '--api_jwt',  ISDM_JWT, '--model', model])
        except Exception as e:
            print(f"Failed to start script with model {model}: {e}")