import numpy as np
import transforms3d as t3d
import yaml
import matplotlib.pyplot as plt

# --- Cargamos T_BS ---
with open("mav0/cam0/sensor.yaml", "r") as f:
    calib = yaml.safe_load(f)

T_BS = np.array(calib["T_BS"]["data"]).reshape(4, 4)

# --- Leemos archivo data.csv de groundtruth ---
poses = []
with open("mav0/state_groundtruth_estimate0/data.csv") as f:
    next(f)  # Se salta el encabezado para cargar desde el primer timestamp
    for line in f:
        vals = line.strip().split(",")
        if len(vals) < 8:
            continue
        t, x, y, z, qw, qx, qy, qz = vals[:8]
        poses.append([float(t), float(x), float(y), float(z),
                      float(qw), float(qx), float(qy), float(qz)])

poses = np.array(poses)
# Contiene la lista de poses en cada timestamp de la IMU como array de Nunpy
# (para las transformaciones)

print("\nPrimeras 5 filas del dataset original:")
for row in poses[:5]:
    print(row)

# --- Convertir timestamp a segundos con precision de nanosegundos ---
timestamps_ns = poses[:, 0]   # columna de timestamps original
timestamps_s = timestamps_ns.astype(np.float64) * 1e-9  # convertir a segundos

# Reemplazar la columna de timestamp en poses
poses[:, 0] = timestamps_s

print("\nPrimeras 5 filas del dataset resultante:")
for row in poses[:5]:
    print(row)
print("\n")

# --- Construimos las poses homogéneas de IMU en coordenadas del mundo ---
T_WB = []  # lista vacia para las poses de body en mundo
for t, x, y, z, qw, qx, qy, qz in poses:
    R = t3d.quaternions.quat2mat([qw, qx, qy, qz])  # [w,x,y,z]
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = [x, y, z]
    T_WB.append(T)

# --- Transformamos a cámara izquierda ---
T_WS = [T @ T_BS for T in T_WB]

# --- Llevamos al marco de la cámara inicial ---
# Definimos la primera pose de la camara izquierda en el origen
T0_inv = np.linalg.inv(T_WS[0])
# Obtenemos el camino en el sistema de coordenadas de la camara izquiera inicial
T_rel = [T0_inv @ T for T in T_WS]

# --- Extraemos las posiciones de ambos ---
# IMU (en coordenadas del mundo)
imu = np.array([T[:3, 3] for T in T_WB])

# Cámara izquierda (en coordenadas del mundo)
cam = np.array([T[:3, 3] for T in T_WS])

# --- GRAFICAS ---
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

# Grafica de la IMU
ax.plot(imu[:,0], imu[:,1], imu[:,2], label='IMU (body)', color='blue')

# Grafica de la cámara
ax.plot(cam[:,0], cam[:,1], cam[:,2], label='Cámara izquierda', color='red')

ax.set_xlabel('X [m]')
ax.set_ylabel('Y [m]')
ax.set_zlabel('Z [m]')
ax.set_title('Trayectorias Ground-Truth: IMU vs Cámara')
ax.legend()
ax.grid(True)

plt.show()

