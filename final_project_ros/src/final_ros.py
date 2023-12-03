#!/usr/bin/env python

import rospy
from final_project_ros.srv import place, placeResponse  # Import the correct service message and response
from geometry_msgs.msg import PoseStamped

class FinalService():  # Correct class name to follow PEP 8 conventions

    def __init__(self):
        rospy.init_node('final_project')
        self.service = rospy.Service('/final_project/nav_goal', place, self.handle_nav_goal)
        self.pose_publisher = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
        
        rospy.spin()

    def handle_nav_goal(self, req):
        response = placeResponse()  # Create an instance of the response message
        response.pose_point.header.stamp = rospy.Time.now()

        if req.place == 0:
            response.pose_point.pose.position.x = 1.0
            response.pose_point.pose.position.y = 2.0
            self.pose_publisher.publish(response.pose_point)
            response.result = "complete"
        elif req.place == 1:
            response.pose_point.pose.position.x = 3.0
            response.pose_point.pose.position.y = 4.0
            self.pose_publisher.publish(response.pose_point)
            response.result = "complete"
        elif req.place == 2:
            response.pose_point.pose.position.x = 5.0
            response.pose_point.pose.position.y = 6.0
            self.pose_publisher.publish(response.pose_point)
            response.result = "complete"
        elif req.place == 3:
            response.pose_point.pose.position.x = 7.0
            response.pose_point.pose.position.y = 8.0
            self.pose_publisher.publish(response.pose_point)
            response.result = "complete"
        elif req.place == 4:
            response.pose_point.pose.position.x = 9.0
            response.pose_point.pose.position.y = 10.0
            self.pose_publisher.publish(response.pose_point)
            response.result = "complete"
        elif req.place == 5:
            response.pose_point.pose.position.x = 11.0
            response.pose_point.pose.position.y = 12.0
            self.pose_publisher.publish(response.pose_point)
            response.result = "complete"
            
        self.pose_publisher.publish(response.pose_point)
        return response

if __name__ == "__main__":
    FinalService()

