# Lista de procesos con (nombre, tiempo de llegada, tiempo de ejecución)
procesos = [
    {"nombre": "P1", "llegada": 0, "ejecucion": 8},
    {"nombre": "P2", "llegada": 1, "ejecucion": 4},
    {"nombre": "P3", "llegada": 2, "ejecucion": 9},
    {"nombre": "P4", "llegada": 3, "ejecucion": 5},
    {"nombre": "P5", "llegada": 4, "ejecucion": 2},
    {"nombre": "P6", "llegada": 5, "ejecucion": 7},
]


def srtf(procesos):
    tiempo_total = 0
    completados = 0
    n = len(procesos)
    tiempo_espera = [0] * n  # Lista para almacenar el tiempo de espera de cada proceso
    tiempo_restante = [p["ejecucion"] for p in procesos]  # Copia de tiempos de ejecución
    proceso_actual = None  # Proceso que se está ejecutando actualmente
    iniciado = [False] * n  # Registro para saber si el proceso ha iniciado alguna vez

    while completados < n:
        # Buscar el proceso con el menor tiempo restante que ya haya llegado
        menor_tiempo = float("inf")
        siguiente_proceso = None

        for i in range(n):
            if procesos[i]["llegada"] <= tiempo_total and tiempo_restante[i] < menor_tiempo and tiempo_restante[i] > 0:
                menor_tiempo = tiempo_restante[i]
                siguiente_proceso = i

        # Si no hay procesos disponibles, avanzar el tiempo
        if siguiente_proceso is None:
            tiempo_total += 1
            continue

        # Si el proceso actual cambia, verificar si el nuevo proceso se está colando
        if proceso_actual is not None and proceso_actual != siguiente_proceso and tiempo_restante[proceso_actual] > 0:
            print(
                f"Proceso {procesos[siguiente_proceso]['nombre']} se cuela a {procesos[proceso_actual]['nombre']} en el tiempo {tiempo_total}")

        # Mensaje de inicio si es la primera vez que el proceso comienza a ejecutarse
        if not iniciado[siguiente_proceso]:
            print(f"Proceso {procesos[siguiente_proceso]['nombre']} comienza a ejecutarse en el tiempo {tiempo_total}")
            iniciado[siguiente_proceso] = True

        # Actualizar el proceso actual
        proceso_actual = siguiente_proceso

        # Ejecutar el proceso seleccionado durante un tiempo (1 unidad)
        tiempo_restante[proceso_actual] -= 1
        tiempo_total += 1

        # Verificar si el proceso actual ha terminado
        if tiempo_restante[proceso_actual] == 0:
            completados += 1
            fin = tiempo_total
            tiempo_espera[proceso_actual] = fin - procesos[proceso_actual]["llegada"] - procesos[proceso_actual][
                "ejecucion"]
            print(f"{procesos[proceso_actual]['nombre']} completado en el tiempo {fin}")

    # Calcular el tiempo de espera promedio
    tiempo_espera_promedio = sum(tiempo_espera) / n
    print(f"\nTiempo de espera promedio: {tiempo_espera_promedio:.2f}")


# Ejecutar el algoritmo SRTF
srtf(procesos)
