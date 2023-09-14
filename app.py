import streamlit as st

#Sidebar
st.sidebar.header('Review')
st.sidebar.file_uploader('', type=['pdf', 'docx'])

#Main Section
st.title('NDA Comparisor')

sample_nda_text = """ This Non-Disclosure Agreement (the “Agreement”) is entered into by and between [Company Name],
a [State] corporation, having a principal place of business at [Address] (“Company”), and [Name],
having a principal place of residence at [Address] (“Recipient”). <span style="background-color: red"> With respect to the disclosure of certain proprietary and confidential information </span>
that is described below, the parties agree to the following terms and conditions:
- Definition of Confidential Information. “Confidential Information” means any information disclosed by or on behalf of Company to Recipient,
whether before or after the date of this Agreement, <span style="background-color: yellow">that is not generally known to the public</span> and that Recipient should know given the facts and circumstances."""

slide_number = st.slider('Scroll through paragraphs', 1, 3, 1)

if slide_number == 1:

    #create two columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Template NDA')
        st.markdown(f'<div style="height:200px; overflow-y: auto;">{sample_nda_text}</div>',
                    unsafe_allow_html=True,)
        st.write("")
        st.write("")
    with col2:
        st.subheader('New NDA')
        st.write('Your NDA text which differs from the template NDA text. It is so long that it is going to be cut off in the middle of a sentence.')

    st.success('Differences: the new text is highlighted in green. The text is cut off in the middle of a sentence. Because the text is so long, the highlighting is not very accurate.')


if slide_number == 2:
    #create two columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Template NDA')
        st.write('Template NDA text which is very long and has a lot of text in it. It is so long that it is going to be cut off in the middle of a sentence.')
    with col2:
        st.subheader('New NDA')
        st.write('Your NDA text which differs from the template NDA text. It is so long that it is going to be cut off in the middle of a sentence.')

    st.error('Differences: the new text is highlighted in green. The text is cut off in the middle of a sentence. Because the text is so long, the highlighting is not very accurate.')


if slide_number == 3:
    #create two columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Template NDA')
        st.write('Template NDA text which is very long and has a lot of text in it. It is so long that it is going to be cut off in the middle of a sentence.')
    with col2:
        st.subheader('New NDA')
        st.write('Your NDA text which differs from the template NDA text. It is so long that it is going to be cut off in the middle of a sentence.')

    st.warning('Differences: the new text is highlighted in green. The text is cut off in the middle of a sentence. Because the text is so long, the highlighting is not very accurate.')
