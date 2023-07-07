from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.FloatField(default=0)

    def __str__(self):
        return self.categoria
    
class Conta(models.Model):
    # O primeiro parâmetro da tupla é oq vai aparecer no DB
    # O numero do max_length é da quantidade de strings que vai ser armazenado no DB, neste caso, é são 2 NU or CE
    banco_choices = (
        ('NU', 'NUBANK'),
        ('CE', 'Caixa Econômica'),
    )

    tipo_choices = (
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    )

    apelido = models.CharField(max_length=50)
    banco = models.CharField( max_length=2, choices=banco_choices)

    tipo = models.CharField(max_length=2, choices=tipo_choices)
    valor = models.FloatField()
    icone = models.ImageField(upload_to="icones")

    def __str__(self):
        return self.apelido