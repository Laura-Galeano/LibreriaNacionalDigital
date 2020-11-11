from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from multiselectfield import MultiSelectField

class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,apellidos,password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        
        usuario = self.model(
            username=username, 
            email =self.normalize_email(email), 
            nombres = nombres, 
            apellidos = apellidos
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
        
    def create_superuser(self,username,email,nombres,apellidos,password):
        usuario = self.create_user(
            email,
            username=username,  
            nombres = nombres, 
            apellidos = apellidos,
            password=password
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser):
    
    ciudad_elecciones=[
            ('Armenia','Armenia'),('Barranquilla','Barranquilla'),('Bello','Bello'),
            ('Bogotá','Bogotá'),('Bucaramanga','Bucaramanga'),('Cali','Cali'),('Cartagena','Cartagena'),
            ('Cúcuta','Cúcuta'),('Ibagué','Ibagué'),('Manizales','Manizales'),
            ('Medellín','Medellín'),('Montería','Montería'),('Neiva','Neiva'),
            ('Cartagena','Cartagena'),('Pasto','Pasto'),('Pereira','Pereira'),
            ('Santa Marta','Santa Marta'),('Soacha','Soacha'),
            ('Soledad','Soledad'),('Valledupar','Valledupar'),('Villavicencio','Villavicencio')

        ]
    es_choices= [
            ('Femenino','Femenino'),
            ('Masculino','Masculino'),
            ('Otro','Otro')
        ]
    temas_elecciones=[
            ('Historia y Geografía', 'Historia y Geografía'),('Narrativa', 'Narrativa'),('Juvenil', 'Juvenil'),('Ciencias físicas', 'Ciencias físicas'),
            ('Infantil', 'Infantil'),('Ciencias Sociales y política', 'Ciencias Sociales y política'),('Medicina y salud', 'Medicina y salud'),
            ('Filosofía', 'Filosofía'),('Arquitectura', 'Arquitectura'),('Arte', 'Arte'), ('Gastronomía', 'Gastronomía'),('Varios', 'Varios'),
        ]
    id = models.AutoField(primary_key=True)
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    nombres = models.CharField('Nombres',max_length=200,blank=False, null=False)
    email = models.EmailField('Correo Electrónico', max_length=254, unique = True)
    apellidos = models.CharField('Apellidos',max_length=200,blank=False, null=False)
    usuario_activo = models.BooleanField(default=True)
    Cedula = models.CharField('Cédula',max_length= 200, blank=True, null=True)
    Fecha_nacimiento = models.DateField('Fecha de nacimiento', blank=False, null=False)
    genero = models.IntegerField('Género',choices=es_choices,max_length= 200,blank=False, null=False, default='1')
    Ciudad = models.IntegerField('Ciudad de residencia',choices=ciudad_elecciones,max_length= 200,blank=False, null=False, default='1')
    suscripcion = models.BooleanField('Suscribirme a noticias',blank=True, null=True, default=False)
    temas_preferidos = MultiSelectField('Temas de preferencia',choices=temas_elecciones,blank=True, null=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = UsuarioManager()
   
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    def __str__(self):
        return f'{self.nombres}, {self.apellidos}'

    def has_perm(self,perm,ob=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador

