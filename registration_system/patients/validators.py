from django.core.exceptions import ValidationError
from validate_docbr import CPF

def validate_cpf(value):
    # Remove tudo que não for número

    cpf = CPF()  # ✅ instancia correta

    if not cpf.validate(value):  # ✅ chamada correta
        raise ValidationError('CPF inválido.')
