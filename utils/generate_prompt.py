def generate_prompt(captions):
    # captions = ["moon", "ocean", "alien"]
    prompt = "Write a movie script involving:"
    for s in captions:
        prompt = prompt + s + ","
    prompt = (
        prompt[:-1]
        + ". Also, add a title to your movie at the beginning. For example: 'The Moon and the Ocean'"
    )
    print(prompt)

    return prompt
