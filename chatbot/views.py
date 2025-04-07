from django.shortcuts import render
from .forms import ChatForm
from .models import Mistake, UserProfile

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

# Load Hugging Face grammar corrector model
tokenizer = AutoTokenizer.from_pretrained("prithivida/grammar_error_correcter_v1")
model = AutoModelForSeq2SeqLM.from_pretrained("prithivida/grammar_error_correcter_v1")

def correct_grammar_with_huggingface(text):
    input_text = "gec: " + text
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=128, truncation=True)
    outputs = model.generate(input_ids, max_length=128, num_beams=5, early_stopping=True)
    corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected_text

def chat_view(request):
    response = None
    corrected = None

    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            corrected = correct_grammar_with_huggingface(message)

            # Dummy user, for testing
            user, _ = UserProfile.objects.get_or_create(
                username="testuser",
                defaults={
                    "known_language": "English",
                    "target_language": "Spanish",
                    "level": "Beginner"
                }
            )

            # Save mistake if changed
            if corrected.strip() != message.strip():
                Mistake.objects.create(
                    user=user,
                    original_input=message,
                    corrected_input=corrected,
                    mistake_type="Grammar"
                )

            response = f"Bot: {corrected}"
    else:
        form = ChatForm()

    return render(request, "chat.html", {"form": form, "response": response})
