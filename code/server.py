from nlu import keyword_approach

__author__ = 'Ameya'


class RestaurantServer():
    def __init__(self):
        pass

    def start_server(self):
        """
        import speech_recognition as sr

        # Record Audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # Speech recognition using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("You said: " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        """
        keyword_approach.get_structured_input("I want a restaurant with average price at near vicinity")



if __name__ == '__main__':
    server = RestaurantServer()
    server.start_server()