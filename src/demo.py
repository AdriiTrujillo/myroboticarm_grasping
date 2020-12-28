#! /usr/bin/env python
import sys
import rospy
import moveit_commander
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('Demo_grasping_myroboticarm', anonymous=True)
robot = moveit_commander.RobotCommander()


# Obtenemos el grupo del brazo
arm_group = moveit_commander.MoveGroupCommander("arm")
# Llevamos al robot hasta la posicion incial de reposo
arm_group.set_named_target("home")
plan1 = arm_group.go()

# Obtenemos el grupo del efector final
hand_group = moveit_commander.MoveGroupCommander("hand")
# Ponemos el robot en la posicion de abrir de abrir la pinza
hand_group.set_named_target("Open")
plan2 = hand_group.go()

# ------ Empezamos la tarea ------------------------------

# Obtenemos el grupo del brazo
arm_group = moveit_commander.MoveGroupCommander("arm")
# Movemos el brazo a una posicion previamente conocida y definida
arm_group.set_named_target("Target_1")
plan1 = arm_group.go()

# Obtenemos el grupo del efector final
hand_group = moveit_commander.MoveGroupCommander("hand")
# Realizamos la accion de cerrar la pinza
hand_group.set_named_target("Close")
plan2 = hand_group.go()

# Obtenemos el grupo del brazo
arm_group = moveit_commander.MoveGroupCommander("arm")
# Movemos el brazo a otra posicion previamente conocida y definida
arm_group.set_named_target("Target_2")
plan1 = arm_group.go()

# Obtenemos el grupo del gripper
hand_group = moveit_commander.MoveGroupCommander("hand")
# Abrimos la pinza para soltar el objeto que habriamos cogido en la accion anterior
hand_group.set_named_target("Open")
plan2 = hand_group.go()

# --------------------------- Fin de la tarea -----------------------------------
# ------------ Llevamos el robot a la posicion de reposo ------------------------

# Obtenemos el grupo del brazo
arm_group = moveit_commander.MoveGroupCommander("arm")
# Llevamos al robot hasta la posicion incial de reposo
arm_group.set_named_target("home")
plan1 = arm_group.go()


rospy.sleep(5)
moveit_commander.roscpp_shutdown()