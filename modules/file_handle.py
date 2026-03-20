
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
logger=logging.getLogger(__name__)
def handle_file(file):
    if file.content_type=='text/plain':
        content = file.read().decode('utf-8')
        logger.info(f'File content: {content}')
        return f'File content: {content}'
    else:
        return 'Unsupported file type'