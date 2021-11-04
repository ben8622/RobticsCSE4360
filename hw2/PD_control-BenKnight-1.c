/*
 * BENJAMIN KNIGHT
 * 1001788622
 * 4360-001, Robotics with Manfred Hubner - Homework 2
 * Goal: Perform system identification to determine the dynamics of the system
 */

#include <stdio.h>
#include <math.h>

double prev_theta_dot = 0;

double PD_control(theta, theta_dot, theta_ref, theta_dot_ref)
double theta, theta_dot, theta_ref, theta_dot_ref;
{
	// ~~~ CALCULATE theta_dot_dot (used for I) ~~~
	double delta_theta_dot = theta_dot - prev_theta_dot;
	double time_passed = 0.002; // 500Hz = 0.002 seconds each cycle
	double theta_dot_dot = delta_theta_dot / time_passed;
	prev_theta_dot = theta_dot; // keep track of velcoity changes
	
	/* ~~~ CALCULATE G(theta) ~~~
	 * Here we have calculated the constant in the G(theta) function, mgl
	 * to do so we applied a constant force (the number is arbitrary) and then
	 * calculated the tangential part of it with constant_force/cos(theta) = mgl
	 * 1.) apply constant_force
	 * 2.) observe the equation constant_force/cos(theta) until it has stopped oscilating
	 */
	double mgl = 1.176;
	double G = mgl*cos(theta);

	/* ~~~ CALCULATE B ~~~
	 * To calculate B, we apply another constant_force along with the gravitational offset
	 * this makes the arm act as if it is weightless and its only dragging factors
	 * are friction. This looks like return( 1 + G ), to prove velocity is constant we
	 * can just print out theta_dot and observe. To calculate B, it is the constant_force/theta_dot.
	 * Acceleration here is essentially 0 so we do not worry about it.
	 * 1.) Apply constant_force alongside G(theta)
	 * 2.) Observe theta_dot to make sure it is constant (within error)
	 * 3.) calculate B, B = constant_force / theta_dot
	 */
	double B = 0.10001;
	
	/* ~~~ CALCULATE I ~~~
	 * To calculate I, it is almost the exact same process as above expect now instead
	 * of just compensation for gravity, we also compensate for friction. This
	 * looks like return( 1 + B*theta_dot + G ), where 1 is the constant force. ADDITIONALLY
	 * we need to calculate angular acceleration with delta_theta_dot/delta_time. Delta_time
	 * is given to us as 500Hz or .002 seconds. Delta_theta_dot we calculate by keeping track of
	 * previous theta_dot through a global variable.
	 * 1.) Apply a constant_force alongside B*theta_dot + G(theta)
	 * 2.) Observe theta_dot_dot to ensure that your acceleration is constant (within error)
	 * 	-- It is important to note, the error in your B value will show here 
	 * 	   the larger the error, the larger of fluxuations you will see in your acceleration
	 * 3.) calculate I, I = constant_force / theta_dot_dot
	 */
	double I = 0.036;
	
	// PD Controller Implementation
	double Kp = 1; 				// proportional gain, this value is dependant on
								// the values found through system identification, must play around
								// and find out how much of a dampener you need to fix your errors
																
	double Kd = 2 * sqrt(Kp);	// derivative gain
	
	return( I*theta_dot_dot + B*theta_dot + G + Kp*(theta_ref-theta) + Kd*(theta_dot_ref-theta_dot));
}
