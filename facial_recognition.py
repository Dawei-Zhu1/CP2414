"""
NumPy show be downgraded to 1.26.4
"""
import face_recognition
import cv2
import numpy as np
import os
import glob

import tkinter as tk
from tkinter import filedialog


class FacialRecognition:
    """
    The basic structure of the Facial Recognition Class is reformed from
    https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py
    """

    def __init__(self, directory_of_faces: str):
        # This is a demo of running face recognition on live video from your webcam.
        # It's a little more complicated than the other example,
        # but it includes some basic performance tweaks to make things run a lot faster:
        #   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
        #   2. Only detect faces in every other frame of video.

        # PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
        # OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
        # specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

        # Get a reference to webcam #0 (the default one)
        self.video_capture = cv2.VideoCapture(0)

        # Create arrays of known face encodings and their names
        self.known_face_encodings = list()
        self.known_face_names = list()
        self.current_working_directory = os.getcwd()
        # self.faces_on_screen = list()
        if directory_of_faces:
            self.train_faces(directory_of_faces)

    def train_faces(self, directory):
        types = ('*.jp*g', '*.png')
        for t in types:
            search_pattern = os.path.join(directory, t)
            for file_path in glob.glob(search_pattern):
                self.train_a_face(file_path)

    def train_a_face(self, file_directory):
        """
        Train single face
        """
        _face = face_recognition.load_image_file(file_directory)
        _face_encoding = face_recognition.face_encodings(_face)[0]
        _name_of_face = os.path.basename(file_directory)
        self.known_face_encodings.append(_face_encoding)
        self.known_face_names.append(os.path.splitext(_name_of_face)[0])

    def recognize_face(self, person_to_validate) -> bool:
        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        is_time_to_quit = False
        is_face_match = False
        cv2.startWindowThread()
        while not is_time_to_quit:
            # Grab a single frame of video
            ret, frame = self.video_capture.read()

            # Only process every other frame of video to save time
            if process_this_frame:
                # Resize frame of video to 1/4 size for faster face recognition processing
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Unknown"

                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     name = known_face_names[first_match_index]

                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]

                    face_names.append(name)

                    # Key part
                    if person_to_validate in face_names:
                        is_face_match = True

            process_this_frame = not process_this_frame

            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Face Recognition', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q') or is_face_match:
                is_time_to_quit = True
                # Release handle to the webcam
                self.video_capture.release()
                cv2.destroyAllWindows()
                cv2.waitKey(1)

        return is_face_match


def input_photo() -> str:
    """
    Prompt a dialog to select photo
    """
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    # while not file_path:
    #     file_path = filedialog.askopenfilename()
    return file_path


def main():
    folder_of_faces = 'data/faces'
    # src_directory = input_photo()
    program = FacialRecognition(folder_of_faces)

    program.recognize_face('zdw')


if __name__ == '__main__':
    main()
