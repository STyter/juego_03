import sys
import os

# Agrega la carpeta raíz del proyecto (una carpeta arriba de 'recursos') al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.main import main

if __name__ == "__main__":
    main()
