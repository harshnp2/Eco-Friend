# libraries
import io

import cv2
import cv2 as cv
import requests
from PIL import Image
from requests_toolbelt.multipart.encoder import MultipartEncoder
import time

# function for detecting trash
def detecting_object():
    # accesses camera
    cam = cv.VideoCapture(0)

    # this variable will be used to break out of the main while loop
    time_to_leave = False

    # the trash type of each of these objects
    objects_dict = {
        'PLASTIC': 'RECYCLING',
        'CARDBOARD': 'RECYCLING',
        'BIODEGRADABLE': 'Blank',
        'GLASS': 'GARBAGE',
        'METAL': 'RECYCLING',
        'PAPER': 'RECYCLING',
    }
    while True:
        # reads what your camera shows
        isTrue, frame = cam.read()

        # shows the view of the camera
        cv.imshow("Camera", frame)
        # keeps delaying and then takes a picture to check later if an object that was specified in the dictionary was detected
        cv.waitKey(5)
        cv.imwrite('pic.png', frame)
        image = cv.imread('pic.png')
        pilImage = Image.fromarray(image)

        buffered = io.BytesIO()
        pilImage.save(buffered, quality=100, format="PNG")

        # Build multipart form and post request
        m = MultipartEncoder(fields={'file': ("imageToUpload", buffered.getvalue(), "image/jpeg")})

        # used the past info that we collected and put into this site to check if one of the objects specified was detected
        response = requests.post("https://detect.roboflow.com/garbage-classification-3/2?api_key=kQE5W7nH700WcHLhL9TN",
                                 data=m, headers={'Content-Type': m.content_type})


        # go to the predictions part of the dictionary
        predictions_list = response.json().get('predictions')

        # if predications_list is there executes the code below
        if bool(predictions_list) == True:
            type_of_object = response.json().get('predictions')[0].get('class')
            confidence_level = response.json().get('predictions')[0].get('confidence')
            print(confidence_level)
        # if type_of_object and confidence level is in the predictions_list then it will execute the code below
        if bool(type_of_object) & bool(confidence_level) != False:
            # will execute the code blow if the confidence level is above 0.6
            if confidence_level > 0.6:
                # gets the x value, y value, height, and width from response.json()
                x = int(response.json().get('predictions')[0].get('x'))
                y = int(response.json().get('predictions')[0].get('y'))
                width = int(response.json().get('predictions')[0].get('width'))
                height = int(response.json().get('predictions')[0].get('height'))
                x = int(x - (1 / 2)*width)
                y = int(y - (1 / 2)*height)
                # prints the type_of_trash that the object is by going to the dictionary first and seeing which type_of_trash is associated with it
                text = objects_dict[type_of_object]
                print(text)

                # draws bounding box around object detected
                bbox = cv.rectangle(frame, (x,y), (x + width, y + height), (255, 0, 0), 2)
                # puts a label on the box
                label = cv.putText(bbox, text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))

                # destroys all windows
                cv.destroyAllWindows()

                # will show the frame for the bounding box around the image for 2 seconds
                while True:
                    cv.imshow("Camera", bbox)
                    cv.waitKey(1)
                    time.sleep(2)
                    # if leave out of the main while loop
                    time_to_leave = True
                    break


        # 'd' is pressed it will break out of the main while loop
        if cv.waitKey(1) & 0xFF == ord('d'):
            break

        # while break out of the main while loop if the satisifies the argument
        if time_to_leave is True:
            break

    # destrors all windows and ends program when out of the main while loop
    cam.release()
    cv.destroyAllWindows()
    # returns the text or the type_of_trash
    return text



