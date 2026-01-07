from django.db import models
from django.contrib.auth.models import User


class HipHopSurvey(models.Model):
    """
    Model for Hip-Hop Culture Research Survey
    Pesquisa Cultura Hip-Hop Nacional
    """
    
    # Role choices - Tipo de atuação na cultura Hip-Hop
    ROLE_CHOICES = [
        ('MC', 'MC/Rapper/Cantor'),
        ('DJ', 'DJ'),
        ('GRAFITE', 'Grafite'),
        ('BREAKING', 'Breaking'),
        ('GRUPO', 'Grupo'),
        ('CONHECIMENTO', 'Conhecimento'),
        ('FAS', 'Fãs'),
        ('CONSUMIDOR', 'Consumidores de produtos do Hip-Hop'),
    ]
    
    # Race/Color choices
    RACE_CHOICES = [
        ('PRETA', 'Preta'),
        ('PARDA', 'Parda'),
        ('BRANCA', 'Branca'),
        ('INDIGENA', 'Indígena'),
        ('AMARELA', 'Amarela'),
    ]
    
    # Gender choices
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('NB', 'Não-binário'),
        ('O', 'Outro'),
    ]
    
    # Personal Information
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Usuário')
    nome = models.CharField(max_length=200, verbose_name='Nome')
    pseudonimo = models.CharField(max_length=200, blank=True, verbose_name='Pseudônimo/Nome Artístico')
    
    # Location
    estado = models.CharField(max_length=100, verbose_name='Estado')
    municipio = models.CharField(max_length=100, verbose_name='Município')
    
    # Age and demographics
    idade = models.PositiveIntegerField(verbose_name='Idade')
    cor = models.CharField(max_length=20, choices=RACE_CHOICES, verbose_name='Cor/Raça')
    genero = models.CharField(max_length=2, choices=GENDER_CHOICES, verbose_name='Gênero')
    
    # Hip-Hop involvement
    tempo_hiphop = models.CharField(
        max_length=100, 
        verbose_name='Quanto tempo na cultura Hip-Hop',
        help_text='Ex: 5 anos, 10 anos, desde 2010'
    )
    
    # Role in Hip-Hop culture (can have multiple roles)
    atuacao = models.CharField(
        max_length=20, 
        choices=ROLE_CHOICES, 
        verbose_name='Atuação na Cultura Hip-Hop'
    )
    
    # For groups
    nome_grupo = models.CharField(
        max_length=200, 
        blank=True, 
        verbose_name='Nome do Grupo',
        help_text='Se faz parte de um grupo'
    )
    membros_masculinos = models.PositiveIntegerField(
        default=0, 
        verbose_name='Número de membros masculinos',
        blank=True
    )
    membros_femininos = models.PositiveIntegerField(
        default=0, 
        verbose_name='Número de membros femininos',
        blank=True
    )
    
    # Education
    formado = models.BooleanField(default=False, verbose_name='É formado?')
    qual_formacao = models.CharField(
        max_length=200, 
        blank=True, 
        verbose_name='Qual formação?',
        help_text='Se sim, qual curso/área'
    )
    
    # Additional information
    observacoes = models.TextField(blank=True, verbose_name='Observações adicionais')
    
    # Metadata
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
    class Meta:
        verbose_name = 'Pesquisa Hip-Hop'
        verbose_name_plural = 'Pesquisas Hip-Hop'
        ordering = ['-criado_em']
    
    def __str__(self):
        return f"{self.nome} ({self.pseudonimo if self.pseudonimo else self.atuacao}) - {self.municipio}/{self.estado}"

