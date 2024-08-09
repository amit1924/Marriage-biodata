import streamlit as st
from PIL import Image
from streamlit_chat import message as st_message  # Import streamlit_chat

# Set page config to change the title
st.set_page_config(page_title="Marriage Biodata", page_icon=":ring:")

# Custom CSS for larger fonts and colors
st.markdown(
    """
    <style>
    h1 {
        font-size: 3em; 
        color: #2E86C1; /* Title color */
        text-align: center; /* Center the title */
    }
    h2 {
        font-size: 2.5em; 
        color: #2874A6; /* Section headers color */
    }
    h3 {
        font-size: 2em; 
        color: #1F618D; /* Sub-headers color */
    }
    p {
        font-size: 1.5em; 
        color: #34495E; /* Text color */
    }
    .answer {
        color: #28B463; /* Answers color */
        font-weight: bold;
    }
    .ganesh-text {
        font-size: 0.5em; 
        color: #FF5733; /* Custom color for Ganesh text */
        text-align: center; 
        margin: 20px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load your profile image
image = Image.open("profile.jpg")
# Load the Ganesh image and resize it
ganesh_image = Image.open("Ganeshaa.png")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ("Home", "Pictures"))

if options == "Home":
    # Display the Ganesh image at the top center
    st.image(ganesh_image, width=100, caption="Lord Ganesh", use_column_width=True)

    # App title
    st.title("Marriage Biodata - Amit Kumar")

    # Display the profile image
    st.image(image, caption="Amit Kumar", use_column_width=True)

    # Personal Information
    st.header("Personal Information")
    st.write(
        f"**Full Name:** <span class='answer'>Amit Kumar</span>", unsafe_allow_html=True
    )
    st.write(
        f"**Date of Birth:** <span class='answer'>19th August 1991</span>",
        unsafe_allow_html=True,
    )
    st.write(
        f"**Height:** <span class='answer'>5 foot 7 inches</span>",
        unsafe_allow_html=True,
    )
    st.write(f"**Weight:** <span class='answer'>66 kg</span>", unsafe_allow_html=True)
    st.write(
        f"**Address:** <span class='answer'>Patna West Patel Nagar, Village - Dakhram (Darbhanga)</span>",
        unsafe_allow_html=True,
    )

    # Education and Profession
    st.header("Education and Profession")
    st.write(
        "**Matriculation and 10+2:** <span class='answer'>CBSE</span>",
        unsafe_allow_html=True,
    )
    st.write(
        "**Engineering:** <span class='answer'>Electrical Engineering</span>",
        unsafe_allow_html=True,
    )
    st.write(
        "**Profession:** <span class='answer'>Software Developer (Freelancer)</span>",
        unsafe_allow_html=True,
    )

    # Family Details
    st.header("Family Details")
    st.write(
        "**Father:** <span class='answer'>Retired Gazetted Officer from Patna Secretariat</span>",
        unsafe_allow_html=True,
    )
    st.write(
        "**Mother:** <span class='answer'>Housewife</span>", unsafe_allow_html=True
    )
    st.write(
        "**Younger Sister:** <span class='answer'>Government School Teacher</span>",
        unsafe_allow_html=True,
    )
    st.write(
        "**Elder Brother:** <span class='answer'>Works in Private Company</span>",
        unsafe_allow_html=True,
    )
    st.write(
        "**Sister-in-Law:** <span class='answer'>Probationary Officer in BOB</span>",
        unsafe_allow_html=True,
    )
    st.write(
        "**Grandfather:** <span class='answer'>Kailash Chandra Jha, Retired from All India Radio</span>",
        unsafe_allow_html=True,
    )

    # Community Information
    st.header("Community Information")
    st.write(
        "**Caste:** <span class='answer'>Hindu Brahmin</span>", unsafe_allow_html=True
    )
    st.write("**Gotra:** <span class='answer'>Shandilya</span>", unsafe_allow_html=True)

    # Partner Preferences
    st.header("Partner Preferences")
    preferred_age = st.slider("Preferred Age Range", 18, 40, (25, 30))
    preferred_height = st.text_input("Preferred Height Range", "5'2\" - 5'5\"")
    preferred_education = st.text_input("Preferred Education", "Graduate or above")
    preferred_occupation = st.text_input("Preferred Occupation", "Not Mandatory")

    # State variable to control summary visibility
    if "show_summary" not in st.session_state:
        st.session_state.show_summary = False

    # Submit Button
    if st.button("Generate Biodata"):
        st.session_state.show_summary = True

    if st.session_state.show_summary:
        st.subheader("Biodata Summary")
        st.write(
            f"**Full Name:** <span class='answer'>Amit Kumar</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Date of Birth:** <span class='answer'>19th August 1991</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Height:** <span class='answer'>5 foot 7 inches</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Weight:** <span class='answer'>66 kg</span>", unsafe_allow_html=True
        )
        st.write(
            f"**Address:** <span class='answer'>Patna West Patel Nagar, Village - Dakhram (Darbhanga)</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Profession:** <span class='answer'>Software Developer (Freelancer)</span>",
            unsafe_allow_html=True,
        )
        st.write(
            "**Father:** <span class='answer'>Retired Gazetted Officer from Patna Secretariat</span>",
            unsafe_allow_html=True,
        )
        st.write(
            "**Mother:** <span class='answer'>Housewife</span>", unsafe_allow_html=True
        )
        st.write(
            "**Younger Sister:** <span class='answer'>Rashmi, Government School Teacher</span>",
            unsafe_allow_html=True,
        )
        st.write(
            "**Elder Brother:** <span class='answer'>Works in Private Company</span>",
            unsafe_allow_html=True,
        )
        st.write(
            "**Sister-in-Law:** <span class='answer'>Probationary Officer in BOB</span>",
            unsafe_allow_html=True,
        )
        st.write(
            "**Grandfather:** <span class='answer'>Kailash Chandra Jha, Retired from All India Radio</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Caste:** <span class='answer'>Hindu Brahmin</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Gotra:** <span class='answer'>Shandilya</span>", unsafe_allow_html=True
        )
        st.write(
            f"**Preferred Age Range:** <span class='answer'>{preferred_age[0]} - {preferred_age[1]}</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Preferred Height Range:** <span class='answer'>{preferred_height}</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Preferred Education:** <span class='answer'>{preferred_education}</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Preferred Occupation:** <span class='answer'>{preferred_occupation}</span>",
            unsafe_allow_html=True,
        )

        # Button to hide summary
        if st.button("Hide Summary"):
            st.session_state.show_summary = False

    # Maps Section
    st.header("Location Map")
    st.write("Here is the location where I reside:")

    # Coordinates for the map (you can change this to your preferred location)
    lat = 25.6162399  # Example latitude
    lon = 85.0943745  # Example longitude
    st.map(data={"lat": [lat], "lon": [lon]})

# Chatbot Section
st.header("Chatbot")

# Create session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input field for user message
user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input:
        # Append user message to chat history
        st.session_state.chat_history.append({"message": user_input, "is_user": True})

        # Here you would add your chatbot logic (for now, it just echoes back the message)
        response = f"You said: {user_input}"
        st.session_state.chat_history.append({"message": response, "is_user": False})

# Display chat messages
for chat in st.session_state.chat_history:
    if chat["is_user"]:
        st_message(chat["message"], is_user=True)
    else:
        st_message(chat["message"], is_user=False)

# Footer
st.markdown(
    "<p class='ganesh-text'>May Lord Ganesh bless this biodata.</p>",
    unsafe_allow_html=True,
)
