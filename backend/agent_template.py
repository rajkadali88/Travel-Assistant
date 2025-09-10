from llm import llm
class Agent:
    '''Base class for all AI agents in the system'''
    def __init__(self, name:str, description:str, system_prompt:str):
        self.name = name 
        self.description = description
        self.system_prompt = system_prompt 
        self.result = None 
        self.loading = False 
        self.error = None 
        
    def run(self, user_prompt:str):
        '''Run the agent with given prompt using specified model name and type'''
        self.loading = True 
        self.error =None 
        
        try:
            response = llm.invoke(self.system_prompt + "\n\n" + user_prompt)
            self.result = response 
            return self.result 
        except Exception as e:
            self.error = str(e) 
            return None 
        finally:
            self.loading =False 
            
    