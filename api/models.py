from django.db import models
import uuid
import os
from enum import unique
from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_image_file_extension
from localflavor.br.models import BRCPFField
from .managers import diarista_manager
from django.contrib.auth.models import UserManager
from administracao.models import Servico

# Create your models here.

def nome_arquivo_foto(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('usuarios', filename)

def nome_arquivo_documento(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('documentos', filename)

# Create your models here.
class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = (
        (1, "Cliente"),
        (2, "Diarista")
    )
    username = None
    nome_completo = models.CharField(max_length=255, null=True, blank=False)
    cpf = BRCPFField(null=True, unique=True)
    nascimento = models.DateField(null=True, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    telefone = models.CharField(max_length=11, null=True, blank=False)
    tipo_usuario = models.IntegerField(choices=TIPO_USUARIO_CHOICES, null=True, blank=False)
    reputacao = models.FloatField(null=True, blank=False, default=5)
    chave_pix = models.CharField(null=True, blank=True, max_length=255)
    foto_documento = models.ImageField(null=True, upload_to=nome_arquivo_foto, validators=[validate_image_file_extension, ])
    foto_usuario = models.ImageField(null=True, upload_to=nome_arquivo_documento, validators=[validate_image_file_extension, ])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('nome_completo', 'cpf', 'telefone', 'tipo_usuario', 'reputacao', 'chave_pix', 'foto_documento', 'foto_usuario')

    objects = UserManager()

    diarista_objects = diarista_manager.DiaristaManager()

class Diaria(models.Model):
    STATUS_DIARIA_CHOICES = (
        (1, "SEM_PAGAMENTO"),
        (2, "PAGO"),
        (3, "CONFIRMADO"),
        (4, "CONCLUIDO"),
        (5, "CANCELADO"),
        (6, "AVALIADO"),
        (7, "TRANSFERIDO")
    )
    data_atendimento = models.DateField(null=False, blank=False)
    tempo_atendimento = models.IntegerField(null=False, blank=False)
    status = models.IntegerField(null=False, blank=False, choices=STATUS_DIARIA_CHOICES, default=1)
    preco = models.FloatField(null=False, blank=False)
    valor_comissao = models.FloatField(null=False, blank=False)
    logradouro = models.CharField(max_length=60, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    bairro = models.CharField(max_length=30, null=False, blank=False)
    complemento = models.CharField(max_length=100, null=False, blank=False)
    cep = models.CharField(max_length=10, null=False, blank=False)
    cidade = models.CharField(max_length=30, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    codigo_ibge = models.IntegerField(null=True, blank=True)
    quantidade_quartos = models.IntegerField(null=True, blank=True)
    quantidade_salas = models.IntegerField(null=True, blank=True)
    quantidade_cozinhas = models.IntegerField(null=True, blank=True)
    quantidade_banheiros = models.IntegerField(null=True, blank=True)
    quantidade_quintais = models.IntegerField(null=True, blank=True)
    quantidade_outros = models.IntegerField(null=True, blank=True)
    observacoes = models.TextField(null=False, blank=False)
    motivo_cancelamento = models.TextField(null=False, blank=False)
    cliente = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.DO_NOTHING,
        related_name='cliente')
    diarista = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.DO_NOTHING,
        related_name='diarista')
    servico = models.ForeignKey(Servico, null=False, blank=False, on_delete=models.DO_NOTHING)
    candidatos = models.ManyToManyField(Usuario, blank=True, related_name='candidatos')
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

class CidadesAtendimento(models.Model):
    codigo_ibge = models.IntegerField(null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    usuario = models.ManyToManyField(Usuario, related_name='cidades_atendidas')