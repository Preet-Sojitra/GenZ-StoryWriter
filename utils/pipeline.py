import utils.text_generator as text_generator


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
    # mistral_prompt = text_generator.prompt_generator(prompt)
    # ans = text_generator.call_model(mistral_prompt)

    # logger.log("Story generated")
    # print(ans)

    # return ans
