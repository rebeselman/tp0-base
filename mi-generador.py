import sys


SERVER = """ server:
    container_name: server
    image: server:latest
    entrypoint: python3 /main.py
    volumes:
      - ./config_server.ini:/config.ini:ro
    networks:
      - testing_net
"""

CLIENT = """  client{ID}:
    container_name: client{ID}
    image: client:latest
    entrypoint: /client
    volumes:
      - ./config_client.yaml:/config.yaml:ro
    networks:
      - testing_net
    depends_on:
      - server
"""

NETWORK = """networks:
  testing_net:
    ipam:
      driver: default
      config:
        - subnet: 172.25.125.0/24
"""


# Genera un archivo docker compose con
# lacantidad de clientes pedidos y el nombre indicado
def generar_docker_compose(nombre_archivo, cantidad_clientes):
    with open(nombre_archivo, 'w') as f:
        f.write("name: tp0\n")
        f.write("services:\n")
        f.write(SERVER)
        f.write("\n")
        for i in range(1, cantidad_clientes + 1):
            f.write(CLIENT.format(ID=i))
            f.write("\n")
        f.write(NETWORK)


if __name__ == "__main__":
    nombre_archivo = sys.argv[1]
    cantidad_clientes = int(sys.argv[2])

    generar_docker_compose(nombre_archivo, cantidad_clientes)