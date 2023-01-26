#!/usr/bin/env/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse

"""
Set of classes for defining SE(3) trajectories for the end effector of a robot 
manipulator
"""

class Trajectory:

    def __init__(self, total_time):
        """
        Parameters
        ----------
        total_time : float
        	desired duration of the trajectory in seconds 
        """
        self.total_time = total_time
        self.init_pos = np.array([0, 0, 0])
        self.init_oren = np.array([0, 1, 0, 0])
        self.init_vel = 0
        self.end_vel = 0

    def target_pose(self, time):
        """
        Returns where the arm end effector should be at time t, in the form of a 
        7D vector [x, y, z, qx, qy, qz, qw]. i.e. the first three entries are 
        the desired end-effector position, and the last four entries are the 
        desired end-effector orientation as a quaternion, all written in the 
        world frame.

        Hint: The end-effector pose with the gripper pointing down corresponds 
        to the quaternion [0, 1, 0, 0]. 

        Parameters
        ----------
        time : float        
    
        Returns
        -------
        7x' :obj:`numpy.ndarray`
            desired configuration in workspace coordinates of the end effector
        """
        pass

    def target_velocity(self, time):
        """
        Returns the end effector's desired body-frame velocity at time t as a 6D
        twist. Note that this needs to be a rigid-body velocity, i.e. a member 
        of se(3) expressed as a 6D vector.
        
        Parameters
        ----------
        time : float

        Returns
        -------
        6x' :obj:`numpy.ndarray`
            desired body-frame velocity of the end effector
        """
        pass

    def display_trajectory(self, num_waypoints=67, show_animation=False, save_animation=False):
        """
        Displays the evolution of the trajectory's position and body velocity.

        Parameters
        ----------
        num_waypoints : int
            number of waypoints in the trajectory
        show_animation : bool
            if True, displays the animated trajectory
        save_animatioon : bool
            if True, saves a gif of the animated trajectory
        """
        trajectory_name = self.__class__.__name__
        times = np.linspace(0, self.total_time, num=num_waypoints)
        target_positions = np.vstack([self.target_pose(t)[:3] for t in times])
        target_velocities = np.vstack([self.target_velocity(t)[:3] for t in times])
        
        fig = plt.figure(figsize=plt.figaspect(0.5))
        colormap = plt.cm.brg(np.fmod(np.linspace(0, 1, num=num_waypoints), 1))

        # Position plot
        ax0 = fig.add_subplot(1, 2, 1, projection='3d')
        pos_padding = [[-0.1, 0.1],
                        [-0.1, 0.1],
                        [-0.1, 0.1]]
        ax0.set_xlim3d([min(target_positions[:, 0]) + pos_padding[0][0], 
                        max(target_positions[:, 0]) + pos_padding[0][1]])
        ax0.set_xlabel('X')
        ax0.set_ylim3d([min(target_positions[:, 1]) + pos_padding[1][0], 
                        max(target_positions[:, 1]) + pos_padding[1][1]])
        ax0.set_ylabel('Y')
        ax0.set_zlim3d([min(target_positions[:, 2]) + pos_padding[2][0], 
                        max(target_positions[:, 2]) + pos_padding[2][1]])
        ax0.set_zlabel('Z')
        ax0.set_title("%s evolution of\nend-effector's position." % trajectory_name)
        line0 = ax0.scatter(target_positions[:, 0], 
                        target_positions[:, 1], 
                        target_positions[:, 2], 
                        c=colormap,
                        s=2)

        # Velocity plot
        ax1 = fig.add_subplot(1, 2, 2, projection='3d')
        vel_padding = [[-0.1, 0.1],
                        [-0.1, 0.1],
                        [-0.1, 0.1]]
        ax1.set_xlim3d([min(target_velocities[:, 0]) + vel_padding[0][0], 
                        max(target_velocities[:, 0]) + vel_padding[0][1]])
        ax1.set_xlabel('X')
        ax1.set_ylim3d([min(target_velocities[:, 1]) + vel_padding[1][0], 
                        max(target_velocities[:, 1]) + vel_padding[1][1]])
        ax1.set_ylabel('Y')
        ax1.set_zlim3d([min(target_velocities[:, 2]) + vel_padding[2][0], 
                        max(target_velocities[:, 2]) + vel_padding[2][1]])
        ax1.set_zlabel('Z')
        ax1.set_title("%s evolution of\nend-effector's translational body-frame velocity." % trajectory_name)
        line1 = ax1.scatter(target_velocities[:, 0], 
                        target_velocities[:, 1], 
                        target_velocities[:, 2], 
                        c=colormap,
                        s=2)

        if show_animation or save_animation:
            def func(num, line):
                line[0]._offsets3d = target_positions[:num].T
                line[0]._facecolors = colormap[:num]
                line[1]._offsets3d = target_velocities[:num].T
                line[1]._facecolors = colormap[:num]
                return line

            # Creating the Animation object
            line_ani = animation.FuncAnimation(fig, func, frames=num_waypoints, 
                                                          fargs=([line0, line1],), 
                                                          interval=max(1, int(1000 * self.total_time / (num_waypoints - 1))), 
                                                          blit=False)
        plt.show()
        if save_animation:
            line_ani.save('%s.gif' % trajectory_name, writer='pillow', fps=60)
            print("Saved animation to %s.gif" % trajectory_name)

class LinearTrajectory(Trajectory):


    def __init__(self, goal_pos, total_time):
        """
        Remember to call the constructor of Trajectory

        Parameters
        ----------
        ????? You're going to have to fill these in how you see fit
        """
        pass
        # Trajectory.__init__(self, ...)
        self.goal_pos = np.array([2, 10, 0])
        self.init_pos = np.array([0, 0, 0])
        self.init_oren = np.array([0, 1, 0, 0])
        self.total_time = total_time       


    def target_pose(self, time):
        """
        Returns where the arm end effector should be at time t, in the form of a 
        7D vector [x, y, z, qx, qy, qz, qw]. i.e. the first three entries are 
        the desired end-effector position, and the last four entries are the 
        desired end-effector orientation as a quaternion, all written in the 
        world frame.

        Hint: The end-effector pose with the gripper pointing down corresponds 
        to the quaternion [0, 1, 0, 0]. 

        Parameters
        ----------
        time : float        
    
        Returns
        -------
        7x' :obj:`numpy.ndarray`
            desired configuration in workspace coordinates of the end effector
        """
        xd = abs(self.goal_pos[0] - self.init_pos[0])
        yd = abs(self.goal_pos[1] - self.init_pos[1]) 
        zd = abs(self.goal_pos[2] - self.init_pos[2])
        timeTot = self.total_time

        if time < self.total_time/2 :
            # finding slopes 
            xk = 4*xd / (self.total_time ** 2)
            yk = 4*yd / (self.total_time ** 2)
            zk = 4*zd / (self.total_time ** 2)

            # to find the C part of the integral plugged in time = totaltime divided by 2
            pxC = -  1/2*xk*(self.total_time/2)**2 
            pyC = -  1/2*yk*(self.total_time/2)**2      #changed: was d/2 - 1/2*yk(...)
            pzC = -  1/2*zk*(self.total_time/2)**2

            # final line equations
            px = 1/2 * xk * time**2 + pxC
            py = 1/2 * yk * time**2 + pyC
            pz = 1/2 * zk * time**2 + pzC

            position = np.array([px, py, pz, 0, 1, 0, 0])

        else: 
            xk = -4*xd / (self.total_time ** 2)
            yk = -4*yd / (self.total_time ** 2)
            zk = -4*zd / (self.total_time ** 2)

            pxC = xd - 1/2*xk*(self.total_time/2)**2 
            pyC = yd - 1/2*yk*(self.total_time/2)**2 
            pzC = zd - 1/2*zk*(self.total_time/2)**2

            px = - 1/2 * xk * time**2 + xk* time*timeTot + pxC
            py = - 1/2 * yk * time**2 + yk* time* timeTot + pyC
            pz = - 1/2 * zk * time**2 + zk* time* timeTot + pzC

            position = np.array([px, py, pz, 0, 1, 0, 0])

        return position 

    def target_velocity(self, time):

        xd = abs(self.goal_pos[0] - self.init_pos[0])
        yd = abs(self.goal_pos[1] - self.init_pos[1]) 
        zd = abs(self.goal_pos[2] - self.init_pos[2])
        timeTot = self.total_time 

        if time < self.total_time/2 :
            # finding slopes 
            xk = 4*xd / (self.total_time ** 2)
            yk = 4*yd / (self.total_time ** 2)
            zk = 4*zd / (self.total_time ** 2) 

            xv = xk * time 
            yv = yk * time
            zv = zk * time

            vel = np.array([xv, yv, zv, 0, 0, 0])
        else: 
            xk = - 4*xd / (self.total_time ** 2)
            yk = - 4*yd / (self.total_time ** 2)
            zk = - 4*zd / (self.total_time ** 2)

            xv = -xk * time + xk * timeTot
            yv = -yk * time + yk * timeTot
            zv = -zk * time + zk * timeTot 

            vel = np.array([xv, yv, zv, 0, 0, 0])

        return vel
        """
        Returns the end effector's desired body-frame velocity at time t as a 6D
        twist. Note that this needs to be a rigid-body velocity, i.e. a member 
        of se(3) expressed as a 6D vector.

        Parameters
        ----------
        time : float

        Returns
        -------
        6x' :obj:`numpy.ndarray`
            desired body-frame velocity of the end effector
        """

class CircularTrajectory(Trajectory):

    def __init__(self, center_position, radius, total_time):
        """
        Remember to call the constructor of Trajectory

        Parameters
        ----------
        ????? You're going to have to fill these in how you see fit
        """
        pass
        # Trajectory.__init__(self, ...)
        self.radius = radius
        self.total_time = total_time
        self.center_position = center_position

    def target_pose(self, time):
        """
        Returns where the arm end effector should be at time t, in the form of a 
        7D vector [x, y, z, qx, qy, qz, qw]. i.e. the first three entries are 
        the desired end-effector position, and the last four entries are the 
        desired end-effector orientation as a quaternion, all written in the 
        world frame.

        Hint: The end-effector pose with the gripper pointing down corresponds 
        to the quaternion [0, 1, 0, 0]. 

        Parameters
        ----------
        time : float        
    
        Returns
        -------
        7x' :obj:`numpy.ndarray`
            desired configuration in workspace coordinates of the end effector
        """
        ##init_pos = np.array([self.center_position[0] - self.radius, self.center_position[1]])
        k = 8*np.pi*self.radius/self.total_time**2

        if time < self.total_time/2:
            vel = k*time
            theta = 1/2*k*time**2

            x = self.radius * np.cos(theta)
            y = self.radius * np.sin(theta)

            position = np.array([x, y, 0, 0, 1, 0, 0])

        else:
            vel = -k*time + k*self.total_time
            C = np.pi - 3/8*k*self.total_time**2
            theta = -1/2*k*time**2 + k*self.total_time*time + C

            x = self.radius * np.cos(theta)
            y = self.radius * np.sin(theta)

            position = np.array([x, y, 0, 0, 1, 0, 0])

        return position


    def target_velocity(self, time):
        """
        Returns the end effector's desired body-frame velocity at time t as a 6D
        twist. Note that this needs to be a rigid-body velocity, i.e. a member 
        of se(3) expressed as a 6D vector.

        Parameters
        ----------
        time : float

        Returns
        -------
        6x' :obj:`numpy.ndarray`
            desired body-frame velocity of the end effector
        """
        init_pos = np.array([self.center_position[0] - self.radius, self.center_position[1]])
        k = 8*np.pi*self.radius/self.total_time**2

        if time < self.total_time/2:
            vel = k*time
            theta = 1/2*k*time**2

            x_vel = self.radius * vel * np.sin(theta)
            y_vel = self.radius * vel * np.cos(theta)

            velocity = np.array([x_vel, y_vel, 0, 0, 0, 0])

        else:
            vel = -k*time + k*self.total_time
            C = np.pi - 3/8*k*self.total_time**2
            theta = -1/2*k*time**2 + k*self.total_time*time + C

            x_vel = self.radius * vel * np.sin(theta)
            y_vel = self.radius * vel * np.cos(theta)

            velocity = np.array([x_vel, y_vel, 0, 0, 0, 0])

        return velocity

class PolygonalTrajectory(Trajectory):
    def __init__(self, points, total_time):
        """
        Remember to call the constructor of Trajectory.
        You may wish to reuse other trajectories previously defined in this file.

        Parameters
        ----------
        ????? You're going to have to fill these in how you see fit

        """
        pass
        # Trajectory.__init__(self, total_time)

    def target_pose(self, time):
        """
        Returns where the arm end effector should be at time t, in the form of a 
        7D vector [x, y, z, qx, qy, qz, qw]. i.e. the first three entries are 
        the desired end-effector position, and the last four entries are the 
        desired end-effector orientation as a quaternion, all written in the 
        world frame.

        Hint: The end-effector pose with the gripper pointing down corresponds 
        to the quaternion [0, 1, 0, 0]. 

        Parameters
        ----------
        time : float        
    
        Returns
        -------
        7x' :obj:`numpy.ndarray`
            desired configuration in workspace coordinates of the end effector
        """
        pass
        
    def target_velocity(self, time):
        """
        Returns the end effector's desired body-frame velocity at time t as a 6D
        twist. Note that this needs to be a rigid-body velocity, i.e. a member 
        of se(3) expressed as a 6D vector.

        Parameters
        ----------
        time : float

        Returns
        -------
        6x' :obj:`numpy.ndarray`
            desired body-frame velocity of the end effector
        """
        pass

def define_trajectories(args):
    """ Define each type of trajectory with the appropriate parameters."""
    trajectory = None
    if args.task == 'line':
        trajectory = LinearTrajectory(np.array([0, 3, 6]), 10.0)
    elif args.task == 'circle':
        trajectory = CircularTrajectory(np.array([0, 0, 0]), 2, 20)
    elif args.task == 'polygon':
        trajectory = PolygonalTrajectory()
    return trajectory

if __name__ == '__main__':
    """
    Run this file to visualize plots of your paths. Note: the provided function
    only visualizes the end effector position, not its orientation. Use the 
    animate function to visualize the full trajectory in a 3D plot.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-task', '-t', type=str, default='line', help=
        'Options: line, circle, polygon.  Default: line'
    )
    parser.add_argument('--animate', action='store_true', help=
        'If you set this flag, the animated trajectory will be shown.'
    )
    args = parser.parse_args()

    trajectory = define_trajectories(args)
    
    if trajectory:
        trajectory.display_trajectory(show_animation=args.animate)
