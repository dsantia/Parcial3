from django.urls import path

from . import views

app_name = "contactos"

urlpatterns = [
    path("departamento/",views.DepartamentoListView.as_view(), name="ListaDepartamento"), 
    path("departamento/nuevo/",views.DepartamentoCreateView.as_view(), name="NuevoDepartamento"), 
    path("departamento/update/<int:pk>/",views.DepartamentoUpdateView.as_view(), name="EditarDepartamento"), 
    path("departamento/eliminar/<int:pk>/",views.DepartamentoDeleteView.as_view(), name="BorrarDepartamento"), 
    path("departamento/detalle/<int:pk>/",views.DepartamentoDetailView.as_view(), name="DetalleDepartamento"), 

    path("telefono/",views.TelefonoListView.as_view(), name="ListaTelefono"), 
    path("telefono/nuevo/",views.TelefonoCreateView.as_view(), name="NuevoTelefono"), 
    path("telefono/update/<int:pk>/",views.TelefonoUpdateView.as_view(), name="EditarTelefono"), 
    path("telefono/eliminar/<int:pk>/",views.TelefonoDeleteView.as_view(), name="BorrarTelefono"), 
    path("telefono/detalle/<int:pk>/",views.TelefonoDetailView.as_view(), name="DetalleTelefono"), 
    
    path("inscrito/",views.InscritoListView.as_view(), name="ListaInscrito"), 
    path("inscrito/nuevo/",views.InscritoCreateView.as_view(), name="NuevoInscrito"), 
    path("inscrito/update/<int:pk>/",views.InscritoUpdateView.as_view(), name="EditarInscrito"), 
    path("inscrito/eliminar/<int:pk>/",views.InscritoDeleteView.as_view(), name="BorrarInscrito"), 
    path("inscrito/detalle/<int:pk>/",views.InscritoDetailView.as_view(), name="DetalleInscrito"), 

    path("responsable/",views.ResponsableListView.as_view(), name="ListaResponsable"), 
    path("responsable/nuevo/",views.ResponsableCreateView.as_view(), name="NuevoResponsable"), 
    path("responsable/update/<int:pk>/",views.ResponsableUpdateView.as_view(), name="EditarResponsable"), 
    path("responsable/eliminar/<int:pk>/",views.ResponsableDeleteView.as_view(), name="BorrarResponsable"), 
    path("responsable/detalle/<int:pk>/",views.ResponsableDetailView.as_view(), name="DetalleResponsable"), 

    path("contacto/",views.ContactoListView.as_view(), name="ListaContacto"),
    path("contacto/nuevo/",views.ContactoCreateView.as_view(), name="NuevoContacto"), 
    path("contacto/update/<int:pk>/",views.ContactoUpdateView.as_view(), name="EditarContacto"), 
    path("contacto/eliminar/<int:pk>/",views.ContactoDeleteView.as_view(), name="BorrarContacto"), 
    path("contacto/detalle/<int:pk>/",views.ContactoDetailView.as_view(), name="DetalleContacto"),  
]
