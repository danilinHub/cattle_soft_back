from django.test import TestCase
from .models import Usuario

class UsuarioTest(TestCase):

    def setUp(self):
        # Configura los datos de prueba
        self.usuario = Usuario.objects.create(
            nombre='Juan Pérez',
            rol='Admin',
            email='juan.perez@example.com',
            contrasena='contraseña123'
        )

    def test_usuario_creation(self):
        """Prueba que un usuario se crea correctamente"""
        self.assertEqual(self.usuario.nombre, 'Juan Pérez')
        self.assertEqual(self.usuario.rol, 'Admin')
        self.assertEqual(self.usuario.email, 'juan.perez@example.com')

    def test_usuario_email_unique(self):
        """Prueba que el email sea único"""
        with self.assertRaises(Exception):  # Debería generar una excepción si se repite el email
            Usuario.objects.create(
                nombre='Maria González',
                rol='User',
                email='juan.perez@example.com',  # Mismo email que el usuario anterior
                contrasena='contraseña456'
            )

class GanadoTest(TestCase):

    def setUp(self):
        # Creamos un usuario primero para asignarlo al ganado
        self.usuario = Usuario.objects.create(
            nombre='Carlos Gómez',
            rol='Admin',
            email='carlos.gomez@example.com',
            contrasena='password123'
        )

        # Creamos un objeto de ganado
        self.ganado = Ganado.objects.create(
            tipo='Vaca',
            raza='Holstein',
            peso=500.0,
            fecha_nacimiento='2023-01-01',
            estado_salud='Bueno',
            finca=self.usuario  # Relación con el usuario
        )

    def test_ganado_creation(self):
        """Prueba que el ganado se crea correctamente"""
        self.assertEqual(self.ganado.tipo, 'Vaca')
        self.assertEqual(self.ganado.raza, 'Holstein')
        self.assertEqual(self.ganado.peso, 500.0)
        self.assertEqual(self.ganado.estado_salud, 'Bueno')
        self.assertEqual(self.ganado.finca, self.usuario)

    def test_ganado_relacion_usuario(self):
        """Prueba que el ganado está correctamente relacionado con el usuario"""
        ganado = Ganado.objects.get(id_ganado=self.ganado.id_ganado)
        self.assertEqual(ganado.finca.nombre, 'Carlos Gómez')

class AlimentacionTest(TestCase):

    def setUp(self):
        # Creamos un usuario primero para asignarlo al ganado
        self.usuario = Usuario.objects.create(
            nombre='Ana López',
            rol='Admin',
            email='ana.lopez@example.com',
            contrasena='password123'
        )

        # Creamos un objeto de ganado
        self.ganado = Ganado.objects.create(
            tipo='Vaca',
            raza='Jersey',
            peso=450.0,
            fecha_nacimiento='2023-02-02',
            estado_salud='Excelente',
            finca=self.usuario  # Relación con el usuario
        )

        # Creamos un objeto de alimentación
        self.alimentacion = Alimentacion.objects.create(
            ganado=self.ganado,  # Relación con el ganado
            tipo_alimento='Pastura',
            cantidad_diaria=15.5,
            frecuencia=3,
            fecha_inicio='2024-01-01',
            fecha_fin=None
        )

    def test_alimentacion_creation(self):
        """Prueba que la alimentación se crea correctamente"""
        self.assertEqual(self.alimentacion.tipo_alimento, 'Pastura')
        self.assertEqual(self.alimentacion.cantidad_diaria, 15.5)
        self.assertEqual(self.alimentacion.frecuencia, 3)
        self.assertEqual(self.alimentacion.fecha_inicio, '2024-01-01')
        self.assertIsNone(self.alimentacion.fecha_fin)

    def test_alimentacion_relacion_ganado(self):
        """Prueba que la alimentación está correctamente relacionada con el ganado"""
        alimentacion = Alimentacion.objects.get(id_alimentacion=self.alimentacion.id_alimentacion)
        self.assertEqual(alimentacion.ganado.tipo, 'Vaca')
        self.assertEqual(alimentacion.ganado.raza, 'Jersey')

