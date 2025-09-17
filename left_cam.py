import numpy as np
import transforms3d as t3d
import yaml

# --- Cargamos T_BS ---
with open("mav0/cam0/sensor.yaml", "r") as f:
    calib = yaml.safe_load(f)

T_BS = np.array(calib["T_BS"]["data"]).reshape(4, 4) # Matriz 4x4

# --- Leemos archivo data.csv de groundtruth ---
poses = []
with open("mav0/state_groundtruth_estimate0/data.csv") as f:
    next(f)  # se salta el encabezado para cargar desde el primer timestamp
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

# --- Construimos las poses homogéneas de IMU en coordenadas del mundo ---
T_WB = []  # lista vacia para las poses de body en mundo
for t, x, y, z, qw, qx, qy, qz in poses:
    R = t3d.quaternions.quat2mat([qw, qx, qy, qz])  # [w,x,y,z]
    T = np.eye(4)
    T[:3, :3] = R  # Reemplazo los elementos 3x3 (orientacion) en la identidad
    T[:3, 3] = [x, y, z]  # Agrego la posición en la columna 4
    T_WB.append(T)  # lleno la lista de poses (camino) para cada timestemp

# --- Transformamos a cámara izquierda ---
T_WS = [T @ T_BS for T in T_WB]

# --- Llevamos al marco de la cámara inicial ---
# Definimos la primera pose de la camara izquierda en el origen
T0_inv = np.linalg.inv(T_WS[0])
# Obtenemos el camino en el sistema de coordenadas de la camara izquiera inicial
T_rel = [T0_inv @ T for T in T_WS]

