import numpy as np
import sys
def rotation_matrix(theta_x, theta_y, theta_z):
    theta_x = (theta_x * np.pi) / 180
    theta_y = (theta_y * np.pi) / 180
    theta_z = (theta_z * np.pi) / 180
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(theta_x), -np.sin(theta_x)],
        [0, np.sin(theta_x), np.cos(theta_x)]
    ])
    Ry = np.array([
        [np.cos(theta_y), 0, np.sin(theta_y)],
        [0, 1, 0],
        [-np.sin(theta_y), 0, np.cos(theta_y)]
    ])
    Rz = np.array([
        [np.cos(theta_z), -np.sin(theta_z), 0],
        [np.sin(theta_z), np.cos(theta_z), 0],
        [0, 0, 1]
    ])
    aRb = Rx.dot(Ry).dot(Rz)
    return (aRb)

def pure_translation(Px, Py, Pz, dx, dy, dz):
    initial_vector = np.array([
        [Px],
        [Py],
        [Pz]
    ])
    displacement = np.array([
        [dx],
        [dy],
        [dz]
    ])
    translated_vector = initial_vector + displacement
    return translated_vector

def pure_rotation(Vx, Vy, Vz, theta_x, theta_y, theta_z):
    aRb = rotation_matrix(theta_x, theta_y, theta_z)
    V = np.array([
        [Vx],
        [Vy],
        [Vz]
    ])
    pure_rotation_vector = np.dot(aRb, V)
    return pure_rotation_vector

entry = input("Is the question a purely translative, purely rotative or a hybrid type :")

try:
    if entry in ("purely translative", "translative", "pure translative"):
        l1 = eval(input("Enter coordinates of initial vector separated by commas: "))
        l2 = eval(input("Enter the values of translation in each axis separated by commas: "))
        translated = pure_translation(l1[0], l1[1], l1[2], l2[0], l2[1], l2[2])
        print(f"The final vector required is ", translated[0][0], "i + ", translated[1][0], "j + ", translated[2][0],
              "k")

    elif entry in ("purely rotative", "rotative", "pure rotative"):
        l3 = eval(input("Enter the coordinates of initial vector: "))
        l4 = eval(
            input("Enter the values of the angles of rotaion about x, y and z respectively separated by commas: "))
        rotated = pure_rotation(l3[0], l3[1], l3[2], l4[0], l4[1], l4[2])
        print(f"The final vector required is ", int(rotated[0][0]), "i + ", int(rotated[1][0]), "j + ",
              int(rotated[2][0]), "k")

    elif entry in ("hybrid", "both"):
        l5 = eval(input("Enter the coordinates of initial vector: "))
        l6 = eval(
            input("Enter the values of the angles of rotaion about x, y and z respectively separated by commas: "))
        l7 = eval(input("Enter values of translation along x, y and z axes respectively separated by commas: "))
        rot = rotation_matrix(l6[0], l6[1], l6[2])
        transformation_matrix = np.eye(4)
        transformation_matrix[:3, :3] = rot
        transformation_matrix[:3, 3] = l7
        print(transformation_matrix)
        initial_matrix = np.array([
            [l5[0]],
            [l5[1]],
            [l5[2]],
            [1]
        ])
        final_matrix = np.dot(transformation_matrix, initial_matrix)
        print("The resultant vector is \n", final_matrix[:3])

    else:
        print("Invalid input. Please recheck prompt!")

except:
    print("Error.. try again")
    sys.exit(0)

