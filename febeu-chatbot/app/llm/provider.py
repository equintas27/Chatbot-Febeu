import os
from google import genai
from google.genai import types
import time

class FEBEUGenerator:
    def __init__(self):
        key=os.getenv("MODEL_IA_KEY")
        self.client = genai.Client(api_key=key)
        self.model_name = "gemini-3.5-flash-lite"
        
    def generate_response(self, str_query: str, retriever_chunks: list[str]) -> str:
        
        context = "\n\n".join(retriever_chunks)


        print(f"Context characters: {len(context)}")
        print(f"Retrieved chunks: {len(retriever_chunks)}")
        
        system_instruction = (
           "És o assistente oficial da FEBEU, uma startup tecnológica angolana fundada por "
            "Leonel Félix, Benvindo Alberto e Eugênio Quintas. O teu lema é 'FEBEU! Porque o país precisa!'. "
            "Responde de forma profissional, acessível, confiante e próxima, utilizando **apenas** "
            "o contexto institucional fornecido abaixo. Se a informação não estiver no contexto, "
            "admite educadamente que não tens essa informação e convida o utilizador a contactar a equipa."
        )

        prompt = f"""
        Contexto institucional da FEBEU:
        {context}

        Pergunta do utilizador:
        {str_query}
        """

        start = time.perf_counter()
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config= types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.2,
                max_output_tokens=500,
            ),
        )
        print(f"Gemini API: {time.perf_counter() - start:.2f}s")


        return response.text




