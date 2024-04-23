"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()
    bot.browse("https://portaldatransparencia.gov.br/download-de-dados/auxilio-brasil")

    # Implement here your logic...
    ...
    if not bot.find( "ano", matching=0.97, waiting_time=10000):
        not_found("ano")
    bot.click()
    if not bot.find( "2022", matching=0.97, waiting_time=10000):
        not_found("2022")
    bot.click()
     
    if not bot.find( "baixar", matching=0.97, waiting_time=10000):
        not_found("baixar")
    bot.click() 
     
            
    if not bot.find( "mes", matching=0.97, waiting_time=10000):
        not_found("mes")
    bot.click()
          
    if not bot.find( "fevereiro", matching=0.97, waiting_time=10000):
        not_found("fevereiro")
    bot.click()
    
    if not bot.find( "baixar2", matching=0.97, waiting_time=10000):
        not_found("baixar2")
    bot.click()
    
    
    if not bot.find( "fev", matching=0.97, waiting_time=10000):
        not_found("fev")
    bot.click()
    if not bot.find( "mar", matching=0.97, waiting_time=10000):
        not_found("mar")
    bot.click()
    
    if not bot.find( "baixar2", matching=0.97, waiting_time=10000):
        not_found("baixar2")
    bot.click()
    
    
    if not bot.find( "mar2", matching=0.97, waiting_time=10000):
        not_found("mar2")
    bot.click()
    if not bot.find( "abr", matching=0.97, waiting_time=10000):
        not_found("abr")
    bot.click()
    
    if not bot.find( "baixar", matching=0.97, waiting_time=10000):
        not_found("baixar")
    bot.click() 
     
    
    if not bot.find( "abr2", matching=0.97, waiting_time=10000):
        not_found("abr2")
    bot.click()
    
    
    if not bot.find( "mai", matching=0.97, waiting_time=10000):
        not_found("mai")
    bot.click()
    
    if not bot.find( "baixar", matching=0.97, waiting_time=10000):
        not_found("baixar")
    bot.click() 
    
          
    if not bot.find( "mai2", matching=0.97, waiting_time=10000):
        not_found("mai2")
    bot.click()
    if not bot.find( "jun", matching=0.97, waiting_time=10000):
        not_found("jun")
    bot.click()
    
    if not bot.find( "baixar", matching=0.97, waiting_time=10000):
        not_found("baixar")
    bot.click() 
    
    if not bot.find( "jun2", matching=0.97, waiting_time=10000):
        not_found("jun2")
    bot.click()
    if not bot.find( "jul", matching=0.97, waiting_time=10000):
        not_found("jul")
    bot.click()
    if not bot.find( "baixar", matching=0.97, waiting_time=10000):
        not_found("baixar")
    bot.click() 
    
    if not bot.find( "jul2", matching=0.97, waiting_time=10000):
        not_found("jul2")
    bot.click()
    if not bot.find( "agos", matching=0.97, waiting_time=10000):
        not_found("agos")
    bot.click()
    
    if not bot.find( "baixar", matching=0.97, waiting_time=10000):
        not_found("baixar")
    bot.click() 
    
    if not bot.find( "agos2", matching=0.97, waiting_time=10000):
        not_found("agos2")
    bot.click()
    if not bot.find( "set2", matching=0.97, waiting_time=10000):
        not_found("set2")
    bot.click()
    if not bot.find( "baixar", matching=0.97, waiting_time=10000):
        not_found("baixar")
    bot.click() 
    if not bot.find( "out", matching=0.97, waiting_time=10000):
        not_found("out")
    bot.click()
    if not bot.find( "out2", matching=0.97, waiting_time=10000):
        not_found("out2")
    bot.click()
    
    if not bot.find( "baixar", matching=0.97, waiting_time=10000):
        not_found("baixar")
    bot.click()
     
    if not bot.find( "nov3", matching=0.97, waiting_time=10000):
        not_found("nov3")
    bot.click()
        
    
    if not bot.find( "nov", matching=0.97, waiting_time=10000):
        not_found("nov")
    bot.click()
    if not bot.find( "baixar", matching=0.97, waiting_time=10000):
        not_found("baixar")
    bot.click() 
    if not bot.find( "nov2", matching=0.97, waiting_time=10000):
        not_found("nov2")
    bot.click()
    if not bot.find( "dez", matching=0.97, waiting_time=10000):
        not_found("dez")
    bot.click()
    
    if not bot.find( "baixar", matching=0.97, waiting_time=10000):
        not_found("baixar")
    bot.click() 
    
    bot.wait(30000)
    
    
    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
