# Streamlit Password Generator 🔐

## Overview 🚀
This is a **Password Generator** built using [Streamlit](https://streamlit.io/). It allows users to generate random, secure passwords with customizable options such as:

✅ Adjustable password length (6-30 characters)  
✅ Option to include digits 🔢  
✅ Option to include special characters 🎭  
✅ Large font display for the generated password ✨  
✅ Beautiful background styling 🎨  

## Features 🎯
- Simple & easy-to-use **slider** for password length selection
- **Checkboxes** to include digits and special characters
- **Button click** to generate passwords instantly
- **Large font display** for better visibility
- Custom background image for an aesthetic UI
- Built with ❤️ by [Sania Tariq]

## Installation 🛠️
To run this app locally, follow these steps:

### 1️⃣ Clone the Repository
```sh
 git clone <repository-url>
 cd <project-folder>
```

### 2️⃣ Install Dependencies
Make sure you have **Python 3.x** installed. Then, install the required packages:
```sh
pip install streamlit python-dotenv google-generativeai
```

### 3️⃣ Run the App 🏃‍♂️
```sh
streamlit run app.py
```

## Usage 📌
1. Adjust the **password length** using the slider.
2. Select checkboxes to include **digits** and **special characters**.
3. Click the **"Generate Password"** button.
4. Your generated password will be displayed in **large font**.

## Custom Styling 🎨
The app includes a custom **background image**:
```python
st.markdown(
    """
    <style>
        .stApp {
            background-image: url("https://i.pinimg.com/736x/5c/f7/12/5cf712daad50b04c91f31aab21d53456.jpg");
            background-size: cover;
            background-position: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)
```

## Contribution 🤝
Feel free to contribute to improve this project! Fork, clone, and submit a pull request. 😊

## License 📜
This project is open-source and available under the **MIT License**.

---

💻 **Happy Coding!** 🎉

