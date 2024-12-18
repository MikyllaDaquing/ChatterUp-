from uuid import uuid4
from nicegui import ui

messages = []   # list for storing messages.

# a function dynamically refreshes and displays chat messages.
@ui.refreshable
def chat_message(own_id):

    # a loop that iterates over a collection of messages and renders each chat message in a user interface using "ui.chat_message()".
    for user_id, avatar, text in messages:
        ui.chat_message(avatar = avatar, text = text, sent = user_id == own_id)

# Main chat page setup. This creates the user session, the chat interface, and the input field for sending messages.
@ui.page('/')
def index():

    # Send function. Handles sending messages.
    def send():
        messages.append((user, avatar, text.value))
        chat_message.refresh()
        text.value = ''     # Clears the input field after sending.
    
    user = str(uuid4())     # Unique user ID for each session.
    avatar = f'https://robohash.org/{user}?bgset=bg2'       # Unique avatar URL based on the user ID.

    with ui.column().classes('w-full items-stretch'):
        chat_message(user)      # Renders the chat interface.
    
    with ui.footer().classes('bg-pink'):    # creates a footer with a soft pink background
        with ui.row().classes('w-full items-center'):   # Creates a container that arranges child elements horizontally
            with ui.avatar():
                ui.image(avatar)    # Displays the user's avatar. 
            
            # creates a text input field
            text = ui.input(placeholder = 'messages') \
                .props('rounded outlined').classes('flex-grow') \
                .on('keydown.enter', send)       
                # Sends the message when the Enter key is pressed.

ui.run()    # starts NiceGUI application. 
