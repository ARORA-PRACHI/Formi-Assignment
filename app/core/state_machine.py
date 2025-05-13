from enum import Enum  # Used to define chatbot states
from typing import Dict, Any  # For general data types
from pydantic import BaseModel  # For clean data handling
import jinja2  # Used to load and fill in message templates

# Step 1: Define all chatbot states
class State(str, Enum):
    GREETING = "greeting"
    FAQ = "faq"
    NEW_BOOKING = "new_booking"
    MODIFY_BOOKING = "modify_booking"
    CANCEL_BOOKING = "cancel_booking"
    CONFIRMATION = "confirmation"
    GOODBYE = "goodbye"

# Step 2: This keeps track of current state, past state, and user data
class StateContext(BaseModel):
    current_state: State
    previous_state: State = None
    entities: Dict[str, Any] = {}  # Example: {"booking_date": "May 15"}
    conversation_history: list = []  # Stores all messages exchanged

# Step 3: Main class that handles chatbot logic
class StateMachine:
    def __init__(self):
        # Load Jinja2 templates from the "templates" folder
        self.template_loader = jinja2.FileSystemLoader(searchpath="./templates")
        self.template_env = jinja2.Environment(loader=self.template_loader)

        # Start with GREETING state
        self.current_context = StateContext(current_state=State.GREETING)

    def get_state_prompt(self, state: State, context: Dict[str, Any]) -> str:
        """Loads the response template for a state and fills in info"""
        template = self.template_env.get_template(f"{state.value}.j2")
        return template.render(**context)  # Replaces {{}} in the template

    def transition(self, user_input: str):
        """Changes the chatbot's state based on what user says"""
        current_state = self.current_context.current_state
        response = ""

        # Example: User just joined, bot says hello and asks for help
        if current_state == State.GREETING:
            if "booking" in user_input.lower():
                self.current_context.previous_state = current_state
                self.current_context.current_state = State.NEW_BOOKING
                response = self.get_state_prompt(State.NEW_BOOKING, self.current_context.dict())
            elif "faq" in user_input.lower():
                self.current_context.previous_state = current_state
                self.current_context.current_state = State.FAQ
                response = self.get_state_prompt(State.FAQ, self.current_context.dict())
            else:
                response = "Hi there! I can help with bookings or questions about Barbeque Nation. What would you like to do?"

        # If bot is answering FAQs
        elif current_state == State.FAQ:
            response = "Here's some information you might find useful..."
            self.current_context.previous_state = current_state
            self.current_context.current_state = State.GREETING

        # If bot is handling a new booking
        elif current_state == State.NEW_BOOKING:
            if "confirm" in user_input.lower():
                self.current_context.previous_state = current_state
                self.current_context.current_state = State.CONFIRMATION
                response = self.get_state_prompt(State.CONFIRMATION, self.current_context.dict())
            else:
                response = "Please provide your booking details (date, time, guests)..."

        # If bot is confirming booking
        elif current_state == State.CONFIRMATION:
            self.current_context.previous_state = current_state
            self.current_context.current_state = State.GOODBYE
            response = self.get_state_prompt(State.GOODBYE, self.current_context.dict())

        # Return the updated state and message
        return self.current_context.current_state, response

    def update_context(self, key: str, value: Any):
        """Save something in memory like 'booking_date': 'May 20'"""
        self.current_context.entities[key] = value

    def add_to_history(self, role: str, content: str):
        """Save each message (who said what)"""
        self.current_context.conversation_history.append({
            "role": role,  # Either "user" or "bot"
            "content": content
        })
