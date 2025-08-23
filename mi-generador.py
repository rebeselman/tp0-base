import sys


# Genera un archivo docker compose con
# lacantidad de clientes pedidos y el nombre indicado
def generar_docker_compose(nombre_archivo, cantidad_clientes):
    with open(nombre_archivo, 'w') as f:
        f.write("name: tp0\n")
        f.write("services:\n")
        f.write("  server:\n")
        f.write("    container_name: server\n")
        f.write("    image: server:latest\n")
        f.write("    entrypoint: python3 /main.py\n")
        f.write("    environment:\n")
        f.write("      - PYTHONUNBUFFERED=1\n")
        f.write("      - LOGGING_LEVEL=DEBUG\n")
        f.write("    networks:\n")
        f.write("      - testing_net\n")
        
        f.write("\n")
        for i in range(1, cantidad_clientes + 1):
            f.write(f"  client{i}:\n")
            f.write(f"    container_name: client{i}\n")
            f.write("    image: client:latest\n")
            f.write("    entrypoint: /client\n")
            f.write(f"    environment:\n")
            f.write(f"      - CLI_ID={i}\n")
            f.write("      - CLI_LOG_LEVEL=DEBUG\n")
            f.write("    networks:\n")
            f.write("      - testing_net\n")
            f.write("    depends_on:\n")
            f.write("      - server\n")
            f.write("\n")



        f.write("networks:\n")
        f.write("  testing_net:\n")
        f.write("    ipam:\n")
        f.write("      driver: default\n")
        f.write("      config:\n")
        f.write("        - subnet: 172.25.125.0/24\n")






if __name__ == "__main__":
    nombre_archivo = sys.argv[1]
    cantidad_clientes = int(sys.argv[2])

    generar_docker_compose(nombre_archivo, cantidad_clientes)
    print(f"Archivo {nombre_archivo} generado con {cantidad_clientes} clientes.")