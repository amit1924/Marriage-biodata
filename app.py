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

# Load your images
image = Image.open("profile.jpg")
ganesh_image = Image.open("Ganeshaa.png")
photos = [
    Image.open("p-8.jpg"),  # Replace with your photo file paths
    Image.open("p-2.jpg"),
    Image.open("p-9.jpg"),
]

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
        f"**Current Address:** <span class='answer'> West Patel Nagar Patna</span>",
        unsafe_allow_html=True,
    )

    st.write(
        f"**Village:** <span class='answer'> Dakhram (Darbhanga)</span>",
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

    st.header("Contact Information")
    st.write(
        "**Contact:** <span class='answer'>9431629191</span>", unsafe_allow_html=True
    )
    # Partner Preferences
    st.header("Partner Preferences")
    preferred_age = st.slider("Preferred Age Range", 18, 40, (25, 30))
    preferred_height = st.text_input("Preferred Height Range", "5'2\" - 5'5\"")
    preferred_education = st.text_input("Preferred Education", "Graduate or above")
    preferred_occupation = st.text_input("Preferred Occupation", "Not Mandatory")

    # State variable to control summary visibility
    if "show_summary" not in st.session_state:
        st.session_state.show_summary = False

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
            "**Grandfather:** <span class='answer'>Kailash  Jha, Retired from All India Radio</span>",
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

    if st.button("Show Biodata Summary"):
        st.session_state.show_summary = True

    # Maps Section
    st.header("Location Map")
    st.write("Here is the location where I reside:")

    # Embed Google Map
    google_maps_url = (
        "https://www.google.com/maps/embed?pb=!"  # Replace with your own embed URL
    )
    st.markdown(
        f'<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d648472.8122326031!2d85.02088603073184!3d26.12045422176567!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sin!4v1723266602593!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',
        unsafe_allow_html=True,
    )

elif options == "Pictures":
    st.title("My Photos")
    for photo in photos:
        st.image(photo, width=700)
