Major Tasks:
============
1. Program to be Dhwani, requires:
	- Intent analyzer, like, https://github.com/slapbot/sounder
	- Audio Recorder and Speaker interface using [PortAudio](http://www.portaudio.com/)
	- STT and TTS speech engine
		* Julius
		* PocketSphinx
		* Google Cloud Speech
		* Wit.ai
		* Houndify
	- API key support
	- Sound corpus for Open Source Speech engine alternatives
	- Ability for other developers to contribute and write modules at will.
	- Features [ Important ]:
		* Ability to train your own dhwani
		* Emotion detector and friendly chatbot
		* In case, the output is not satisfactory, or input is not understood, the report will be generated for developers to improve the part (feature that is lacked in every virtual assistant till yet)

2. Setup script that will do:
	- Server setup
	- App support
	- Website Interface for demo, documentation and users
	- 
	
3. Configuration script that will:
	- Configure the User configurations such as name, email, twitter, spotify etc.
	- Decide on the preinstalled modules and speech engine to use.
	- Whether the user wants to train the program themselves or not.
	- Whether they want their dhwani to connect to remote server

4. Secure infrastructure
	- the program will have a central repository updated with training and feedback of contributors all over the world.
	- User will have option to either stay away from hassle and use the central updated code, and features or train their assistant themselves along with the updates.
	- Setting up some rules for the assistant that can't be override without user's permission.


# NLP task
- Convert Voice to Text string
- Tokenize Text
- Filter the intent of the sentence and categorise it as:
    - Action statement, commands
    - Compound statements, i.e. multiple commands
    - 
    - 


# Sounder/Intent analyzer

# Infrastructure
- Port management for the secure transmission
- Offline working
- API support

Task to do:
===========

* [ ] Convert Voice to Text String.
* [ ] Tokenize Text
* [ ] Filter the commands and other conversational from the token to perform the following tasks: 
	- Sentimental Analysis
	- Manage System operations like Open Browser
* [ ] Sound/Visual Feedback for the completion of task.


Framework, to create skills as in alexa.

Reference:
* https://slapbot.github.io/documentation/configuration/
* http://jasperproject.github.io/

