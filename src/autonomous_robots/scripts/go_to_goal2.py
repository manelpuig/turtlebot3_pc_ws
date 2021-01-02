#!/usr/bin/env python
# license removed for brevity

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = 0.883261655683
    goal.target_pose.pose.position.y = 0.0143495894055
    goal.target_pose.pose.position.z = -0.00101095064357
    goal.target_pose.pose.orientation.z = -0.673835083899
    goal.target_pose.pose.orientation.w = 0.73888004246

    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server DOWN ;/ ")
    else:
        return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('movebaseClient')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal is EXECUTED!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation DONE ")