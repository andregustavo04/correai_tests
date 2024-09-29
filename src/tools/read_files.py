from crewai_tools import FileReadTool, DirectoryReadTool

# Read Database Schema
read_database_schema_dir = DirectoryReadTool(directory=r'CorreAI\support_docs\database_schema')

# Read Base Training Plans
read_base_training_plans_dir = DirectoryReadTool(directory=r'CorreAI\support_docs\base_training_plans')

# Reading Best Practices on Creating Training Plans
read_best_practices_on_creating_training_plans_dir = DirectoryReadTool(directory=r'CorreAI\support_docs\best_practices_creating_training_plans') 

