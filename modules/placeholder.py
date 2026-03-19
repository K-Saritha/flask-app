import requests
from flask import Flask,request,render_template
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
logger=logging.getLogger(__name__)


def get_all_todos(id):
    try:
        todos=[]
        if id is not None:
            result= requests.get(f'https://jsonplaceholder.typicode.com/todos/{id}')
        else:
            result= requests.get('https://jsonplaceholder.typicode.com/todos')
        if result.status_code == 200:
            todos = result.json()
            logger.info(f'Successfully fetched todos: {todos}')
        return todos
    except Exception as e:
        print('Error fetching todos:', e)
        logger.error(f'Error fetching todos: {e}')
        return []