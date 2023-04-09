## Evolution of Traffic Jams
When driving along a highway, traffic can seem to just appear. Take a one lane highway. Traffic flows continuously until a small disturbance causes a driver to brake a little. The driver behind brakes a little harder, the driver behind them does the same until someone comes to a complete stop. Though the small disturbance is long gone, its effects can be felt for hours afterwards. Our goal for this project was to better understand how these “phantom traffic jams” perpetrate in a system, and to visually show how the actions of one driver can quickly lead to effects felt by everyone on the road. 

For the design process of our simulation, we started with an inspiration, or question that we wanted to explore: how can we visualize and better understand phantom traffic jams. We found previous examples of simulations that tried to explain the behavior, and chose pieces such as the equations from a paper published in 2000 by Martin Treiber, Ansgar Hennecke, and Dirk Helbing, that we believed to best represent driver behavior. Next, we moved onto the ideation for our simulation, or the formation of our core concepts. We decided to create a simulation that shows how one disturbance leads to lasting effects. Lastly, we implemented this core concept by simulating a loop, where cars leaving traffic congestion return to enter the traffic jam. We chose to use a loop of cars so that we could reuse cars exiting the jam and so that we could observe how the traffic congestion moved in a system.

FIGURE 1: “Cars” represented as circles in their equidistant starting position

![image](https://user-images.githubusercontent.com/127057159/230755681-6024d91a-845d-4dd6-9034-2199cf6f0bae.png)

FIGURE 2: “Cars” entering and exiting traffic congestion

![image](https://user-images.githubusercontent.com/127057159/230755687-4cfe381c-ce59-4a22-8304-07dd1b971dc0.png)

Because we were focusing on how individual actions lead to phantom traffic jams, we had to simulate traffic on a microscopic scale, which simulates the individual behaviors of cars. A macroscopic simulation, on the other hand, would simulate traffic density over a larger scale. To implement a microscopic model, we had to find a way to describe the behavior of individual drivers. To do this, we followed what the paper’s authors termed the “intelligent driver model.” The main component of this model is the equation shown below, which updates the acceleration of an individual car based on information about that car and the car directly in front of it.

![image](https://user-images.githubusercontent.com/127057159/230755774-606fa3da-ee2b-4dbf-9109-f6fd1dcf196d.png)


This equation states that the variables affecting a vehicle’s acceleration are a_i , it’s current acceleration, v_i , it’s current velocity, v_0 , the vehicle’s max speed, δ, a parameter controlling the smoothness of a vehicle’s acceleration, s_0 ,  the minimum desired distance between two cars, T_i , the reaction time of the driver, Δv_i , the difference between this vehicle and the next vehicle’s speeds, and b_i , the maximum comfortable deceleration for the vehicle. 

In our simulation, we chose to represent each car as an object with its own acceleration, velocity, and position. We then created a Simulation class that managed an array of every car on the road being simulated, and had a main file containing the simulation loop and managing the animation of the cars. Using the equation above, we were able to iterate through the array of each car in the loop and update its acceleration based on the car in front of it. Once we had the car’s new acceleration, we could also update its velocity and position. Our simulation loop continuously updates the state of each car and redraws the circle representing that car onto the screen, showing its movement over time.

The results of our simulation showed the real-world behavior we expected. We were able to visually see how the different rates for cars entering the traffic jam and cars exiting the traffic jam lead to the jam growing and shrinking. We observed a chain of equidistant vehicles moving with the same velocity did not remain in this nice configuration when we introduced a relatively minor obstruction. Instead, the disturbance grows as the congestion condenses in our simulation. Depending on the variables affecting a vehicle’s acceleration, we observed cars entering and exiting at different rates. When cars entered the traffic jam more quickly than they exited, the traffic grew, and when cars exited the traffic jam more quickly than they entered, the traffic dissipated. 

**Work Cited**

Treiber, Martin, Ansgar Hennecke, Dirk Helbing. ‘Congested traffic states in empirical observations and microscopic simulations’. Phys. Rev. E 62 (2000): 1805–1824. Web.
