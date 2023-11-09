from ctransformers import AutoModelForCausalLM, AutoConfig, Config


class MistralModel:
    def __init__(
        self,
        model_name="mistral-7b-instruct-v0.1.Q4_K_M.gguf",
        temperature=0.8,
        repetition_penalty=1.1,
        batch_size=52,
        max_new_tokens=512,
        context_length=2048,
    ):
        self.model = self.load_model(
            model_name,
            temperature,
            repetition_penalty,
            batch_size,
            max_new_tokens,
            context_length,
        )

    def load_model(
        self,
        model_name,
        temperature,
        repetition_penalty,
        batch_size,
        max_new_tokens,
        context_length,
    ):
        conf = AutoConfig(
            Config(
                temperature=temperature,
                repetition_penalty=repetition_penalty,
                batch_size=batch_size,
                max_new_tokens=max_new_tokens,
                context_length=context_length,
            )
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_name, model_type="mistral", config=conf
        )

        print("Mistra model loaded")

        return model

    def prompt_generator(self, prompt):
        mistral_prompt = f"<s>[INST] {prompt} [/INST]"
        return mistral_prompt

    def call_model(
        self,
        mistral_prompt,
        temperature=0.7,
        repetition_penalty=1.15,
        max_new_tokens=512,
    ):
        script = self.model(
            mistral_prompt,
            temperature=temperature,
            repetition_penalty=repetition_penalty,
            max_new_tokens=max_new_tokens,
        )

        print(script)
        return script
