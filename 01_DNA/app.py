from numpy import string_
import pandas as pd
import streamlit as st
import altair as alt
# from PIL import image

st.write("""
# DNA Nucleotide Counter APP

Now let's count DNA Nucleotide of query DNA

***
""")

st.header("Enter DNA Sequence")

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence Input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = "".join(sequence)

st.write("""
***
""")

st.header('INPUT (DNA Query)')
st.text(sequence)

st.header('OUTPUT (DNA Nucleotide Count)')

def DNA_nucleotide_count(seq:str) -> dict:
    d = dict([
        ('Adenine', seq.count('A')),
        ('Thymine', seq.count('T')),
        ('Guanine', seq.count('G')),
        ('Cytosine', seq.count('C')),
    ])

    return d

X = DNA_nucleotide_count(sequence)

for k,v in X.items():
    st.write(f'There are {str(v)} {k}')

st.subheader('Display in Dataframe')
df = pd.DataFrame.from_dict(X, orient='index', columns=['count'])
df.reset_index(inplace=True)
df = df.rename(columns= {'index': 'nucleotide'})
st.write(df)

p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count',
)

p = p.properties(
    width=alt.Step(80)
)

st.write(p)