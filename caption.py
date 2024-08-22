import requests
import streamlit as st
import base64

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Provide the path to your image file
img_path = r"C:\Users\pandian\OneDrive\Pictures\Desktop\ai app\wallaper.jpg"

# Convert the image to base64
img_base64 = get_img_as_base64(img_path)

# Create the background image CSS
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/jpeg;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
[data-testid="stHeader"] {{
    background: rgba(0, 0, 0, 0);
}}
</style>
"""

# Apply the background image
st.markdown(page_bg_img, unsafe_allow_html=True)

# Add content to the Streamlit app
st.title("img to text")
st.write("Hi,There")

# Define API details
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
headers = {"Authorization": "Bearer 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"}

# Function to query the Hugging Face model
def query(image_bytes):
    response = requests.post(API_URL, headers=headers, files={"file": image_bytes})
    return response.json()

# Streamlit file uploader
uploaded_file = st.file_uploader("Upload an image", type="jpg")

# Process the uploaded image
if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    # Get the raw bytes of the uploaded image
    image_bytes = uploaded_file.getvalue()
    
    # Query the API with the image bytes
    output = query(image_bytes)
    
    # Display the output
    if "error" in output:
        st.write("Error:", output["error"])
    else:
        st.write("Generated Caption:")
        st.write(output)
