
from .configuracion import ventana_altura,ventana_ancho,RGB,fps,frame_height,frame_width
from .personaje  import Personaje
from .mascota import Mascota
from .bala_ import Bala,disparar
from .mapas import Mapa1,Mapa2
from .config_mapas import imagen, construir_mapa

__all__=["construir_mapa","imagen","Mapa1","Mapa2",
         "Bala","disparar"
         ,"Personaje","Mascota",
         "ventana_altura","ventana_ancho","RGB","frame_height","frame_width","fps"]
#__all__ lista de cadenas que dice que modulos se van a exportar de los import