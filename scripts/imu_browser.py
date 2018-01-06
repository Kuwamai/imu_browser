#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Imu

def recv_imu(message):
	accel = message.linear_acceleration
	omega = message.angular_velocity
	print accel.x, accel.y, accel.z, omega.x, omega.y, omega.z

if __name__ == '__main__':
	rospy.init_node('imu_subscriber')
	rospy.Subscriber("imu/data_raw", Imu, recv_imu)
	rospy.spin()
