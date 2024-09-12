# generator/views.py
import random
import string
from django.shortcuts import render

def generate_password(request):
    if request.method == 'POST':
        length = int(request.POST.get('length', 12))  # Default length is 12
        include_letters = 'letters' in request.POST
        include_digits = 'digits' in request.POST
        include_special = 'special' in request.POST

        character_list = ""

        if include_letters:
            character_list += string.ascii_letters
        if include_digits:
            character_list += string.digits
        if include_special:
            character_list += string.punctuation

        if not character_list:  # No character set selected
            return render(request, 'generator/index.html', {'error': 'Please select at least one character set!'})

        password = ''.join(random.choice(character_list) for _ in range(length))
        
        return render(request, 'generator/index.html', {'password': password})

    return render(request, 'generator/index.html')

