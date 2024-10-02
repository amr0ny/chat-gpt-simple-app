import openai
from openai._exceptions import OpenAIError
from settings import settings
import logging

logging.basicConfig(level=logging.INFO)


def retrieve_answer(client: openai, msg: str, model: str = 'gpt-4o-mini', temperature: float = 0.7) -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    'role': 'user',
                    'content': [
                        {
                            'type': 'text',
                            'text': msg
                        }
                    ],
                }
            ],
            temperature=temperature
        )
        return response['choices'][0]['message']['content']
    except OpenAIError as e:
        logging.error(f"Ошибка при обращении к OpenAI API: {e}")
        return "Произошла ошибка при запросе к API. Попробуйте снова."


if __name__ == '__main__':
    openai.api_key = settings.API_KEY
    while True:
        user_input = input('Введите ваш запрос к ChatGPT (или "exit" для завершения):\n')

        if user_input.lower() in ['exit', 'quit']:
            break

        answer = retrieve_answer(openai, user_input)

        print("\nОтвет ChatGPT:")
        print(answer)
        print("-" * 50)
