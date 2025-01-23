import streamlit as st
from pyqrcode import create
from io import BytesIO

def generate_qr_code(data):
    qr = create(data)

    buffer = BytesIO()
    qr.png(buffer, scale=6)
    buffer.seek(0)

    return buffer

def main():
    st.set_page_config(page_title="Shivi's QR Code Generator", layout="centered")

    st.title("Shivi's QR Code Generator")

    data = st.text_input("Enter the Text or URL for the QR code:", placeholder="Type here...")

    if st.button("Generate QR Code" , key="generate_qr"):
        if data.strip() == "":
            st.error("Please enter valid data to generate a QR code.")
        else:
            buffer = generate_qr_code(data)

            st.image(buffer, caption="Your QR Code", use_container_width=True, output_format="PNG")

            st.download_button(
                label="Download QR Code",
                data=buffer,
                file_name="QRCode.png",
                mime="image/png"
            )


    st.markdown("---")
    st.markdown(
        "Created with ❤️ for **Shivi and Team**"
    )

if __name__ == "__main__":
    main()
