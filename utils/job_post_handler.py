from langchain_community.document_loaders import WebBaseLoader

def get_job_posts(post_url:str)->str:
    job_post_text=WebBaseLoader(post_url).load()
    return job_post_text
    