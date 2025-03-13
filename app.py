import streamlit as st
import random
import openai
import pandas as pd  # Useful if you want to display or manage data in a table format later

# -------------------------------
# Define Art Prompt Categories
# -------------------------------
themes = ["Nature", "Surrealism", "Historical", "Abstract", "Futuristic"]
techniques = ["Watercolor", "Charcoal", "Oil Painting", "Digital", "Mixed Media"]
styles = ["Impressionism", "Cubism", "Realism", "Pop Art", "Minimalism"]

# -------------------------------
# Optional: OpenAI API Integration
# -------------------------------
def generate_openai_prompt(selected_theme, selected_technique, selected_style):
    """
    Generate a creative art prompt using the OpenAI API.
    Ensure that you have added your OpenAI API key in Streamlit secrets as OPENAI_API_KEY.
    """
    # Set your OpenAI API key from Streamlit secrets
    openai.api_key = st.secrets.get("OPENAI_API_KEY")
    
    # Build the prompt for OpenAI
    prompt_text = (
        f"Generate a creative and detailed art prompt that combines the following elements: "
        f"a {selected_theme} theme, using {selected_technique} technique, and executed in a {selected_style} style."
    )
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt_text,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.8
        )
        generated_prompt = response.choices[0].text.strip()
        return generated_prompt
    except Exception as e:
        st.error("Error calling the OpenAI API: " + str(e))
        return None

# -------------------------------
# Main App Function
# -------------------------------
def main():
    st.title("AI-Powered Art Prompt Generator")
    st.write("Create unique art prompts by mixing art themes, techniques, and styles. "
             "Choose your categories below and generate a prompt!")

    # Create dropdowns for each art prompt category
    selected_theme = st.selectbox("Select Theme", themes)
    selected_technique = st.selectbox("Select Technique", techniques)
    selected_style = st.selectbox("Select Style", styles)

    # Checkbox to optionally use OpenAI for creative prompt generation
    use_openai = st.checkbox("Use OpenAI for creative prompt generation")

    # When the user clicks the button, generate a prompt
    if st.button("Generate Art Prompt"):
        if use_openai:
            # Generate prompt via OpenAI API
            generated_prompt = generate_openai_prompt(selected_theme, selected_technique, selected_style)
            if generated_prompt:
                st.success("Generated Art Prompt (via OpenAI):")
                st.write(generated_prompt)
            else:
                st.error("Failed to generate a prompt using the OpenAI API.")
        else:
            # Generate a random prompt by randomly mixing categories
            random_theme = random.choice(themes)
            random_technique = random.choice(techniques)
            random_style = random.choice(styles)
            prompt = (
                f"Create an art piece with a {random_theme.lower()} theme, using "
                f"{random_technique.lower()} technique, and rendered in a {random_style.lower()} style."
            )
            st.success("Generated Art Prompt:")
            st.write(prompt)

# Run the app
if __name__ == "__main__":
    main()
