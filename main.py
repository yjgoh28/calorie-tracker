
import streamlit as st
from image_processing import encode_multiple_images
from api import get_nutrition, NutritionInfo
from database import create_db_and_tables, get_session
from query_module import query_database


def save_nutrition_info(nutrition_info: NutritionInfo, session):
    session.add(nutrition_info)
    session.commit()


def main():
    st.title("Calorie Tracker")

    # Create database and tables if they don't exist
    create_db_and_tables()

    # Image upload
    uploaded_images = st.file_uploader("Select images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    if uploaded_images:
        encoded_images = encode_multiple_images(uploaded_images)
        st.write("Encoded images:")

        for i, encoded_image in enumerate(encoded_images):

            # Extract nutrition information
            try:
                nutrition_info = get_nutrition(encoded_image)

                # Save the nutrition information in the database
                with get_session() as session:
                    save_nutrition_info(nutrition_info, session)

                st.write(f"Nutrition information for Image {i+1} has been saved to the database.")
            except Exception as e:
                st.write(f"Error extracting nutrition information for Image {i+1}: {e}")

    # Chat textbox (though not used in this implementation)
    chat_input = st.text_input("Enter your message")
    
    if chat_input:
        response = query_database(chat_input)
        st.write(response)


if __name__ == "__main__":
    main()