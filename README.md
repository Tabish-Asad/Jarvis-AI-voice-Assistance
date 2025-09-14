# Jarvis-AI-voice-Assistance
Built a Python-based voice assistant with wake-word activation to perform tasks like Google/Wikipedia search, opening websites, reporting time/date, and playing music using speech recognition and text-to-speech

## Objective
To develop an intelligent voice assistant that automates daily tasks, provides information through speech interaction, and improves user efficiency using Python, speech recognition, and text-to-speech technologies.

## process

- Initialize Text-to-Speech Engine: Set up pyttsx3 to enable Jarvis to speak responses.
- Greet the User: Check the current time and give a greeting (Good Morning/Afternoon/Evening).
- Listen for Wake Word: Continuously listen for the wake word “Jarvis” using speech_recognition.
- Activate on Wake Word: When “Jarvis” is detected, respond immediately and start listening for commands.
- Process Commands:
- Search Wikipedia for queries.
- Open websites like YouTube, Google, LinkedIn, Facebook, Stack Overflow.
- Play songs from a custom musicLibrary.
- Provide current time and date.
- Execute Actions: Perform the requested action through webbrowser or other Python modules.
- Return to Listening: After executing a command, go back to waiting for the wake word for the next instruction.
- Exit: Stop the assistant when the user says “sleep,” “exit,” or “quit.”
