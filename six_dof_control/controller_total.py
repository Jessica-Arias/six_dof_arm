#!/usr/bin/env python3

import sys, copy
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from controller_window_total import Ui_Form

import rospy
from sensor_msgs.msg import Image
from darknet_ros_msgs.msg import BoundingBoxes
from std_msgs.msg import Header
from std_msgs.msg import String
from actionlib_msgs.msg import GoalStatusArray


from geometry_msgs.msg import Pose
import moveit_commander

# status_robot = GoalStatusArray()

class Robot6dof(QDialog):
    
    def __init__(self,parent=None):
        super(Robot6dof, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        rospy.init_node('controller', anonymous=True)
        rospy.Subscriber('/darknet_ros/bounding_boxes', BoundingBoxes , self.boundig_boxes_callback)
        # rospy.Subscriber("/move_group/status", GoalStatusArray, self.status_callback)


        self.bounding_boxes = BoundingBoxes()
        # self.status_robot = GoalStatusArray()

        self.arm = moveit_commander.MoveGroupCommander("arm")
        self.gripper = moveit_commander.MoveGroupCommander("gripper")

    def Move_to_initial_position(self):
        self.arm.set_goal_tolerance(0.01)
        self.arm.set_named_target("pose_0")
        self.arm.go()

    def Move_to_Pose_1(self):
        self.arm.set_goal_tolerance(0.01)
        self.arm.set_named_target("pose_1")
        self.arm.go()

    def Move_to_Pose_Obj_1(self):
        self.arm.set_goal_tolerance(0.01)
        self.arm.set_named_target("pose_obj_1")
        self.arm.go()

    def Move_to_Pose_Obj_2(self):
        self.arm.set_goal_tolerance(0.01)
        self.arm.set_named_target("pose_obj_2")
        self.arm.go()

    def Grab(self):
        self.gripper.set_goal_tolerance(0.01)
        self.gripper.set_named_target("close")
        self.gripper.go()

    def Open(self):
        self.gripper.set_goal_tolerance(0.01)
        self.gripper.set_named_target("open")
        self.gripper.go()

    def boundig_boxes_callback(self, data):

        self.bounding_boxes = data

    """def status_callback(self, data):

        self.status_robot = data """

    def Classification_move(self):  
        self.Grab()
        self.Move_to_initial_position()

        for box in self.bounding_boxes.bounding_boxes:
            print(box.Class)
            if box.Class == "person":
                self.Open()
                self.Move_to_Pose_1()
                self.Grab()
                self.Move_to_Pose_Obj_1()
                self.Open()
                self.Move_to_initial_position()
                self.Grab()
                print("Ready")
                print("")
            elif box.Class == "dog":
                self.Open()
                self.Move_to_Pose_1()
                self.Grab()
                self.Move_to_Pose_Obj_2()
                self.Open()
                self.Move_to_initial_position()                
                self.Grab()
                print("Ready")
                print("")
            else:
                print("No se puede clasificar")
                print("")

def main():
    app = QApplication(sys.argv)
    window = Robot6dof()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    try :
        main()
    except rospy.ROSInterruptException:
        pass


