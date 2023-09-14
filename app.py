import streamlit as st

#Sidebar
st.sidebar.header('Review')
st.sidebar.file_uploader('', type=['pdf', 'docx'])

#Main Section
st.title('NDA Comparisor')

slide_number = st.slider('Scroll through paragraphs', 1, 3, 1)

if slide_number == 1:

    #create two columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Template NDA')
        st.write('Template NDA text which is very long and has a lot of text in it. It is so long that it is going to be cut off in the middle of a sentence.')
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
