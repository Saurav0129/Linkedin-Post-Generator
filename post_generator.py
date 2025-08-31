from llm_helper import llm
from Few_shots import FewShotPosts

# Initialize the FewShotPosts class to access data
few_shot = FewShotPosts()


def get_length_str(length):
    """
    Translates a length category into a line count range.
    """
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"


def generate_post(length, language, tag, influencer, engagement_level):
    """
    Generates a LinkedIn post using the LLM with a tailored prompt.
    
    Args:
        length (str): The desired length of the post ("Short", "Medium", "Long").
        language (str): The language of the post ("English", "Hinglish").
        tag (str): The primary topic/tag of the post.
        influencer (str): The name of the influencer style to mimic ("Any" or a specific name).
        engagement_level (str): The engagement level to prioritize ("High", "Medium", "Low").
    """
    prompt = get_prompt(length, language, tag, influencer, engagement_level)
    response = llm.invoke(prompt)
    return response.content


def get_prompt(length, language, tag, influencer, engagement_level):
    """
    Constructs a detailed prompt for the LLM, including examples.
    """
    length_str = get_length_str(length)

    # Base prompt with user-selected parameters
    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    If Language is Hinglish then it means it is a mix of Hindi and English.
    The script for the generated post should always be English.
    '''

    # Get a base set of examples filtered by length, language, and tag.
    examples = few_shot.get_filtered_posts(length, language, tag)
    
    # Filter examples further based on influencer style.
    if influencer != "Any":
        examples = [post for post in examples if post['influencer'] == influencer]

    # Filter examples by engagement level.
    if engagement_level == "High":
        examples = [post for post in examples if post['engagement'] > 500]
    elif engagement_level == "Medium":
        examples = [post for post in examples if post['engagement'] > 200 and post['engagement'] <= 500]
    elif engagement_level == "Low":
        examples = [post for post in examples if post['engagement'] <= 200]
        
    # Add examples to the prompt if they exist after all filtering.
    if len(examples) > 0:
        prompt += "\n\n4) Use the writing style as per the following examples."

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        if i == 1:  # Use a maximum of two samples
            break

    return prompt


if __name__ == "__main__":
    print(generate_post("Medium", "English", "Mental Health", "Any", "High"))
