import json
from llm_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

def process_posts(raw_data_path,preprocessed_path):
    with open(raw_data_path, encoding='utf-8') as file:
        posts= json.load(file)
        enriched_posts=[]
        for post in posts:
            metadata=extract_metadata(post['text'])
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)
        
    unified_tags = get_unified_tags(enriched_posts)
    for post in enriched_posts:
        current_tags = post['tags']
        new_tags = {unified_tags[tag] for tag in current_tags}
        post['tags'] = list(new_tags)

    with open(preprocessed_path, encoding='utf-8', mode="w") as outfile:
        json.dump(enriched_posts, outfile, indent=4)
        



def extract_metadata(post):
    template = """
    You are given a LinkedIn post. Your task is to extract structured metadata.
    Rules:
    1. Respond with **only a valid JSON object** (no extra text, no explanations).
    2. The JSON object must contain exactly these three keys:
    - "line_count": (integer) number of lines in the post
    - "language": (string) either "English" or "Hinglish"
    - "tags": (array of strings) maximum 2 short descriptive tags about the post
    3. Hinglish means a mix of Hindi and English.
    4. Do not invent content. Use only the given post.
    
    Post:
    {post}
    """
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"post": post})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")
    return res

def get_unified_tags(posts_with_metadata):
    unified_tags_set = set()
    for post in posts_with_metadata:
        unified_tags_set.update(post['tags'])
    unified_tags_list = ", ".join(sorted(unified_tags_set))

    template = '''I will give you a list of tags. You need to unify tags with the following requirements,
    1. Tags are unified and merged to create a shorter list. 
       Example 1: "Jobseekers", "Job Hunting" can be all merged into a single tag "Job Search". 
       Example 2: "Motivation", "Inspiration", "Drive" can be mapped to "Motivation"
       Example 3: "Personal Growth", "Personal Development", "Self Improvement" can be mapped to "Self Improvement"
       Example 4: "Scam Alert", "Job Scam" etc. can be mapped to "Scams"
    2. Each tag should be follow title case convention. example: "Motivation", "Job Search"
    3. Output should be a JSON object, No preamble
    3. Output should have mapping of original tag and the unified tag. 
       For example: {{"Jobseekers": "Job Search",  "Job Hunting": "Job Search", "Motivation": "Motivation}}
    
    Here is the list of tags: 
    {tags}
    '''

    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke({"tags": unified_tags_list})
    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse tags.")
    return res

if __name__ == '__main__':
    process_posts(r"data\raw_posts.json", r"data\preprocessed.json")
    print(f"Preprocessing Done")
