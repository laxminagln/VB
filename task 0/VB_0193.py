#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

PI = 3.1415926535

class TurtleRevolve(object):
    
    def __init__(self):
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.vel_msg = Twist()
        rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)

    def set_velocities(self, linear_vel, angular_vel):
        self.vel_msg.linear.x = linear_vel
        self.vel_msg.angular.z = angular_vel

    @classmethod
    def pose_callback(cls, msg):
        print "Moving in a Circle"
        print msg.theta

    def draw_circle(self):
        now = rospy.Time.now()
        rate = rospy.Rate(10)
        radius = self.vel_msg.linear.x/self.vel_msg.angular.z
        time = (2*PI*radius)/self.vel_msg.linear.x

        while rospy.Time.now() < now + rospy.Duration.from_sec(time):
            self.velocity_publisher.publish(self.vel_msg)
            rate.sleep()

def main():
    rospy.init_node('node_turtle_revolve', anonymous=True)
    circle = TurtleRevolve()
    circle.set_velocities(1, 1)
    circle.draw_circle()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
