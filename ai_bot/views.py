# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("AIzaSyAsCl5-BHlEcBwyPgLIKiMRWiG3jpPK_vM"))

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="try to keep the conversation going and ask the user to have the users attention",
)

@csrf_exempt
def chat_with_ai(request):
    if request.method == "POST":
        user_message = request.POST.get("message", "")
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        "You are Martian, a friendly assistant AI bot created by a highly advanced Martian society from the year 2100. ..."
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        "Greetings, Earthlings! I am Martian, a friendly AI assistant sent from the year 2100 by a society deeply concerned for the fate of our shared planet. ..."
                    ],
                },
                {
                    "role": "user",
                    "parts": [
                        "you are a personal assistant to an individual",
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        "Okay, I'm ready to be your personal assistant! Tell me a little bit about yourself. ..."
                    ],
                },
            ]
        )
        response = chat_session.send_message(user_message)
        return JsonResponse({"response": response.text})

    return JsonResponse({"error": "Invalid request"}, status=400)
