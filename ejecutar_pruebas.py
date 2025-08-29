import subprocess
import sys
import os

def run_test_file(test_file):
    """Ejecuta un archivo de pruebas específico"""
    print(f"\n{'='*50}")
    print(f"Ejecutando: {test_file}")
    print(f"{'='*50}")
    
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        test_file_path = os.path.join(script_dir, test_file)
        
        if not os.path.exists(test_file_path):
            print(f"❌ ERROR: El archivo {test_file} no existe en {script_dir}")
            return
        
        result = subprocess.run([sys.executable, test_file_path], 
                              capture_output=True, text=True)
        
        print("SALIDA:")
        print(result.stdout)
        
        if result.stderr:
            print("ERRORES:")
            print(result.stderr)
            
        if result.returncode == 0:
            print("✅ PRUEBAS PASARON")
        else:
            print("❌ ALGUNAS PRUEBAS FALLARON")
            
    except Exception as e:
        print(f"Error ejecutando {test_file}: {e}")

if __name__ == "__main__":
    print("🧪 EJECUTANDO SUITE DE PRUEBAS")
    print("SENA - ADSO")
    print(f"Directorio actual: {os.getcwd()}")
    print(f"Directorio de scripts: {os.path.dirname(os.path.abspath(__file__))}")
    
    # Lista de archivos de prueba a ejecutar
    test_files = [
        'test_usuario.py',
        'test_custom_user.py'
    ]
    
    for test_file in test_files:
        run_test_file(test_file)
    
    print(f"\n{'='*50}")
    print("✨ EJECUCIÓN DE PRUEBAS COMPLETADA")
    print(f"{'='*50}")
