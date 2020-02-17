from django.test import TestCase
from .models import Articulo, LONGITUD_MAXIMA
from django import forms
from django.core.exceptions import ValidationError

# Create your tests here.

class TestModels(TestCase):

    def test_smoke_Test(self):
        self.assertEqual(2+2,4)
    

    def setUp(self,nombre='lapiz',descripcion='2h',precio=25.0):
        self.articulo = Articulo.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio
        )

    def  test_return_object_articulo(self):
        self.articulo.save()
        self.assertEquals(self.articulo.nombre,str(self.articulo))
    
    def test_max_length_nombre(self):
        self.articulo.nombre = 'l'*100,
        self.assertLess(len(self.articulo.nombre),100)

    def test_longexcedida_mensaje(self):
        self.articulo.nombre = 'lapiz'*100,
        self.assertLess(len(self.articulo.nombre),100)
        with self.assertRaises(ValidationError):
            self.articulo.full_clean()

    def test_agrega_articulo(self):
        self.articulo.save()
        self.assertEqual(Articulo.objects.count(), 1)

    def test_prueba_mensaje_error(self):
        self.articulo.nombre = 'lapiz'*100
        try:
            self.articulo.full_clean()
        except ValidationError as ex:
            msg=str(ex.message_dict['nombre'][0])
            self.assertEquals(msg,LONGITUD_MAXIMA)

    def test_url_articulos_alta(self):
        respose = self.client.get('/articulo/')
        self.assertEqual(respose.status_code, 200)

    