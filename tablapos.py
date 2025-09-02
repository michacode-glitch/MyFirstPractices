#   Estructura - Tabla de posiciones
tabla_pos = [
        ['Grupo A'],
        ['Club', 'PJ', 'G', 'E', 'P', 'GF', 'GC', 'DG', 'Pts'],
        ['Argentino Jrs.', 16, 9, 6, 1, 24, 9, 15, 33],
        ['Boca Juniors', 16, 10, 3, 3, 24, 11, 13, 33],
        ['Racing', 16, 9, 1, 6, 26, 16, 10, 28],
        ['Huracan', 16, 7, 6, 3, 19, 12, 7, 27],
        ['Tigre', 16, 8, 3, 5, 18, 12, 6, 27]
]

#   Print 

print("=== TABLA DE POSICIONES ===")
print(f"{tabla_pos[0][0]:<15}")
print(f"{tabla_pos[1][0]:<20} {tabla_pos[1][1]:3} {tabla_pos[1][2]:3} {tabla_pos[1][3]:3} {tabla_pos[1][4]:3} {tabla_pos[1][5]:3} {tabla_pos[1][6]:3} {tabla_pos[1][7]:3} {tabla_pos[1][8]:3}")
print("-" * 55)


for i in range(2, len(tabla_pos)):
    stats = tabla_pos[i]
    print(f"{stats[0]:<20} {stats[1]:3} {stats[2]:3} {stats[3]:3} {stats[4]:3} {stats[5]:3} {stats[6]:3} {stats[7]:3} {stats[8]:3}")


