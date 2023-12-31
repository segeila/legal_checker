import streamlit as st

#st.set_page_config(layout="wide")

#Sidebar
st.sidebar.header('Review')
st.sidebar.file_uploader('', type=['pdf', 'docx'])
st.sidebar.header('Download')
st.sidebar.download_button(label = "Download", data = "data", file_name = "file_name", mime = None, key = None)

#Main Section
st.title('NDA Comparisor')

if 'paragraph_01' not in st.session_state:
    st.session_state.paragraph_clicked = None

sample_nda_text = """NON-DISCLOSURE AGREEMENT (NDA)
This Nondisclosure Agreement or ("Agreement") has been entered into on the date of ______________________________ and is by and between:
Party Disclosing Information: ______________________________ with a mailing address of ____________________________________________________________ (“Disclosing Party”).
Party Receiving Information: ______________________________ with a mailing address of ____________________________________________________________ (“Receiving Party”).
For the purpose of preventing the unauthorized disclosure of Confidential Information as defined below. The parties agree to enter into a confidential relationship concerning the disclosure of certain proprietary and confidential information ("Confidential Information").
1. Definition of Confidential Information. For purposes of this Agreement, "Confidential Information" shall include all information or material that has or could have commercial value or other utility in the business in which Disclosing Party is engaged. If Confidential Information is in written form, the Disclosing Party shall label or stamp the materials with the word "Confidential" or some similar warning. If Confidential Information is transmitted orally, the Disclosing Party shall promptly provide writing indicating that such oral communication constituted Confidential Information.
2. Exclusions from Confidential Information. Receiving Party's obligations under this Agreement do not extend to information that is: (a) publicly known at the time of disclosure or subsequently becomes publicly known through no fault of the Receiving Party; (b) discovered or created by the Receiving Party before disclosure by Disclosing Party; (c) learned by the Receiving Party through legitimate means other than from the Disclosing Party or Disclosing Party's representatives; or (d) is disclosed by Receiving Party with Disclosing Party's prior written approval.
3. Obligations of Receiving Party. Receiving Party shall hold and maintain the Confidential Information in strictest confidence for the sole and exclusive benefit of the Disclosing Party. Receiving Party shall carefully restrict access to Confidential Information to employees, contractors and third parties as is reasonably required and shall require those persons to sign nondisclosure restrictions at least as protective as those in this Agreement. Receiving Party shall not, without the prior written approval of Disclosing Party, use for Receiving Party's benefit, publish, copy, or otherwise disclose to others, or permit the use by others for their benefit or to the detriment of Disclosing Party, any Confidential Information. Receiving Party shall return to Disclosing Party any and all records, notes, and other written, printed, or tangible materials in its possession pertaining to Confidential Information immediately if Disclosing Party requests it in writing.
4. Time Periods. The nondisclosure provisions of this Agreement shall survive the termination of this Agreement and Receiving Party's duty to hold Confidential Information in confidence shall remain in effect until the Confidential Information no longer qualifies as a trade secret or until Disclosing Party sends Receiving Party written notice releasing Receiving Party from this Agreement, whichever occurs first.
       Copyright © 2020 NonDisclosureAgreement.com. All Rights Reserved. Page 1 of 2

<span style="background:yellow"> 5. Relationships. Nothing contained in this Agreement shall be deemed to constitute either party a partner, joint venture or employee of the other party for any purpose.</span>
6. Severability. If a court finds any provision of this Agreement invalid or unenforceable, the remainder of this Agreement shall be interpreted so as best to affect the intent of the parties.
7. Integration. This Agreement expresses the complete understanding of the parties with respect to the subject matter and supersedes all prior proposals, agreements, representations, and understandings. This Agreement may not be amended except in writing signed by both parties.
8. Waiver. The failure to exercise any right provided in this Agreement shall not be a waiver of prior or subsequent rights.
<span style="background:red"><a hreaf="#" id="my-link">9. Notice of Immunity. Employee is provided notice that an individual shall not be held criminally or civilly liable under any federal or state trade secret law for the disclosure of a trade secret that is made (i) in confidence to a federal, state, or local government official, either directly or indirectly, or to an attorney; and (ii) solely for the purpose of reporting or investigating a suspected violation of law; or is made in a complaint or other document filed in a lawsuit or other proceeding, if such filing is made under seal.</a></span> An individual who files a lawsuit for retaliation by an employer for reporting a suspected violation of law may disclose the trade secret to the attorney of the individual and use the trade secret information in the court proceeding, if the individual (i) files any document containing the trade secret under seal; and (ii) does not disclose the trade secret, except pursuant to court order.
This Agreement and each party's obligations shall be binding on the representatives, assigns and successors of such party. Each party has signed this Agreement through its authorized representative.
DISCLOSING PARTY
Signature: _____________________________________________________ Typed or Printed Name: ___________________________ Date: _______________ RECEIVING PARTY
Signature: _____________________________________________________ Typed or Printed Name: ___________________________ Date: _______________
      Copyright © 2020 NonDisclosureAgreement.com. All Rights Reserved.
Page 2 of 2
"""

#1. Definition of Confidential Information. 
#2. Exclusions from Confidential Information. 
#3. Obligations of Receiving Party.
#7. Integration. 

paragraph_01 = """ Definition of Confidential Information. For purposes of this Agreement,
    "Confidential Information" shall include all information or material that has or could have commercial
    value or other utility in the business in which Disclosing Party is engaged. If Confidential Information is in written form, 
    he Disclosing Party shall label or stamp the materials with the word "Confidential" or some similar warning.
    If Confidential Information is transmitted orally, the Disclosing Party shall promptly provide writing indicating
    that such oral communication constituted Confidential Information"""

paragraph_02 = """ Exclusions from Confidential Information. Receiving Party's obligations under this Agreement
    do not extend to information that is: (a) publicly known at the time of disclosure or subsequently becomes publicly known
    through no fault of the Receiving Party; (b) discovered or created by the Receiving Party before disclosure by Disclosing Party;
    (c) learned by the Receiving Party through legitimate means other than from the Disclosing Party or Disclosing Party's
    representatives; or (d) is disclosed by Receiving Party with Disclosing Party's prior written approval. 
"""

paragraph_03 = """ Obligations of Receiving Party. Receiving Party shall hold and maintain the Confidential
    Information in strictest confidence for the sole and exclusive benefit of the Disclosing Party.
    Receiving Party shall carefully restrict access to Confidential Information to employees, contractors and third
    parties as is reasonably required and shall require those persons to sign nondisclosure restrictions at least as
    protective as those in this Agreement. Receiving Party shall not, without the prior written approval of Disclosing Party,
    use for Receiving Party's benefit, publish, copy, or otherwise disclose to others, or permit the use by others for their
    benefit or to the detriment of Disclosing Party, any Confidential Information. Receiving Party shall return to
    Disclosing Party any and all records, notes, and other written, printed, or tangible materials in its possession pertaining
    to Confidential Information immediately if Disclosing Party requests it in writing.
"""


paragraph_07 = """
    Integration. This Agreement expresses the complete understanding of the parties with respect to the subject
    matter and supersedes all prior proposals, agreements, representations, and understandings. This Agreement may not
    be amended except in writing signed by both parties.
"""

#st.markdown(f'<div style="height:500px; overflow-y: auto;">{sample_nda_text}</div>', unsafe_allow_html=True,)

st.markdown(
    """
    <style>
    button[kind="primary"] {
        background: yellow!important;
        border: none;
        padding: 0!important;
        color: black !important;
        text-decoration: none;
        cursor: pointer;
        border: none !important;
        text-align: left !important;
    }
    button:hover[kind="primary"] {
        text-decoration: none;
        color: black !important;
    }
    button:focus[kind="primary"] {
        outline: none !important;
        box-shadow: none !important;
        color: black !important;
    }

    button[kind="secondary"] {
        background: #f0ad4e!important;
        border: none;
        padding: 0!important;
        color: black !important;
        text-decoration: none;
        cursor: pointer;
        border: none !important;
        text-align: left !important;
    }
    button:hover[kind="secondary"] {
        text-decoration: none;
        color: black !important;
    }
    button:focus[kind="secondary"] {
        outline: none !important;
        box-shadow: none !important;
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if st.button(paragraph_01, type = "primary"):
   st.session_state.paragraph_clicked = 1

st.write(paragraph_03)

if st.button(paragraph_02, type = "secondary"):
    st.session_state.paragraph_clicked = 2

st.write(paragraph_07)

st.write("")
st.write("")

if st.session_state.paragraph_clicked != None:
    with st.expander("Expander", expanded=True):
        st.write(f"You clicked paragraph {st.session_state.paragraph_clicked}")
        st.write("Similarity: 0.85")
        st.write("Action: Review")
        st.write("Matching paragraph:")
        st.write(paragraph_01)
