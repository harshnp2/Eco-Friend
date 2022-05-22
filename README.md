# Eco-Friend
Changing the way we dispose trash

## Inspiration
After observing that in my high school cafeteria, no one pays attention to whether something is recycled or thrown away. I came up with the idea of making a trash sorter that uses object detection to recognize the object and the arduino to control the parts that organize the trash and make sure it doesn't overfill. This, I believe, has the potential to significantly benefit the environment.

## What it does
Eco Friend first recognizes the type of trash the user is holding up using my computer's camera and real-time object detection. Once the object has been detected and the type of trash has been sent to Arduino, the arduino will move the stepper motor shaft to open the opening, rotate the servo motor to move the slide to the correct bin (recycling or garbage), and the user will place the trash down the opening, allowing it to go to the correct bin with the help of the slide. The ultrasonic in each bin will continue to check for any changes in their readings. If there is, it means that the trash has been disposed of. After half a second, the ultrasonic sensor will check for any disturbance in its regular reading; if there is, it means that something at the top of the bin is blocking the ultrasonic sensor. Because the recycling/garbage has reached the top, it is full; therefore, send an email to the person who takes out the trash informing them that the garbage or recycling is full. After going through all of this, the camera will turn back on to detect any trash and repeat the process.

## How we built it
I constructed the trash sorter out of wood and cardboard. The microcontroller used to control the project's hardware was an arduino that was programmed in C++. The rest of the project's code was written in Python. The emails were sent using SMTPLib, the objects were detected using Roboflow, and the bounding boxes were drawn and labelled using OpenCV. Whatever was discovered was transmitted to the arduino via serial communication between the arduino and Python.

## Challenges we ran into
I first attempted to create a custom object detection model for detecting trash, but it took too long to load (after 5 hours, 10% of it was still untrained) due to the large dataset. Then I used a Roboflow pre-trained model and incorporated it into my code. I also had issues with serial communication between the arduino and Python, and it took me a while to figure out how to tell Python that the garbage/recycling bin was full before executing the code to send the email. Also, because I ran out of wood, I had to use cardboard to finish the project.

## Accomplishments that we're proud of
Although Eco Friend might not seem too complicated at first, it's application can be used to decrease our negative impacts on the environment. Since this was my first time using object detection, I am proud that it worked properly and that I didn't have troubling detecting objects. 

## What we learned
I learned how to work with wood, in terms of adding nails to it, drilling holes, etc. Also I learned how to use object detection, how to communicate between Arduino and Python, and send emails through Python.

## What's next for Eco Friend
To make Eco Friend even better, a larger and more accurate dataset can be used to detect many more objects. Also another bin can be added for organic materials and with the help of a camera module, the project can be more compact and look cleaner.
