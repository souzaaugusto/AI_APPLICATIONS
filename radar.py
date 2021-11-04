#!/usr/bin/env python

#
# Copyright (c) 2019-2020 Intel Corporation
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.
#
"""
Classes to handle Carla Radar
"""

import math

import pandas as pd

from carla_msgs.msg import CarlaRadarMeasurement, CarlaRadarDetection
from carla_ros_bridge.sensor import Sensor
import rospy


class Radar(Sensor):

    """
    Actor implementation details of Carla RADAR
    """

    def __init__(self,carla_actor, parent, communication, synchronous_mode):
        """
        Constructor
        :param carla_actor: carla actor object
        :type carla_actor: carla.Actor
        :param parent: the parent of this
        :type parent: carla_ros_bridge.Parent
        :param communication: communication-handle
        :type communication: carla_ros_bridge.communication
        :param synchronous_mode: use in synchronous mode?
        :type synchronous_mode: bool
        """
       # Retrieves the world model         # Retrieves the ego_vehicle
        super(Radar, self).__init__(
                                    carla_actor=carla_actor,
                                    parent=parent,
                                    communication=communication,
                                    synchronous_mode=synchronous_mode,
                                    prefix="radar/" + carla_actor.attributes.get('role_name'))

    # pylint: disable=arguments-differ

    def sensor_data_updated(self, carla_radar_measurement):
        """
        Function to transform the a received Radar measurement into a ROS message

        :param carla_radar_measurement: carla Radar measurement object
        :type carla_radar_measurement: carla.RadarMeasurement
        """
        
        result = open("/home/rota2030/Desktop/detection_raw_data.txt","a") #Save the detection data into a txt file
        radar_msg = CarlaRadarMeasurement()
        radar_msg.header = self.get_msg_header(timestamp=carla_radar_measurement.timestamp)
        radar_detection = CarlaRadarDetection()
        for detection in carla_radar_measurement:
            radar_detection.altitude = detection.altitude
            radar_detection.azimuth = detection.azimuth
            radar_detection.depth = detection.depth
            radar_detection.velocity = detection.velocity
            radar_msg.detections.append(radar_detection)
        self.publish_message(self.get_topic_prefix() + "/radar", radar_msg)
        rospy.loginfo("Detection: {}".format(radar_detection)) #Show the detection data from the terminal
        result.write(str(radar_detection))
        result.close()
        